# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acercaosbGKY.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QWidget)
from Recursos.img import bg_rc

class Ui_Acerca(object):
    def setupUi(self, Acerca):
        if not Acerca.objectName():
            Acerca.setObjectName(u"Acerca")
        Acerca.setWindowModality(Qt.WindowModality.WindowModal)
        Acerca.resize(400, 300)
        Acerca.setMinimumSize(QSize(400, 300))
        Acerca.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/brianda1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Acerca.setWindowIcon(icon)
        Acerca.setStyleSheet(u"    QDialog {\n"
"        background-color: #1E1E2F;\n"
"        color: #F4F4F4;\n"
"        font-family: 'Arial', sans-serif;\n"
"        font-size: 14px;\n"
"    }\n"
"    \n"
"    QLabel {\n"
"        font-size: 18px;\n"
"        color: #E1E1E1;\n"
"\n"
"    }\n"
"\n"
"\n"
"    QStatusBar {\n"
"        background-color: #1E1E2F;\n"
"        color: #F4F4F4;\n"
"        font-size: 12px;\n"
"    }\n"
"    \n"
"QDialog QLabel#label_2{\n"
"    background-color: rgba(41, 41, 61, 0.5); \n"
"    border-radius: 15px;\n"
"	    border: 2px solid #5D6D7E;\n"
"}")
        self.horizontalLayoutWidget = QWidget(Acerca)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 10, 341, 111))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.logo_acerca = QLabel(self.horizontalLayoutWidget)
        self.logo_acerca.setObjectName(u"logo_acerca")
        self.logo_acerca.setFrameShape(QFrame.Shape.NoFrame)
        self.logo_acerca.setFrameShadow(QFrame.Shadow.Plain)
        self.logo_acerca.setLineWidth(10)
        self.logo_acerca.setPixmap(QPixmap(u":/prefijoNuevo/brianda1.png"))

        self.horizontalLayout.addWidget(self.logo_acerca)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.contenedor_logo = QLabel(self.horizontalLayoutWidget)
        self.contenedor_logo.setObjectName(u"contenedor_logo")

        self.horizontalLayout.addWidget(self.contenedor_logo)

        self.label_2 = QLabel(Acerca)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 170, 331, 101))
        self.label_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frameLogo = QFrame(Acerca)
        self.frameLogo.setObjectName(u"frameLogo")
        self.frameLogo.setGeometry(QRect(30, 170, 331, 101))
        self.frameLogo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.frameLogo.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_2.raise_()

        self.retranslateUi(Acerca)

        QMetaObject.connectSlotsByName(Acerca)
    # setupUi

    def retranslateUi(self, Acerca):
        Acerca.setWindowTitle(QCoreApplication.translate("Acerca", u"Acerca", None))
        self.logo_acerca.setText("")
        self.contenedor_logo.setText("")
        self.label_2.setText(QCoreApplication.translate("Acerca", u"Aplicaci\u00f3n creada por Alberto Serradilla\n"
"Versi\u00f3n 1.0\u00a9 2025 \n"
"Todos los derechos reservados", None))
    # retranslateUi

