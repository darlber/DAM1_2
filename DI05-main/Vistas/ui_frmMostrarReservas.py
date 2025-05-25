# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmMostrarReservasVcalFK.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)
from Recursos.img import bg_rc

class Ui_MostrarReservas(object):
    def setupUi(self, MostrarReservas):
        if not MostrarReservas.objectName():
            MostrarReservas.setObjectName(u"MostrarReservas")
        MostrarReservas.setWindowModality(Qt.WindowModality.WindowModal)
        MostrarReservas.resize(795, 601)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MostrarReservas.sizePolicy().hasHeightForWidth())
        MostrarReservas.setSizePolicy(sizePolicy)
        MostrarReservas.setMinimumSize(QSize(0, 0))
        MostrarReservas.setMaximumSize(QSize(5000, 659))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        MostrarReservas.setFont(font)
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/brianda1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MostrarReservas.setWindowIcon(icon)
        MostrarReservas.setStyleSheet(u"/* Estilo general para la ventana */\n"
"QWidget {\n"
"	background-color: rgba(38, 45, 67, 100);\n"
"    color: #E0E0E0; /* Texto claro */\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"/* Estilo para el QListWidget */\n"
"QListWidget {\n"
"    background-color: #34495E; /* Fondo oscuro */\n"
"    border: 1px solid #555555;\n"
"    border-radius: 5px;\n"
"    color: #E0E0E0; /* Texto claro */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo para el QTableWidget */\n"
"QTableWidget {\n"
"    background-color: #34495E; /* Fondo oscuro */\n"
"    border: 1px solid #555555;\n"
"    border-radius: 5px;\n"
"    gridline-color: #555555; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"    color: #E0E0E0; /* Texto claro */\n"
"}\n"
"\n"
"\n"
"QTableWidget::item {\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"\n"
"/* Estilo para los botones */\n"
"QPushButton {\n"
"    background-color: #2C3E50; /* Fondo oscuro */\n"
"    color: #E0E0E0; /* Texto claro */\n"
"    border: 1"
                        "px solid #555555;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #34495E; /* Fondo m\u00e1s claro al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1C2A36; /* Fondo m\u00e1s oscuro al presionar */\n"
"}\n"
"\n"
"\n"
"/* Estilo para el men\u00fa */\n"
"QMenuBar {\n"
"    background-color: #2C3E50; /* Fondo oscuro */\n"
"    color: #E0E0E0; /* Texto claro */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #34495E; /* Fondo para elementos seleccionados */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #2C3E50; /* Fondo oscuro */\n"
"    color: #E0E0E0; /* Texto claro */\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #34495E; /* Fondo para elementos seleccionados */\n"
"}")
        self.centralwidget = QWidget(MostrarReservas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.asg_botonReservar = QPushButton(self.centralwidget)
        self.asg_botonReservar.setObjectName(u"asg_botonReservar")
        self.asg_botonReservar.setGeometry(QRect(460, 490, 271, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.asg_botonReservar.setFont(font1)
        self.asg_botonReservar.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 500, 351, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.asg_edit_reserva = QPushButton(self.horizontalLayoutWidget)
        self.asg_edit_reserva.setObjectName(u"asg_edit_reserva")
        self.asg_edit_reserva.setFont(font1)
        self.asg_edit_reserva.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.asg_edit_reserva)

        self.asg_consultar = QPushButton(self.horizontalLayoutWidget)
        self.asg_consultar.setObjectName(u"asg_consultar")
        self.asg_consultar.setFont(font1)
        self.asg_consultar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.asg_consultar)

        self.asg_eliminar = QPushButton(self.horizontalLayoutWidget)
        self.asg_eliminar.setObjectName(u"asg_eliminar")
        self.asg_eliminar.setFont(font1)
        self.asg_eliminar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.asg_eliminar)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(50, 30, 681, 451))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.asg_listaWidget = QListWidget(self.horizontalLayoutWidget_2)
        self.asg_listaWidget.setObjectName(u"asg_listaWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.asg_listaWidget.sizePolicy().hasHeightForWidth())
        self.asg_listaWidget.setSizePolicy(sizePolicy1)
        self.asg_listaWidget.setMinimumSize(QSize(104, 400))
        self.asg_listaWidget.setMaximumSize(QSize(156, 492))
        self.asg_listaWidget.setStyleSheet(u"    background-color: #2C3E50; /* Fondo oscuro */")
        self.asg_listaWidget.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.asg_listaWidget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.asg_tablaWidget = QTableWidget(self.horizontalLayoutWidget_2)
        if (self.asg_tablaWidget.columnCount() < 5):
            self.asg_tablaWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.asg_tablaWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.asg_tablaWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.asg_tablaWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.asg_tablaWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.asg_tablaWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.asg_tablaWidget.setObjectName(u"asg_tablaWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(190)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.asg_tablaWidget.sizePolicy().hasHeightForWidth())
        self.asg_tablaWidget.setSizePolicy(sizePolicy2)
        self.asg_tablaWidget.setMaximumSize(QSize(554, 492))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.asg_tablaWidget.setFont(font2)
        self.asg_tablaWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.asg_tablaWidget.setAutoFillBackground(False)
        self.asg_tablaWidget.setStyleSheet(u"QWidget {\n"
"    background-color: #2C3E50; /* Fondo oscuro */\n"
"\n"
"}\n"
"    QHeaderView::section {\n"
"        background-color:  rgb(20, 24, 36);\n"
"    }")
        self.asg_tablaWidget.setAutoScroll(True)
        self.asg_tablaWidget.setAlternatingRowColors(True)
        self.asg_tablaWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.asg_tablaWidget.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.asg_tablaWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.asg_tablaWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.asg_tablaWidget.setGridStyle(Qt.PenStyle.NoPen)
        self.asg_tablaWidget.setRowCount(0)
        self.asg_tablaWidget.setColumnCount(5)
        self.asg_tablaWidget.horizontalHeader().setMinimumSectionSize(32)
        self.asg_tablaWidget.horizontalHeader().setDefaultSectionSize(122)

        self.horizontalLayout_2.addWidget(self.asg_tablaWidget)

        MostrarReservas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MostrarReservas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 27))
        MostrarReservas.setMenuBar(self.menubar)

        self.retranslateUi(MostrarReservas)

        QMetaObject.connectSlotsByName(MostrarReservas)
    # setupUi

    def retranslateUi(self, MostrarReservas):
        MostrarReservas.setWindowTitle(QCoreApplication.translate("MostrarReservas", u"Mostrar Reservas", None))
#if QT_CONFIG(tooltip)
        self.asg_botonReservar.setToolTip(QCoreApplication.translate("MostrarReservas", u"Acceder a la pantalla de Reservas", None))
#endif // QT_CONFIG(tooltip)
        self.asg_botonReservar.setText(QCoreApplication.translate("MostrarReservas", u"Reservar", None))
#if QT_CONFIG(tooltip)
        self.asg_edit_reserva.setToolTip(QCoreApplication.translate("MostrarReservas", u"Acceder a la pantalla de Reservas para editar", None))
#endif // QT_CONFIG(tooltip)
        self.asg_edit_reserva.setText(QCoreApplication.translate("MostrarReservas", u"Editar", None))
#if QT_CONFIG(tooltip)
        self.asg_consultar.setToolTip(QCoreApplication.translate("MostrarReservas", u"Acceder a la pantalla de Reservas para editar", None))
#endif // QT_CONFIG(tooltip)
        self.asg_consultar.setText(QCoreApplication.translate("MostrarReservas", u"Consultar", None))
#if QT_CONFIG(tooltip)
        self.asg_eliminar.setToolTip(QCoreApplication.translate("MostrarReservas", u"Acceder a la pantalla de Reservas para editar", None))
#endif // QT_CONFIG(tooltip)
        self.asg_eliminar.setText(QCoreApplication.translate("MostrarReservas", u"Eliminar", None))
        ___qtablewidgetitem = self.asg_tablaWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MostrarReservas", u"idReserva", None));
        ___qtablewidgetitem1 = self.asg_tablaWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MostrarReservas", u"Fecha", None));
        ___qtablewidgetitem2 = self.asg_tablaWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MostrarReservas", u"Persona", None));
        ___qtablewidgetitem3 = self.asg_tablaWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MostrarReservas", u"Tel\u00e9fono", None));
        ___qtablewidgetitem4 = self.asg_tablaWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MostrarReservas", u"Tipo de Reserva", None));
    # retranslateUi

