from PySide6.QtWidgets import QMainWindow, QDialog
from Control.clientes import Clientes
from Control.mostrar_reservas import MostrarReservas
from Vistas.ui_mainMenu import Ui_MainMenu
from Vistas.ui_acerca import Ui_Acerca
from Vistas.ui_docu import Ui_Documentacion


class mainMenu(QMainWindow, Ui_MainMenu):
    """
    Clase para gestionar el menú principal de la aplicación.
    """

    def __init__(self, bd):
        """
        Inicializamos la clase y configuramos la interfaz de usuario.
        """
        super().__init__()
        self.bd = bd

        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        self.ui.buttonClientes.clicked.connect(self.abrir_ventana_clientes)
        self.ui.buttonAcerca.clicked.connect(self.abrir_ventana_acerca_de)
        self.ui.buttonDocumentacion.clicked.connect(self.abrir_ventana_documentacion)
        self.ui.buttonReservar.clicked.connect(self.abrir_ventana_reservar)

    def abrir_ventana_clientes(self):
        """
        Abrimos la ventana de gestión de clientes.
        """
        self.clientes = Clientes(self.bd)  # Crea una nueva instancia de Clientes
        self.clientes.show()

    def abrir_ventana_acerca_de(self):
        """
        Abrimos la ventana de información "Acerca de".
        """
        self.acerca_dialog = QDialog(self)
        self.ui_acerca = Ui_Acerca()
        self.ui_acerca.setupUi(self.acerca_dialog)
        self.acerca_dialog.show()

    def abrir_ventana_documentacion(self):
        """
        Abrimos la ventana de documentación.
        """
        self.docum_dialog = QDialog(self)
        self.docum = Ui_Documentacion()
        self.docum.setupUi(self.docum_dialog)
        self.docum_dialog.show()

    def abrir_ventana_reservar(self):
        """
        Abrimos la ventana para realizar una nueva reserva.
        """
        self.reservar = MostrarReservas(self.bd)
        self.reservar.show()
