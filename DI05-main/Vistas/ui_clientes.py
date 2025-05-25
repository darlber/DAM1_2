# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteslXmjsn.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
from Recursos.img import bg_rc


class Ui_tablaClientes(object):
    def setupUi(self, tablaClientes):
        if not tablaClientes.objectName():
            tablaClientes.setObjectName(u"tablaClientes")
        tablaClientes.setWindowModality(Qt.WindowModality.WindowModal)
        tablaClientes.resize(1245, 589)
        tablaClientes.setMinimumSize(QSize(1245, 589))
        tablaClientes.setMaximumSize(QSize(1245, 589))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/brianda1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        tablaClientes.setWindowIcon(icon)
        tablaClientes.setStyleSheet(u"QWidget {\n"
"    background-color: #2C3E50; /* Fondo oscuro */\n"
"\n"
"}\n"
"")
        self.frameDeBotones = QFrame(tablaClientes)
        self.frameDeBotones.setObjectName(u"frameDeBotones")
        self.frameDeBotones.setGeometry(QRect(20, 10, 291, 551))
        self.frameDeBotones.setStyleSheet(u"\n"
"background-color: rgba(38, 45, 67, 100);\n"
"")
        self.frameDeBotones.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameDeBotones.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayoutWidget = QWidget(self.frameDeBotones)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 271, 291))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelId = QLabel(self.formLayoutWidget)
        self.labelId.setObjectName(u"labelId")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelId)

        self.lineEdit_id = QLineEdit(self.formLayoutWidget)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setEnabled(False)
        self.lineEdit_id.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_id)

        self.LabelNombre = QLabel(self.formLayoutWidget)
        self.LabelNombre.setObjectName(u"LabelNombre")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.LabelNombre)

        self.lineEdit_nombre = QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_nombre)

        self.LabelApell = QLabel(self.formLayoutWidget)
        self.LabelApell.setObjectName(u"LabelApell")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.LabelApell)

        self.lineEdit_apellidos = QLineEdit(self.formLayoutWidget)
        self.lineEdit_apellidos.setObjectName(u"lineEdit_apellidos")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_apellidos)

        self.LabelNumId = QLabel(self.formLayoutWidget)
        self.LabelNumId.setObjectName(u"LabelNumId")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.LabelNumId)

        self.lineEdit_numId = QLineEdit(self.formLayoutWidget)
        self.lineEdit_numId.setObjectName(u"lineEdit_numId")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_numId)

        self.labelFecha = QLabel(self.formLayoutWidget)
        self.labelFecha.setObjectName(u"labelFecha")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelFecha)

        self.labelPas = QLabel(self.formLayoutWidget)
        self.labelPas.setObjectName(u"labelPas")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelPas)

        self.lineEdit_pais = QLineEdit(self.formLayoutWidget)
        self.lineEdit_pais.setObjectName(u"lineEdit_pais")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_pais)

        self.labelTLF = QLabel(self.formLayoutWidget)
        self.labelTLF.setObjectName(u"labelTLF")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelTLF)

        self.lineEdit_telefon = QLineEdit(self.formLayoutWidget)
        self.lineEdit_telefon.setObjectName(u"lineEdit_telefon")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_telefon)

        self.labelMail = QLabel(self.formLayoutWidget)
        self.labelMail.setObjectName(u"labelMail")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.labelMail)

        self.lineEdit_mail = QLineEdit(self.formLayoutWidget)
        self.lineEdit_mail.setObjectName(u"lineEdit_mail")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_mail)

        self.labelSexo = QLabel(self.formLayoutWidget)
        self.labelSexo.setObjectName(u"labelSexo")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.labelSexo)

        self.lineEdit_sexo = QLineEdit(self.formLayoutWidget)
        self.lineEdit_sexo.setObjectName(u"lineEdit_sexo")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_sexo)

        self.labelMenores = QLabel(self.formLayoutWidget)
        self.labelMenores.setObjectName(u"labelMenores")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.labelMenores)

        self.lineEdit_menores = QLineEdit(self.formLayoutWidget)
        self.lineEdit_menores.setObjectName(u"lineEdit_menores")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_menores)

        self.date_fechaNac = QDateEdit(self.formLayoutWidget)
        self.date_fechaNac.setObjectName(u"date_fechaNac")
        self.date_fechaNac.setWrapping(False)
        self.date_fechaNac.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.date_fechaNac)

        self.gridLayoutWidget = QWidget(self.frameDeBotones)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 390, 271, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.botonLeer = QPushButton(self.gridLayoutWidget)
        self.botonLeer.setObjectName(u"botonLeer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botonLeer.sizePolicy().hasHeightForWidth())
        self.botonLeer.setSizePolicy(sizePolicy)
        self.botonLeer.setStyleSheet(u"background-color: #2C3E50")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/magnet.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonLeer.setIcon(icon1)
        self.botonLeer.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.botonLeer, 0, 1, 1, 1)

        self.botonCrear = QPushButton(self.gridLayoutWidget)
        self.botonCrear.setObjectName(u"botonCrear")
        sizePolicy.setHeightForWidth(self.botonCrear.sizePolicy().hasHeightForWidth())
        self.botonCrear.setSizePolicy(sizePolicy)
        self.botonCrear.setStyleSheet(u"background-color: #2C3E50")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/new.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonCrear.setIcon(icon2)
        self.botonCrear.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.botonCrear, 0, 0, 1, 1)

        self.BotonUpdate = QPushButton(self.gridLayoutWidget)
        self.BotonUpdate.setObjectName(u"BotonUpdate")
        sizePolicy.setHeightForWidth(self.BotonUpdate.sizePolicy().hasHeightForWidth())
        self.BotonUpdate.setSizePolicy(sizePolicy)
        self.BotonUpdate.setStyleSheet(u"background-color: #2C3E50")
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/cloud-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BotonUpdate.setIcon(icon3)
        self.BotonUpdate.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.BotonUpdate, 1, 0, 1, 1)

        self.botonBorrar = QPushButton(self.gridLayoutWidget)
        self.botonBorrar.setObjectName(u"botonBorrar")
        sizePolicy.setHeightForWidth(self.botonBorrar.sizePolicy().hasHeightForWidth())
        self.botonBorrar.setSizePolicy(sizePolicy)
        self.botonBorrar.setStyleSheet(u"background-color: #2C3E50")
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonBorrar.setIcon(icon4)
        self.botonBorrar.setIconSize(QSize(64, 64))

        self.gridLayout.addWidget(self.botonBorrar, 1, 1, 1, 1)

        self.framedeTabla = QFrame(tablaClientes)
        self.framedeTabla.setObjectName(u"framedeTabla")
        self.framedeTabla.setGeometry(QRect(320, 10, 911, 551))
        self.framedeTabla.setStyleSheet(u"background-color: rgb(38, 45, 67);")
        self.framedeTabla.setFrameShape(QFrame.Shape.StyledPanel)
        self.framedeTabla.setFrameShadow(QFrame.Shadow.Raised)
        self.tabla = QTableWidget(self.framedeTabla)
        if (self.tabla.columnCount() < 10):
            self.tabla.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(10, 10, 891, 531))
        self.tabla.setStyleSheet(u"QWidget {\n"
"    background-color: #2C3E50; /* Fondo oscuro */\n"
"\n"
"}\n"
"    QHeaderView::section {\n"
"        background-color:  rgb(20, 24, 36);\n"
"    }")
        self.tabla.setAlternatingRowColors(True)

        self.retranslateUi(tablaClientes)

        QMetaObject.connectSlotsByName(tablaClientes)
    # setupUi

    def retranslateUi(self, tablaClientes):
        tablaClientes.setWindowTitle(QCoreApplication.translate("tablaClientes", u"Clientes", None))
        self.labelId.setText(QCoreApplication.translate("tablaClientes", u"Id", None))
        self.LabelNombre.setText(QCoreApplication.translate("tablaClientes", u"Nombre", None))
        self.LabelApell.setText(QCoreApplication.translate("tablaClientes", u"Apellidos", None))
        self.LabelNumId.setText(QCoreApplication.translate("tablaClientes", u"Num_Identificaci\u00f3n", None))
        self.labelFecha.setText(QCoreApplication.translate("tablaClientes", u"Fecha_Nacimiento", None))
        self.labelPas.setText(QCoreApplication.translate("tablaClientes", u"Pais", None))
        self.labelTLF.setText(QCoreApplication.translate("tablaClientes", u"Tel\u00e9fono", None))
        self.labelMail.setText(QCoreApplication.translate("tablaClientes", u"E-mail", None))
        self.labelSexo.setText(QCoreApplication.translate("tablaClientes", u"Sexo", None))
        self.labelMenores.setText(QCoreApplication.translate("tablaClientes", u"Menores", None))
#if QT_CONFIG(tooltip)
        self.botonLeer.setToolTip(QCoreApplication.translate("tablaClientes", u"Leer", None))
#endif // QT_CONFIG(tooltip)
        self.botonLeer.setText("")
#if QT_CONFIG(tooltip)
        self.botonCrear.setToolTip(QCoreApplication.translate("tablaClientes", u"Crear", None))
#endif // QT_CONFIG(tooltip)
        self.botonCrear.setText("")
#if QT_CONFIG(tooltip)
        self.BotonUpdate.setToolTip(QCoreApplication.translate("tablaClientes", u"Actualizar", None))
#endif // QT_CONFIG(tooltip)
        self.BotonUpdate.setText("")
#if QT_CONFIG(tooltip)
        self.botonBorrar.setToolTip(QCoreApplication.translate("tablaClientes", u"Borrar", None))
#endif // QT_CONFIG(tooltip)
        self.botonBorrar.setText("")
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tablaClientes", u"Id", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tablaClientes", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tablaClientes", u"Apellidos", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tablaClientes", u"Num_Identificacion", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tablaClientes", u"Fecha_Nacimiento", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tablaClientes", u"Pais", None));
        ___qtablewidgetitem6 = self.tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tablaClientes", u"Tel\u00e9fono", None));
        ___qtablewidgetitem7 = self.tabla.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tablaClientes", u"E-mail", None));
        ___qtablewidgetitem8 = self.tabla.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tablaClientes", u"Sexo", None));
        ___qtablewidgetitem9 = self.tabla.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tablaClientes", u"Menores", None));
    # retranslateUi

