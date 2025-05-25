import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QToolTip

from Control.basedatos import BD
from Control.mainMenu import mainMenu
from Vistas.ui_login import Ui_asg_login


class Login(QMainWindow, Ui_asg_login):
    """
    Clase Login que maneja la interfaz de inicio de sesión.
    Hereda de QMainWindow y Ui_asg_login.
    Métodos:
    --------
    __init__():
        Constructor de la clase. Inicializa la interfaz y conecta las señales.
    show_tooltip(message, color):
        Muestra un tooltip con un mensaje y color especificado.
    login_action():
        Acción que se ejecuta al intentar iniciar sesión. Valida las credenciales y muestra el menú principal si son correctas.
    validar_credenciales(usuario, usuario_password):
        Valida las credenciales del usuario consultando la base de datos.
    mainMenu():
        Muestra el menú principal si las credenciales son correctas.
    """
    
    def __init__(self):
        """
        Constructor de la clase. Inicializa la interfaz de inicio de sesión, conecta las señales y
        coloca las credenciales predeterminadas.
        """
        super().__init__()

        self.ui = Ui_asg_login()
        self.ui.setupUi(self)

        # username 'admin' pass 'admin'
        self.bd = BD()
        self.bd.CrearConexion()

        self.ui.usuarioEdit.setText("admin")
        self.ui.passEdit.setText("admin")

        self.ui.asg_pushButton.clicked.connect(self.login_action)
        self.ui.passEdit.returnPressed.connect(self.ui.asg_pushButton.click)
        self.ui.actionSalir.triggered.connect(self.close)

    def show_tooltip(self, message, color):
        """
        Muestra un tooltip con el mensaje y color especificados.

        Parámetros:
        -----------
        message : str
            El mensaje a mostrar en el tooltip.
        color : str
            El color del texto que se mostrará en el tooltip.
        """
        QToolTip.setFont(self.ui.asg_pushButton.font())
        self.ui.asg_pushButton.setStyleSheet(f"color: {color};")
        QToolTip.showText(
            self.ui.asg_pushButton.mapToGlobal(self.ui.asg_pushButton.rect().center()),
            message,
        )

    def login_action(self):
        """
        Intenta iniciar sesión con las credenciales proporcionadas. Si las credenciales
        son correctas, muestra el menú principal; de lo contrario, muestra un tooltip con
        un mensaje de acceso denegado y borra las credenciales actualmente ingresadas.
        """
        user = self.ui.usuarioEdit.text()
        password = self.ui.passEdit.text()

        if self.validar_credenciales(user, password):
            self.mainMenu()

        else:
            self.show_tooltip("Acceso denegado", "red")
            self.ui.usuarioEdit.clear()
            self.ui.passEdit.clear()

    def validar_credenciales(self, usuario, usuario_password):
        """
        Valida las credenciales del usuario consultando la base de datos.

        Parámetros:
        -----------
        usuario : str
            El nombre de usuario a validar.
        usuario_password : str
            La contraseña a validar.

        Returns:
        -------
        bool
            True si las credenciales son correctas, False de lo contrario.
        """

        query = "SELECT password FROM usuarios WHERE username = ?"
        resultado = self.bd.Consulta(query, (usuario,))

        if resultado:
            db_password = resultado[0][0]
            if usuario_password == db_password:
                return True
        return False

    def mainMenu(self):
        """
        Abre la ventana principal del menú si las credenciales son correctas.

        Muestra la ventana principal del menú y oculta la actual.
        """
        
        self.hide()
        self.ui = mainMenu(self.bd)
        self.ui.show()
        
def main():
    app = QApplication(sys.argv)
    main_window = Login()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()