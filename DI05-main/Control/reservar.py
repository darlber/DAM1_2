from PySide6.QtCore import QTimer, QDate, Signal
from PySide6.QtWidgets import QWidget, QMessageBox, QLabel

from Vistas.ui_frmReservas import Ui_Reservas


class Reservar(QWidget, Ui_Reservas):
    """
    Clase para gestionar la creación y edición de reservas.
    """

    reserva_guardada = Signal()

    def __init__(self, bd):
        """
        Inicializamos la clase y configuramos la interfaz de usuario.
        """
        super().__init__()

        self.setupUi(self)
        self.bd = bd
        self.salon = None
        self.reserva_seleccionada = None
        self.toast_label = None

        self.asg_tipoReserva.currentTextChanged.connect(self.opcionCongreso)
        self.asg_volver.clicked.connect(self.cerrar_ventana)

        self.cargar_clientes()

    def cargar_clientes(self):
        """
        Cargamos los clientes desde la base de datos y los añadimos al combo box.
        """
        resultado = self.bd.Consulta(
            "SELECT Id, Num_Identificacion, Nombre, Telefono FROM clientes"
        )

        if resultado != "Error":
            self.combo_identificacin.clear()
            self.clientes_dict = (
                {}
            )  # Diccionario para almacenar cliente_id -> (nombre, teléfono)

            self.combo_identificacin.addItem(
                "Seleccione un cliente", -1
            )  # Opción inicial

            for cliente_id, num_identificacion, nombre, telefono in resultado:
                self.combo_identificacin.addItem(num_identificacion, cliente_id)
                self.clientes_dict[cliente_id] = (
                    nombre,
                    telefono,
                )  # Guardamos los datos del cliente

            # Conectar evento para actualizar los datos del cliente seleccionado
            self.combo_identificacin.currentIndexChanged.connect(
                self.actualizar_datos_cliente
            )

            # Bloquear los campos de nombre y teléfono para evitar edición manual
            self.asg_lineaNombre.setEnabled(False)
            self.asg_lineaTel.setEnabled(False)

    def actualizar_datos_cliente(self):
        """
        Actualizamos los datos del cliente seleccionado en los campos correspondientes.
        """
        cliente_id = self.combo_identificacin.currentData()
        if cliente_id is None:  # Evita errores si no hay selección
            cliente_id = -1

        datos_cliente = self.clientes_dict.get(cliente_id, ("", ""))

        self.asg_lineaNombre.setText(datos_cliente[0])
        self.asg_lineaTel.setText(datos_cliente[1])

    def obtener_tipos_reserva(self):
        """
        Obtenemos los tipos de reserva desde la base de datos.
        """
        resultado = self.bd.Consulta(
            "SELECT tipo_reserva_id, nombre FROM tipos_reservas"
        )
        return resultado if resultado != "Error" else []

    def obtener_tipos_cocina(self):
        """
        Obtenemos los tipos de cocina desde la base de datos.
        """
        resultado = self.bd.Consulta("SELECT tipo_cocina_id, nombre FROM tipos_cocina")
        return resultado if resultado != "Error" else []

    def configurar_salon(self, salon):
        """
        Configuramos el salón seleccionado y cargamos los tipos de reserva y cocina.
        """
        self.salon = salon
        self.asg_tipoReserva.clear()
        self.asg_tipoCocina.clear()

        for tipo_id, tipo_nombre in self.obtener_tipos_reserva():
            self.asg_tipoReserva.addItem(tipo_nombre, tipo_id)

        for tipo_cocina_id, tipo_cocina_nombre in self.obtener_tipos_cocina():
            self.asg_tipoCocina.addItem(tipo_cocina_nombre, tipo_cocina_id)

        self.opcionCongreso(self.asg_tipoReserva.currentText())

    def opcionCongreso(self, tipo_reserva):
        """
        Habilitamos o deshabilitamos los campos específicos para congresos.
        """
        es_congreso = tipo_reserva == "Congreso"
        self.asg_numJorn.setEnabled(es_congreso)
        self.asg_checkBox.setEnabled(es_congreso)
        self.asg_textoCongreso.setEnabled(es_congreso)
        self.asg_textoCongreso.setVisible(es_congreso)
        self.asg_numJorn.setVisible(es_congreso)
        self.asg_checkBox.setVisible(es_congreso)

    def limpiar_campos(self):
        """
        Limpiamos todos los campos de entrada.
        """
        self.asg_lineaNombre.clear()
        self.asg_lineaTel.clear()
        self.combo_identificacin.setCurrentIndex(0)

        self.asg_fecha.setDate(QDate.currentDate())
        self.asg_tipoReserva.setCurrentIndex(0)
        self.asg_numeroAsis.clear()
        self.asg_numJorn.clear()
        self.asg_tipoCocina.setCurrentIndex(0)

    def guardar_reserva(self):
        """
        Guardamos una nueva reserva en la base de datos.
        """
        num_identificacion = self.combo_identificacin.currentText().strip()

        if not num_identificacion:
            QMessageBox.critical(self, "Error", "Seleccione un cliente válido")
            return

        resultado = self.bd.Consulta(
            "SELECT Id FROM Clientes WHERE Num_Identificacion = ?",
            (num_identificacion,),
        )

        if not resultado or resultado == "Error":
            return

        cliente_id = resultado[0][0]

        nombre_salon = self.salon
        resultado_salon = self.bd.Consulta(
            f"SELECT salon_id FROM salones WHERE nombre = '{nombre_salon}' LIMIT 1"
        )
        if resultado_salon and resultado_salon != "Error":
            salon_id = resultado_salon[0][0]
        else:
            QMessageBox.warning(self, "Error", "Salón no encontrado")
            return

        fecha_reserva = self.asg_fecha.text()
        tipo_reserva_id = self.asg_tipoReserva.currentData() or 0
        tipo_cocina_id = self.asg_tipoCocina.currentData() or 0
        numero_asistentes = self.asg_numeroAsis.text().strip()

        if not numero_asistentes.isdigit() or int(numero_asistentes) <= 0:
            QMessageBox.critical(
                self,
                "Error",
                "El número de asistentes debe ser un número válido y mayor a 0",
            )
            return

        resultado_reserva = self.bd.Consulta(
            "SELECT reserva_id FROM reservas WHERE id_Cliente = ? AND fecha = ?",
            (cliente_id, fecha_reserva),
        )

        if resultado_reserva and resultado_reserva != "Error":
            QMessageBox.critical(
                self,
                "Error",
                "Ya existe una reserva para esta fecha con el cliente seleccionado.",
            )
            return

        consulta = """INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, id_Cliente, fecha, ocupacion, jornadas, habitaciones)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        valores = (
            tipo_reserva_id,
            salon_id,
            tipo_cocina_id,
            cliente_id,
            fecha_reserva,
            int(numero_asistentes),
            0,
            0,
        )

        resultado = self.bd.Consulta(consulta, valores)

        if resultado != "Error":
            QMessageBox.information(self, "Éxito", "Reserva guardada correctamente")
            self.limpiar_campos()
            self.cerrar_ventana()
            self.reserva_guardada.emit()
        else:
            QMessageBox.critical(self, "Error", "El salón está ocupado en esa fecha")

    def actualizar_reserva(self):
        """
        Actualizamos una reserva existente en la base de datos.
        """
        if not self.reserva_seleccionada:
            QMessageBox.critical(
                self, "Error", "No hay una reserva seleccionada para actualizar."
            )
            return

        reserva_id = self.reserva_seleccionada[0]

        num_identificacion = self.combo_identificacin.currentText().strip()

        if not num_identificacion:
            QMessageBox.critical(self, "Error", "Seleccione un cliente válido")
            return

        resultado = self.bd.Consulta(
            "SELECT Id FROM Clientes WHERE Num_Identificacion = ?",
            (num_identificacion,),
        )

        print("Resultado de la consulta del cliente:", resultado)

        if not resultado or resultado == "Error":
            return

        cliente_id = resultado[0][0]
        print("ID del cliente encontrado:", cliente_id)

        nombre_salon = self.salon
        resultado_salon = self.bd.Consulta(
            f"SELECT salon_id FROM salones WHERE nombre = '{nombre_salon}' LIMIT 1"
        )
        if resultado_salon and resultado_salon != "Error":
            salon_id = resultado_salon[0][0]
        else:
            QMessageBox.warning(self, "Error", "Salón no encontrado")
            return

        fecha_reserva = self.asg_fecha.text()
        tipo_reserva_id = self.asg_tipoReserva.currentData() or 0
        tipo_cocina_id = self.asg_tipoCocina.currentData() or 0
        numero_asistentes = self.asg_numeroAsis.text().strip()

        if not numero_asistentes.isdigit() or int(numero_asistentes) <= 0:
            self.mostrar_error(
                "El número de asistentes debe ser un número válido y mayor a 0"
            )
            return

        resultado_conflict = self.bd.Consulta(
            "SELECT reserva_id FROM reservas WHERE id_Cliente = ? AND fecha = ? AND reserva_id != ?",
            (cliente_id, fecha_reserva, reserva_id),
        )
        if resultado_conflict and resultado_conflict != "Error":
            QMessageBox.critical(
                self,
                "Error",
                "Ya existe una reserva para esta fecha con el cliente seleccionado.",
            )
            return

        consulta = """UPDATE reservas
                    SET tipo_reserva_id = ?, salon_id = ?, tipo_cocina_id = ?, 
                        ocupacion = ?, jornadas = ?, habitaciones = ?, fecha = ?
                    WHERE reserva_id = ?"""
        valores = (
            tipo_reserva_id,
            salon_id,
            tipo_cocina_id,
            int(numero_asistentes),
            0,
            0,
            fecha_reserva,
            reserva_id,
        )

        resultado = self.bd.Consulta(consulta, valores)

        if resultado != "Error":
            QMessageBox.information(self, "Éxito", "Reserva actualizada correctamente")
            self.limpiar_campos()
            self.cerrar_ventana()
            self.reserva_guardada.emit()
        else:
            QMessageBox.critical(
                self, "Error", "Hubo un error al actualizar la reserva"
            )

    def cargar_reserva(self, reserva):
        """
        Cargamos los datos de una reserva existente en los campos correspondientes.
        """
        self.reserva_seleccionada = reserva

        self.reserva_id = reserva[0]
        index_numIdent = self.combo_identificacin.findText(reserva[11])
        if index_numIdent != -1:
            self.combo_identificacin.setCurrentIndex(index_numIdent)

        self.asg_lineaNombre.setText(reserva[2])
        self.asg_lineaTel.setText(reserva[3])
        self.asg_fecha.setDate(QDate.fromString(reserva[1], "dd/MM/yyyy"))
        self.asg_numeroAsis.setValue(reserva[6])
        self.asg_numJorn.setValue(reserva[7])
        self.asg_checkBox.setChecked(bool(reserva[9]))

        index_tipo = self.asg_tipoReserva.findData(reserva[5])
        if index_tipo != -1:
            self.asg_tipoReserva.setCurrentIndex(index_tipo)

        index_cocina = self.asg_tipoCocina.findData(reserva[8])
        if index_cocina != -1:
            self.asg_tipoCocina.setCurrentIndex(index_cocina)

        self.opcionCongreso(self.asg_tipoReserva.currentText())

    def mostrar_error(self, mensaje):
        """
        Mostramos un mensaje de error en un QLabel.
        """
        self.toast_label = QLabel(self)
        self.toast_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 200); color: white; padding: 10px; border-radius: 5px;"
        )
        self.toast_label.setText(mensaje)
        self.toast_label.setGeometry(200, 50, 300, 40)
        self.toast_label.setVisible(True)
        QTimer.singleShot(3000, self.ocultar_mensaje)

    def ocultar_mensaje(self):
        """
        Ocultamos el mensaje de error.
        """
        self.toast_label.setVisible(False)

    def cerrar_ventana(self):
        """
        Cerramos la ventana de reservas.
        """
        self.close()
