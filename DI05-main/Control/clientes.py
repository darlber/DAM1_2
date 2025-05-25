import datetime
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QAbstractItemView, QMessageBox, QTableWidgetItem, QWidget

from Vistas.ui_clientes import Ui_tablaClientes


class Clientes(QWidget, Ui_tablaClientes):

    def __init__(self, bd):
        """
        Inicializamos la clase y configuramos la interfaz de usuario.
        """
        super().__init__()
        self.bd = bd

        self.ui = Ui_tablaClientes()
        self.ui.setupUi(self)

        self.load_data()

        self.ui.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.botonLeer.clicked.connect(self.load_selected_row)
        self.ui.BotonUpdate.clicked.connect(self.update_selected_row)
        self.ui.botonCrear.clicked.connect(self.create_new_row)
        self.ui.botonBorrar.clicked.connect(self.delete_selected_row)

    def load_data(self):
        """
        Cargamos los datos de los clientes en la tabla.
        """
        consulta = """SELECT * FROM clientes"""
        query = self.bd.Consulta(consulta)

        if not query:
            return []

        self.ui.tabla.setRowCount(len(query))
        for row_idx, row_data in enumerate(query):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.ui.tabla.setItem(row_idx, col_idx, item)

        self.ui.tabla.resizeRowsToContents()
        self.ui.tabla.resizeColumnsToContents()

    def load_selected_row(self):
        """
        Cargamos los datos de la fila seleccionada en los campos de entrada.
        """
        selected_row = self.ui.tabla.currentRow()

        if selected_row < 0:
            return  # No hay fila seleccionada

        self.ui.lineEdit_id.setText(self.ui.tabla.item(selected_row, 0).text())
        self.ui.lineEdit_nombre.setText(self.ui.tabla.item(selected_row, 1).text())
        self.ui.lineEdit_apellidos.setText(self.ui.tabla.item(selected_row, 2).text())
        self.ui.lineEdit_numId.setText(self.ui.tabla.item(selected_row, 3).text())

        # Obtener la fecha de la tabla y establecerla en el QDateEdit
        fecha_texto = self.ui.tabla.item(selected_row, 4).text()
        fecha = QDate.fromString(fecha_texto, "dd/MM/yyyy")
        self.ui.date_fechaNac.setDate(fecha)

        self.ui.lineEdit_pais.setText(self.ui.tabla.item(selected_row, 5).text())
        self.ui.lineEdit_telefon.setText(self.ui.tabla.item(selected_row, 6).text())
        self.ui.lineEdit_mail.setText(self.ui.tabla.item(selected_row, 7).text())
        self.ui.lineEdit_sexo.setText(self.ui.tabla.item(selected_row, 8).text())
        self.ui.lineEdit_menores.setText(self.ui.tabla.item(selected_row, 9).text())

    def update_selected_row(self):
        """
        Actualizamos los datos de la fila seleccionada.
        """
        id_cliente = self.ui.lineEdit_id.text()
        nombre = self.ui.lineEdit_nombre.text()
        apellidos = self.ui.lineEdit_apellidos.text()
        identificacion = self.ui.lineEdit_numId.text()

        # Obtener la fecha del QDateEdit
        fecha = self.ui.date_fechaNac.date().toString("dd/MM/yyyy")

        pais = self.ui.lineEdit_pais.text()
        telefono = self.ui.lineEdit_telefon.text()
        email = self.ui.lineEdit_mail.text()
        sexo = self.ui.lineEdit_sexo.text()
        menores = self.ui.lineEdit_menores.text()

        if not self.verify_date(fecha):
            QMessageBox.critical(self, "Error", "Fecha de nacimiento inválida")
            return

        consulta = """UPDATE clientes 
        SET Nombre = ?, Apellidos = ?, Num_Identificacion = ?, Fec_Nac = ?, 
            Pais = ?, Telefono = ?, email = ?, Sexo = ?, Menores = ?
        WHERE Id = ?"""
        valores = (
            nombre,
            apellidos,
            identificacion,
            fecha,
            pais,
            telefono,
            email,
            sexo,
            menores,
            id_cliente,
        )

        if self.bd.Consulta(consulta, valores):
            QMessageBox.information(
                self, "Actualización", "Registro actualizado con éxito"
            )
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el registro")
        self.load_data()
        self.clear_input_fields()

    def verify_date(self, date_text):
        """
        Verificamos si la fecha es válida.
        """
        try:
            datetime.datetime.strptime(date_text, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def create_new_row(self):
        """
        Creamos una nueva fila en la tabla de clientes.
        """
        nombre = self.ui.lineEdit_nombre.text()
        apellidos = self.ui.lineEdit_apellidos.text()
        identificacion = self.ui.lineEdit_numId.text()

        # Obtener la fecha del QDateEdit
        fecha = self.ui.date_fechaNac.date().toString("dd/MM/yyyy")

        pais = self.ui.lineEdit_pais.text()
        telefono = self.ui.lineEdit_telefon.text()
        email = self.ui.lineEdit_mail.text()
        sexo = self.ui.lineEdit_sexo.text()
        menores = self.ui.lineEdit_menores.text()

        if not self.verify_date(fecha):
            QMessageBox.critical(self, "Error", "Fecha de nacimiento inválida")
            return

        consulta = """INSERT INTO clientes 
                    (Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        valores = (
            nombre,
            apellidos,
            identificacion,
            fecha,
            pais,
            telefono,
            email,
            sexo,
            menores,
        )

        self.bd.Consulta(consulta, valores)
        self.load_data()
        self.clear_input_fields()

    def clear_input_fields(self):
        """
        Limpiamos todos los campos de entrada.
        """
        self.ui.lineEdit_id.clear()
        self.ui.lineEdit_nombre.clear()
        self.ui.lineEdit_apellidos.clear()
        self.ui.lineEdit_numId.clear()
        self.ui.date_fechaNac.setDate(
            QDate.currentDate()
        )  # Restablecer la fecha actual
        self.ui.lineEdit_pais.clear()
        self.ui.lineEdit_telefon.clear()
        self.ui.lineEdit_mail.clear()
        self.ui.lineEdit_sexo.clear()
        self.ui.lineEdit_menores.clear()

    def delete_selected_row(self):
        """
        Eliminamos la fila seleccionada de la tabla de clientes.
        """
        selected_row = self.ui.tabla.currentRow()

        if selected_row < 0:
            print("No hay fila seleccionada")
            return

        id_cliente = self.ui.tabla.item(selected_row, 0).text()

        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Estás seguro de que deseas eliminar este cliente?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirmacion == QMessageBox.Yes:
            consulta = "DELETE FROM clientes WHERE Id = ?"
            valores = (id_cliente,)
            self.bd.Consulta(consulta, valores)
            self.load_data()
            self.clear_input_fields()
