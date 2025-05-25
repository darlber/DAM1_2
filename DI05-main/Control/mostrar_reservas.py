from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QMainWindow,
    QListWidgetItem,
    QTableWidgetItem,
    QMessageBox,
)

from Control.reservar import Reservar
from Vistas.ui_frmMostrarReservas import Ui_MostrarReservas


class MostrarReservas(QMainWindow, Ui_MostrarReservas):
    """
    Clase para mostrar y gestionar las reservas de los salones.
    """

    def __init__(self, bd):
        """
        Inicializamos la clase y configuramos la interfaz de usuario.
        Métodos:
            __init__: Inicializamos la ventana principal, configuramos los iconos,
                      creamos la conexión a la base de datos y configuramos las señales y slots.
        Atributos:
            bd (BD): Instancia de la clase BD para manejar la base de datos.
            salon_seleccionado (None): Variable para almacenar el salón seleccionado.
            reserva_seleccionada (None): Variable para almacenar la reserva seleccionada.
            ventana_reservar (Reservar): Instancia de la clase Reservar para manejar la ventana de reservas.
        """
        super().__init__()

        self.bd = bd

        self.setupUi(self)
        self.asg_edit_reserva.setVisible(False)
        self.asg_consultar.setVisible(False)
        self.asg_eliminar.setVisible(False)
        self.asg_tablaWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.asg_tablaWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.introducirSalones()

        self.salon_seleccionado = None
        self.reserva_seleccionada = None

        self.ventana_reservar = Reservar(self.bd)

        self.asg_listaWidget.itemClicked.connect(self.seleccionar_salon)
        self.asg_edit_reserva.clicked.connect(self.abrir_ventana_editar)
        self.asg_botonReservar.clicked.connect(self.abrir_ventana_reservar)
        self.asg_tablaWidget.cellClicked.connect(self.seleccionar_reserva)
        self.asg_eliminar.clicked.connect(self.eliminar_reserva)
        self.asg_consultar.clicked.connect(self.abrir_consulta)

        self.ventana_reservar.reserva_guardada.connect(self.actualizar_reservas)

    def seleccionar_salon(self, salon):
        """
        Seleccionamos un salón de la lista y mostramos sus reservas en la tabla.
        """
        if not salon:
            print("No se ha seleccionado ningún salón.")
            return
        self.salon_seleccionado = salon.text()
        self.mostrar_reservas_en_tabla(self.salon_seleccionado)

    def seleccionar_reserva(self, row):
        """
        Seleccionamos una reserva de la tabla y mostramos sus detalles.
        """
        self.actualizar_reservas()
        fecha = self.asg_tablaWidget.item(row, 1).text()
        id_reserva = self.asg_tablaWidget.item(row, 0).text()

        print(f"Buscando reserva con id_reserva: {id_reserva} y fecha: {fecha}")

        consulta = """SELECT 
            r.reserva_id, 
            r.fecha, 
            c.Nombre AS nombre_cliente, 
            c.Telefono AS telefono_cliente, 
            r.id_Cliente,
            r.tipo_reserva_id, 
            r.ocupacion, 
            r.jornadas, 
            r.tipo_cocina_id, 
            r.habitaciones, 
            r.salon_id,
            c.Num_Identificacion
        FROM reservas r
        JOIN Clientes c ON r.id_Cliente = c.Id
        WHERE r.reserva_id = ? AND r.fecha = ?
        """

        resultado = self.bd.Consulta(consulta, (id_reserva, fecha))

        print(f"Resultado de la consulta: {resultado}")

        if not resultado or resultado == "Error":
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo obtener la información completa de la reserva.",
            )
            return

        self.reserva_seleccionada = resultado[0]

        self.asg_edit_reserva.setVisible(True)
        self.asg_consultar.setVisible(True)
        self.asg_eliminar.setVisible(True)

        print(f"Reserva seleccionada: {self.reserva_seleccionada}")

    def introducirSalones(self):
        """
        Introducimos los salones en la lista desde la base de datos.
        """
        datos = self.bd.Consulta("SELECT nombre FROM salones")
        self.asg_listaWidget.clear()

        for f, fila in enumerate(datos):
            print(f"Fila {f}: {fila}")
            item = QListWidgetItem(fila[0])
            self.asg_listaWidget.addItem(item)

    def obtener_reservas(self, salon):
        """
        Obtiene todas las reservas de un salón con información completa.
        """
        salon_id = self.obtener_id_salon(salon)
        if not salon_id:
            return []

        consulta = """SELECT 
            r.reserva_id,
            r.fecha, 
            c.Nombre AS persona, 
            c.Telefono AS telefono, 
            r.tipo_reserva_id,
            r.ocupacion,
            r.jornadas,
            r.tipo_cocina_id,
            r.habitaciones,
            c.Num_Identificacion
        FROM reservas r
        JOIN Clientes c ON r.id_Cliente = c.Id 
        WHERE r.salon_id = ? 
        ORDER BY r.fecha DESC;"""

        resultado = self.bd.Consulta(consulta, (salon_id,))
        if resultado == "Error":
            return []

        return resultado

    def obtener_id_salon(self, salon):
        """
        Obtenemos el ID de un salón a partir de su nombre.
        """
        consulta = """SELECT salon_id FROM salones WHERE nombre = ?"""
        resultado = self.bd.Consulta(consulta, (salon,))

        if resultado != "Error" and len(resultado) > 0:
            return resultado[0][0]
        else:
            return None

    def obtener_tipo_reserva(self, tipo_reserva_id):
        """
        Obtenemos el nombre del tipo de reserva a partir de su ID.
        """
        consulta = """SELECT nombre FROM tipos_reservas WHERE tipo_reserva_id = ?"""
        resultado = self.bd.Consulta(consulta, (tipo_reserva_id,))

        if resultado != "Error" and len(resultado) > 0:
            return resultado[0][0]
        else:
            return None

    def obtener_nombre_salon(self, salon_id):
        """
        Obtenemos el nombre del salón a partir de su ID.
        """
        consulta = """SELECT nombre FROM salones WHERE salon_id = ?"""
        resultado = self.bd.Consulta(consulta, (salon_id,))

        if resultado != "Error" and len(resultado) > 0:
            return resultado[0][0]
        else:
            return "Desconocido"

    def obtener_tipo_cocina(self, tipo_cocina_id):
        """
        Obtenemos el nombre del tipo de cocina a partir de su ID.
        """
        consulta = """SELECT nombre FROM tipos_cocina WHERE tipo_cocina_id = ?"""
        resultado = self.bd.Consulta(consulta, (tipo_cocina_id,))

        if resultado != "Error" and len(resultado) > 0:
            return resultado[0][0]
        else:
            return None

    def actualizar_reservas(self):
        """
        Actualizamos las reservas del salón seleccionado.
        """
        salon = self.salon_seleccionado
        if salon:
            print(f"Actualizando reservas para el salón: {salon}")
            self.mostrar_reservas_en_tabla(salon)

    def insertar_reserva_en_tabla(self, fila, reserva):
        """
        Inserta una reserva en la tabla en la fila dada.
        """
        datos_mostrar = [
            reserva[0],  # id_reserva
            reserva[1],  # fecha
            reserva[2],  # nombre_cliente
            reserva[3],  # telefono_cliente
            self.obtener_tipo_reserva(reserva[4]),  # tipo_reserva
        ]

        for columna, valor in enumerate(datos_mostrar):
            item = QTableWidgetItem(str(valor))
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.asg_tablaWidget.setItem(fila, columna, item)

    def mostrar_reservas_en_tabla(self, salon):
        """
        Mostramos las reservas en la tabla para el salón seleccionado.
        """
        reservas = self.obtener_reservas(salon)

        if not reservas:
            print("No hay reservas para este salón.")
            return

        self.asg_tablaWidget.setRowCount(0)

        for fila, reserva in enumerate(reservas):
            datos_mostrar = (reserva[0], reserva[1], reserva[2], reserva[3], reserva[4])

            self.asg_tablaWidget.insertRow(fila)
            self.insertar_reserva_en_tabla(fila, datos_mostrar)

        self.asg_tablaWidget.resizeRowsToContents()
        self.asg_tablaWidget.resizeColumnsToContents()

    def abrir_ventana_reservar(self):
        """
        Abrimos la ventana para realizar una nueva reserva.
        """
        if not self.salon_seleccionado:
            QMessageBox.warning(
                self, "Advertencia", "Por favor, seleccione un salón antes de reservar."
            )
            return

        self.reserva_seleccionada = None
        self.ventana_reservar.configurar_salon(self.salon_seleccionado)
        self.ventana_reservar.limpiar_campos()
        self.ventana_reservar.show()
        self.asg_edit_reserva.setVisible(False)
        self.asg_consultar.setVisible(False)
        self.asg_eliminar.setVisible(False)
        self.ventana_reservar.asg_finalizar.clicked.connect(
            self.ventana_reservar.guardar_reserva()
        )

    def abrir_ventana_editar(self):
        """
        Abrimos la ventana para editar una reserva existente.
        """
        if not self.verificar_salon_y_reserva():
            return

        self.ventana_reservar.configurar_salon(self.salon_seleccionado)
        self.ventana_reservar.cargar_reserva(self.reserva_seleccionada)
        self.ventana_reservar.show()
        self.asg_edit_reserva.setVisible(False)
        self.asg_consultar.setVisible(False)
        self.asg_eliminar.setVisible(False)

        self.ventana_reservar.asg_finalizar.clicked.connect(
            self.ventana_reservar.actualizar_reserva
        )

    def verificar_salon_y_reserva(self):
        """
        Verifica si se ha seleccionado un salón y una reserva.
        """
        if not self.salon_seleccionado:
            QMessageBox.warning(
                self, "Advertencia", "Por favor, seleccione un salón antes de proceder."
            )
            return False
        if not self.reserva_seleccionada:
            QMessageBox.warning(
                self, "Advertencia", "Por favor, seleccione una reserva para proceder."
            )
            return False
        return True

    def abrir_consulta(self):
        """
        Muestra toda la información de la reserva seleccionada en un QMessageBox.
        Cada parámetro aparece en una línea distinta.
        """
        if not self.verificar_salon_y_reserva():
            return

        id_Reserva = self.reserva_seleccionada[0]
        fecha = self.reserva_seleccionada[1]
        nombre_cliente = self.reserva_seleccionada[2]
        telefono_cliente = self.reserva_seleccionada[3]
        id_cliente = self.reserva_seleccionada[4]
        tipo_reserva_nombre = self.obtener_tipo_reserva(self.reserva_seleccionada[5])
        ocupacion = self.reserva_seleccionada[6]
        jornadas = self.reserva_seleccionada[7]
        tipo_cocina = self.obtener_tipo_cocina(self.reserva_seleccionada[8])
        habitaciones = "Sí" if self.reserva_seleccionada[9] else "No"
        salon_id = self.reserva_seleccionada[10]
        num_id = self.reserva_seleccionada[11]

        salon = self.obtener_nombre_salon(salon_id)
        mensaje = (
            f"👤 ID Reserva: {id_Reserva}\n"
            f"📅 Fecha: {fecha}\n"
            f"🏷️ Tipo de Reserva: {tipo_reserva_nombre}\n"
            f"🏠 Salón: {salon}\n"
            f"🔥 Tipo de Cocina: {tipo_cocina}\n"
            f"👤 ID Cliente: {id_cliente}\n"
            f"👤 Cliente: {nombre_cliente}\n"
            f"📞 Teléfono: {telefono_cliente}\n"
            f"👥 Ocupación: {ocupacion} personas\n"
            f"⏳ Jornadas: {jornadas}\n"
            f"🏨 Habitaciones: {habitaciones}\n"
            f"🔑 Número de Identificación: {num_id}\n"
        )

        QMessageBox.information(self, "Detalles de la Reserva", mensaje)

    def eliminar_reserva(self):
        """
        Elimina la reserva seleccionada tras confirmación del usuario.
        """
        if not self.verificar_salon_y_reserva():
            return

        confirmacion = QMessageBox.question(
            self,
            "Eliminar Reserva",
            "¿Estás seguro de que deseas eliminar esta reserva?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if confirmacion == QMessageBox.No:
            return

        reserva_id = self.reserva_seleccionada[0]

        consulta = "DELETE FROM reservas WHERE reserva_id = ?"
        resultado = self.bd.Consulta(consulta, (reserva_id,))

        if resultado == "Error":
            QMessageBox.critical(self, "Error", "No se pudo eliminar la reserva.")
        else:
            QMessageBox.information(self, "Éxito", "Reserva eliminada correctamente.")
            self.actualizar_reservas()
