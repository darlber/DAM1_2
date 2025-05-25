# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'docuaNyIWl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QScrollArea,
    QSizePolicy, QWidget)
from Recursos.img import bg_rc

class Ui_Documentacion(object):
    def setupUi(self, Documentacion):
        if not Documentacion.objectName():
            Documentacion.setObjectName(u"Documentacion")
        Documentacion.setWindowModality(Qt.WindowModality.WindowModal)
        Documentacion.resize(774, 379)
        Documentacion.setMinimumSize(QSize(774, 379))
        Documentacion.setMaximumSize(QSize(774, 379))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/brianda1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Documentacion.setWindowIcon(icon)
        Documentacion.setStyleSheet(u"    QDialog {\n"
"        background-color: #1E1E2F;\n"
"        color: #F4F4F4;\n"
"        font-family: 'Arial', sans-serif;\n"
"        font-size: 14px;\n"
"    }\n"
"\n"
"")
        self.scrollArea = QScrollArea(Documentacion)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 30, 731, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 717, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -120, 711, 1000))
        self.label.setMinimumSize(QSize(0, 1000))
        self.label.setWordWrap(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Documentacion)

        QMetaObject.connectSlotsByName(Documentacion)
    # setupUi

    def retranslateUi(self, Documentacion):
        Documentacion.setWindowTitle(QCoreApplication.translate("Documentacion", u"Documentaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Documentacion", u"<h2>Documentaci\u00f3n de la Aplicaci\u00f3n</h2>\n"
"\n"
"<h3>Resumen:</h3>\n"
"<p>Esta aplicaci\u00f3n est\u00e1 dise\u00f1ada para gestionar las reservas de un hotel. Permite a los usuarios interactuar con una base de datos para realizar las siguientes operaciones:</p>\n"
"<ul>\n"
"  <li><strong>Autenticaci\u00f3n</strong>: Acceso mediante nombre de usuario y contrase\u00f1a, validada contra la base de datos.</li>\n"
"  <li><strong>Gesti\u00f3n de Clientes</strong>: Permite crear, leer, actualizar y eliminar registros de clientes en la base de datos.</li>\n"
"  <li><strong>Reservas</strong>: Realizaci\u00f3n de reservas, mostrando informaci\u00f3n detallada y permitiendo modificaciones, consultas y eliminaciones de reservas existentes.</li>\n"
"  <li><strong>Interfaz de Usuario</strong>: La aplicaci\u00f3n presenta una interfaz gr\u00e1fica atractiva y f\u00e1cil de usar, desarrollada con la biblioteca PySide6 y dise\u00f1ada con QT Designer.</li>\n"
"</ul>\n"
"\n"
"<h3>Funciones Principales:</h3>\n"
"<ol>\n"
""
                        "  <li><strong>Pantalla de Autenticaci\u00f3n:</strong> Al iniciar la aplicaci\u00f3n, el usuario debe ingresar su nombre de usuario y contrase\u00f1a para acceder. La autenticaci\u00f3n se realiza validando los datos contra la tabla de usuarios en la base de datos SQLite.</li>\n"
"  <li><strong>Gesti\u00f3n de Clientes:</strong> Permite al administrador gestionar los registros de los clientes, agregando nuevos clientes, consultando la informaci\u00f3n existente, y realizando actualizaciones o eliminaciones. Los campos disponibles incluyen nombre, direcci\u00f3n, tel\u00e9fono y correo electr\u00f3nico.</li>\n"
"  <li><strong>Gesti\u00f3n de Reservas:</strong> Permite a los usuarios realizar nuevas reservas, consultar reservas existentes, modificar detalles o eliminarlas. Al crear una reserva, se solicita informaci\u00f3n del cliente, n\u00famero de personas y fechas. El sistema muestra los detalles de las reservas, incluyendo el nombre del cliente y tel\u00e9fono, los cuales se obtienen de la tabla de clientes"
                        " en la base de datos.</li>\n"
"  <li><strong>Pantalla \"Acerca de\":</strong> Esta ventana proporciona informaci\u00f3n sobre los desarrolladores de la aplicaci\u00f3n y el prop\u00f3sito general del proyecto.</li>\n"
"  <li><strong>Pantalla de Documentaci\u00f3n:</strong> Explica el funcionamiento general de la aplicaci\u00f3n y proporciona detalles sobre las distintas funcionalidades disponibles.</li>\n"
"</ol>\n"
"\n"
"<h3>Tecnolog\u00edas Utilizadas:</h3>\n"
"<ul>\n"
"  <li><strong>Lenguaje de Programaci\u00f3n</strong>: Python 3.x</li>\n"
"  <li><strong>Librer\u00eda Gr\u00e1fica</strong>: PySide6 (basada en Qt6)</li>\n"
"  <li><strong>Modelo de Dise\u00f1o</strong>: Modelo Vista Controlador (MVC)</li>\n"
"  <li><strong>Base de Datos</strong>: SQLite</li>\n"
"  <li><strong>Dise\u00f1o de la Interfaz</strong>: QT Designer</li>\n"
"</ul>\n"
"\n"
"<h3>Consideraciones de Dise\u00f1o:</h3>\n"
"<ul>\n"
"  <li>La interfaz est\u00e1 dise\u00f1ada para ser intuitiva y f\u00e1cil de usar, con un esquema de colores "
                        "atractivo y una estructura que facilita la navegaci\u00f3n.</li>\n"
"  <li>Los botones y otros elementos interactivos cuentan con <em>tooltips</em> para facilitar la comprensi\u00f3n de su funci\u00f3n.</li>\n"
"  <li>La aplicaci\u00f3n es completamente funcional y modular, permitiendo una f\u00e1cil expansi\u00f3n en el futuro si fuera necesario.</li>\n"
"</ul>\n"
"", None))
    # retranslateUi

