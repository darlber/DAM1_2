# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenuSMvWCz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QWidget,
)
from Recursos.img import bg_rc


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName("MainMenu")
        MainMenu.setWindowModality(Qt.WindowModality.WindowModal)
        MainMenu.setEnabled(True)
        MainMenu.resize(645, 459)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenu.sizePolicy().hasHeightForWidth())
        MainMenu.setSizePolicy(sizePolicy)
        MainMenu.setMinimumSize(QSize(645, 459))
        MainMenu.setMaximumSize(QSize(645, 459))
        font = QFont()
        font.setFamilies(["Arial"])
        font.setBold(False)
        MainMenu.setFont(font)
        icon = QIcon()
        icon.addFile(
            ":/prefijoNuevo/brianda1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        MainMenu.setWindowIcon(icon)
        MainMenu.setStyleSheet(
            "QWidget {\n"
            "\n"
            "    color: #ECF0F1; /* Texto claro en el fondo */\n"
            "    font-family: 'Arial', sans-serif;\n"
            "    font-size: 14px;\n"
            "}\n"
            "QLabel#aplicacioneslabel, QLabel#ayudalabel{\n"
            "    font-family: 'Arial', sans-serif;\n"
            "    font-size: 24px; /* T\u00edtulo grande */\n"
            "    font-weight: bold; /* Negrita */\n"
            "    color: black; /* Color oscuro para contraste */\n"
            "    background-color: rgba(38, 45, 67, 0.3);\n"
            "    padding: 10px 0; /* Espaciado superior e inferior */\n"
            "    border: none; /* Sin borde */\n"
            "    text-align: center; /* Centrado */\n"
            "    margin-bottom: 20px; /* Espacio debajo del t\u00edtulo */\n"
            "    border-bottom: 3px solid grey; /* Subrayado azul */\n"
            "}\n"
            "\n"
            "QLabel#aplicacioneslabel:hover {\n"
            "    color: #1F8CD0; /* Cambio de color al pasar el rat\u00f3n (Azul) */\n"
            "}\n"
            "\n"
            "QLabel#aplicacioneslabel:focus {\n"
            "    outline: none; /* Elimina el contorno de foco */\n"
            "}\n"
            "QLabel#ayudalabel:hover {\n"
            "    color: #1F8CD0; /* Cambio de color al pasar el rat\u00f3"
            "n (Azul) */\n"
            "}\n"
            "\n"
            "QLabel#ayudalabel:focus {\n"
            "    outline: none; /* Elimina el contorno de foco */\n"
            "}\n"
            "\n"
            "QWidget#gridLayoutWidget {\n"
            "    background-color: rgba(41, 41, 61, 0.5); /* Color de fondo del panel m\u00e1s oscuro */\n"
            "    border-radius: 15px;\n"
            "    border: 2px solid #5D6D7E;\n"
            "    padding: 20px;\n"
            "}\n"
            "\n"
            "QLabel#fondo{\n"
            "    border-image: url(:/prefijoNuevo/DEFE8680-0B24-D610-0C1517DF084837B4.JPG);\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #3498DB; /* Azul brillante */\n"
            "    color: #000000; /* Texto en negro */\n"
            "    border-radius: 12px;\n"
            "    padding: 12px 25px;\n"
            "    font-size: 16px;\n"
            "    font-weight: bold;\n"
            "    min-width: 120px;\n"
            "    min-height: 45px;\n"
            "    margin: 10px;\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #1F8CD0; /* Azul m\u00e1s oscuro */\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #2980B9; /* Azul a\u00fan m\u00e1s oscuro */\n"
            "    fon"
            "t-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "/* Estilos espec\u00edficos para cada bot\u00f3n con hover y pressed */\n"
            "QPushButton#buttonReservar {\n"
            "    background-color: #1ABC9C; /* Verde-agua */\n"
            "}\n"
            "\n"
            "QPushButton#buttonReservar:hover {\n"
            "    background-color: #16A085; /* Verde-agua m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonReservar:pressed {\n"
            "    background-color: #138D6F; /* Verde-agua a\u00fan m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonClientes {\n"
            "    background-color: #27AE60; /* Verde */\n"
            "}\n"
            "\n"
            "QPushButton#buttonClientes:hover {\n"
            "    background-color: #219150; /* Verde m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonClientes:pressed {\n"
            "    background-color: #1C7A4D; /* Verde a\u00fan m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAplicaciones {\n"
            "    background-color: #ac3939; /* Rojo */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAplicaciones:hover {\n"
            "    background-color: #8B2E2E; /* Rojo m\u00e1s oscu"
            "ro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAplicaciones:pressed {\n"
            "    background-color: #732525; /* Rojo a\u00fan m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAyuda {\n"
            "    background-color: #F39C12; /* Naranja */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAyuda:hover {\n"
            "    background-color: #D68910; /* Naranja m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAyuda:pressed {\n"
            "    background-color: #B9770E; /* Naranja a\u00fan m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAcerca {\n"
            "    background-color: #9B59B6; /* P\u00farpura */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAcerca:hover {\n"
            "    background-color: #8E44AD; /* P\u00farpura m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonAcerca:pressed {\n"
            "    background-color: #7D3C98; /* P\u00farpura a\u00fan m\u00e1s oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonDocumentacion {\n"
            "    background-color: #E67E22; /* Naranja oscuro */\n"
            "}\n"
            "\n"
            "QPushButton#buttonDocumentacion:hover {\n"
            "    background-color: #D35400; /* Naranja oscuro m\u00e1s os"
            "curo */\n"
            "}\n"
            "\n"
            "QPushButton#buttonDocumentacion:pressed {\n"
            "    background-color: #BA4A00; /* Naranja oscuro a\u00fan m\u00e1s oscuro */\n"
            "}"
        )
        MainMenu.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget_1 = QWidget(MainMenu)
        self.centralwidget_1.setObjectName("centralwidget_1")
        self.gridLayoutWidget = QWidget(self.centralwidget_1)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 150, 611, 281))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttonClientes = QPushButton(self.gridLayoutWidget)
        self.buttonClientes.setObjectName("buttonClientes")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.buttonClientes.sizePolicy().hasHeightForWidth()
        )
        self.buttonClientes.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.buttonClientes, 1, 0, 1, 1)

        self.buttonReservar = QPushButton(self.gridLayoutWidget)
        self.buttonReservar.setObjectName("buttonReservar")
        sizePolicy1.setHeightForWidth(
            self.buttonReservar.sizePolicy().hasHeightForWidth()
        )
        self.buttonReservar.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.buttonReservar, 0, 0, 1, 1)

        self.buttonAcerca = QPushButton(self.gridLayoutWidget)
        self.buttonAcerca.setObjectName("buttonAcerca")
        sizePolicy1.setHeightForWidth(
            self.buttonAcerca.sizePolicy().hasHeightForWidth()
        )
        self.buttonAcerca.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.buttonAcerca, 0, 1, 1, 1)

        self.buttonDocumentacion = QPushButton(self.gridLayoutWidget)
        self.buttonDocumentacion.setObjectName("buttonDocumentacion")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.buttonDocumentacion.sizePolicy().hasHeightForWidth()
        )
        self.buttonDocumentacion.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.buttonDocumentacion, 1, 1, 1, 1)

        self.fondo = QLabel(self.centralwidget_1)
        self.fondo.setObjectName("fondo")
        self.fondo.setGeometry(QRect(-20, 0, 681, 471))
        self.horizontalLayoutWidget = QWidget(self.centralwidget_1)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 20, 591, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.aplicacioneslabel = QLabel(self.horizontalLayoutWidget)
        self.aplicacioneslabel.setObjectName("aplicacioneslabel")
        self.aplicacioneslabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.aplicacioneslabel)

        self.ayudalabel = QLabel(self.horizontalLayoutWidget)
        self.ayudalabel.setObjectName("ayudalabel")
        self.ayudalabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ayudalabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.ayudalabel)

        MainMenu.setCentralWidget(self.centralwidget_1)
        self.fondo.raise_()
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainMenu)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 645, 33))
        MainMenu.setMenuBar(self.menubar)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)

    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(
            QCoreApplication.translate("MainMenu", "MainWindow", None)
        )
        # if QT_CONFIG(tooltip)
        self.buttonClientes.setToolTip(
            QCoreApplication.translate(
                "MainMenu", "Abre ventana para gestionar Clientes", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.buttonClientes.setText(
            QCoreApplication.translate("MainMenu", "Clientes", None)
        )
        # if QT_CONFIG(tooltip)
        self.buttonReservar.setToolTip(
            QCoreApplication.translate(
                "MainMenu", "Abre ventana para gestionar las reservas", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.buttonReservar.setText(
            QCoreApplication.translate("MainMenu", "Reservar", None)
        )
        # if QT_CONFIG(tooltip)
        self.buttonAcerca.setToolTip(
            QCoreApplication.translate("MainMenu", "Acerca de la aplicaci\u00f3n", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.buttonAcerca.setText(
            QCoreApplication.translate("MainMenu", "Acerca", None)
        )
        # if QT_CONFIG(tooltip)
        self.buttonDocumentacion.setToolTip(
            QCoreApplication.translate("MainMenu", "Leer documentaci\u00f3n", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.buttonDocumentacion.setText(
            QCoreApplication.translate("MainMenu", "Documentaci\u00f3n", None)
        )
        self.fondo.setText("")
        self.aplicacioneslabel.setText(
            QCoreApplication.translate("MainMenu", "Aplicaciones", None)
        )
        self.ayudalabel.setText(QCoreApplication.translate("MainMenu", "Ayuda", None))

    # retranslateUi
