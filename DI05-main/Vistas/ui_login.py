# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmLoginmBHOcV.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)
from Recursos.img import bg_rc

class Ui_asg_login(object):
    def setupUi(self, asg_login):
        if not asg_login.objectName():
            asg_login.setObjectName(u"asg_login")
        asg_login.setWindowModality(Qt.WindowModality.WindowModal)
        asg_login.resize(379, 392)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(asg_login.sizePolicy().hasHeightForWidth())
        asg_login.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        asg_login.setFont(font)
        asg_login.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/brianda1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        asg_login.setWindowIcon(icon)
        asg_login.setAutoFillBackground(False)
        asg_login.setStyleSheet(u"    QWidget {\n"
"        background-color: #1E1E2F;\n"
"        color: #F4F4F4;\n"
"        font-family: 'Arial', sans-serif;\n"
"        font-size: 14px;\n"
"    }\n"
"    \n"
"    QLabel {\n"
"        font-size: 18px;\n"
"        color: #E1E1E1;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QLineEdit {\n"
"        background-color: #2D2D3C;\n"
"        border: 1px solid #4C9DFF;\n"
"        border-radius: 8px;\n"
"        padding: 10px;\n"
"        color: #F4F4F4;\n"
"        font-size: 14px;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 1px solid #00B8D4;\n"
"\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #4C9DFF;\n"
"        color: #000000;\n"
"        border-radius: 12px;\n"
"        padding: 12px 25px;\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"        min-width: 100px;\n"
"        min-height: 25px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #5BB6FF;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: "
                        "#3A80CC;\n"
"    }\n"
"\n"
"    QMenuBar {\n"
"        background-color: #1E1E2F;\n"
"        color: #F4F4F4;\n"
"        font-size: 14px;\n"
"    }\n"
"    QMenuBar::item {\n"
"        background-color: transparent;\n"
"        padding: 8px 15px;\n"
"    }\n"
"    QMenuBar::item:selected {\n"
"        background-color: #00B8D4;\n"
"        color: #1E1E2F;\n"
"    }\n"
"    \n"
"    QMenu {\n"
"        background-color: #2D2D3C;\n"
"        color: #F4F4F4;\n"
"        border: 1px solid #4C9DFF;\n"
"    }\n"
"    QMenu::item {\n"
"        padding: 8px 20px;\n"
"    }\n"
"    QMenu::item:selected {\n"
"        background-color: #00B8D4;\n"
"    }\n"
"\n"
"    QStatusBar {\n"
"        background-color: #1E1E2F;\n"
"        color: #F4F4F4;\n"
"        font-size: 12px;\n"
"    }\n"
"    ")
        asg_login.setIconSize(QSize(0, 0))
        self.actionSalir = QAction(asg_login)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(asg_login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(379, 10))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setFrameShadow(QFrame.Shadow.Plain)
        self.logo.setLineWidth(10)
        self.logo.setPixmap(QPixmap(u":/prefijoNuevo/brianda1.png"))

        self.horizontalLayout_2.addWidget(self.logo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.usuarioEdit = QLineEdit(self.centralwidget)
        self.usuarioEdit.setObjectName(u"usuarioEdit")
        self.usuarioEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.usuarioEdit)

        self.passEdit = QLineEdit(self.centralwidget)
        self.passEdit.setObjectName(u"passEdit")
        self.passEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.passEdit.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.passEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.passEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.asg_pushButton = QPushButton(self.centralwidget)
        self.asg_pushButton.setObjectName(u"asg_pushButton")
        self.asg_pushButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(28)
        sizePolicy2.setVerticalStretch(29)
        sizePolicy2.setHeightForWidth(self.asg_pushButton.sizePolicy().hasHeightForWidth())
        self.asg_pushButton.setSizePolicy(sizePolicy2)
        self.asg_pushButton.setMinimumSize(QSize(150, 49))
        self.asg_pushButton.setMaximumSize(QSize(75, 44))
        self.asg_pushButton.setSizeIncrement(QSize(9, 8))
        self.asg_pushButton.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.asg_pushButton.setFont(font1)
        self.asg_pushButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.asg_pushButton.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.asg_pushButton.setAcceptDrops(False)
        self.asg_pushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.asg_pushButton.setStyleSheet(u"")
        self.asg_pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.asg_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(1, QFormLayout.FieldRole, self.verticalSpacer)

        asg_login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(asg_login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 379, 33))
        self.menuMen = QMenu(self.menubar)
        self.menuMen.setObjectName(u"menuMen")
        asg_login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(asg_login)
        self.statusbar.setObjectName(u"statusbar")
        asg_login.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMen.menuAction())
        self.menuMen.addAction(self.actionSalir)

        self.retranslateUi(asg_login)

        QMetaObject.connectSlotsByName(asg_login)
    # setupUi

    def retranslateUi(self, asg_login):
        asg_login.setWindowTitle(QCoreApplication.translate("asg_login", u"Tarea5", None))
        self.actionSalir.setText(QCoreApplication.translate("asg_login", u"Salir", None))
        self.logo.setText("")
#if QT_CONFIG(tooltip)
        self.usuarioEdit.setToolTip(QCoreApplication.translate("asg_login", u"Introduce usuario", None))
#endif // QT_CONFIG(tooltip)
        self.usuarioEdit.setText("")
        self.usuarioEdit.setPlaceholderText(QCoreApplication.translate("asg_login", u"Username", None))
#if QT_CONFIG(tooltip)
        self.passEdit.setToolTip(QCoreApplication.translate("asg_login", u"Introduce password", None))
#endif // QT_CONFIG(tooltip)
        self.passEdit.setInputMask("")
        self.passEdit.setText("")
        self.passEdit.setPlaceholderText(QCoreApplication.translate("asg_login", u"Password", None))
#if QT_CONFIG(tooltip)
        self.asg_pushButton.setToolTip(QCoreApplication.translate("asg_login", u"Click para hacer Login", None))
#endif // QT_CONFIG(tooltip)
        self.asg_pushButton.setText(QCoreApplication.translate("asg_login", u"Login", None))
        self.menuMen.setTitle(QCoreApplication.translate("asg_login", u"Men\u00fa", None))
    # retranslateUi

