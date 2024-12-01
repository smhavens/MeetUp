# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 592)
        palette = QPalette()
        brush = QBrush(QColor(85, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.myEvents = QScrollArea(self.centralwidget)
        self.myEvents.setObjectName(u"myEvents")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myEvents.sizePolicy().hasHeightForWidth())
        self.myEvents.setSizePolicy(sizePolicy)
        self.myEvents.setMinimumSize(QSize(0, 400))
        self.myEvents.setBaseSize(QSize(0, 400))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.myEvents.setPalette(palette1)
        self.myEvents.setAutoFillBackground(False)
        self.myEvents.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.myEvents.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 374, 388))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_myEvents = QLabel(self.scrollAreaWidgetContents)
        self.label_myEvents.setObjectName(u"label_myEvents")
        sizePolicy.setHeightForWidth(self.label_myEvents.sizePolicy().hasHeightForWidth())
        self.label_myEvents.setSizePolicy(sizePolicy)
        self.label_myEvents.setStyleSheet(u"border: 0;\n"
"color: red;\n"
"font: 24pt \"MV Boli\";")
        self.label_myEvents.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_myEvents)

        self.myEvents.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.myEvents)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(50, 300))
        self.groupBox.setBaseSize(QSize(100, 0))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"QGroupBox#theBox {border:0;};\n"
"border:0;")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setBaseSize(QSize(100, 100))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"border: 10;\n"
"border-radius: 56;\n"
"border-color: grey;\n"
"color: red;\n"
"font: 16pt \"MV Boli\";\n"
"background: white;\n"
"}\n"
"QPushButton:hover {\n"
"            background: rgb(0, 0, 127);\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"border: 10;\n"
"border-radius: 56;\n"
"border-color: grey;\n"
"color: red;\n"
"font: 16pt \"MV Boli\";\n"
"background: white;\n"
"}\n"
"QPushButton:hover {\n"
"            background: rgb(0, 0, 127);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 33))
        self.menubar.setAutoFillBackground(True)
        self.menuHome = QMenu(self.menubar)
        self.menuHome.setObjectName(u"menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHome.menuAction())
        self.menuHome.addAction(self.actionHome)
        self.menuHome.addAction(self.actionLogout)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_myEvents.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; text-decoration: underline; color:#ff0000;\">My Events</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"New Events", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Event", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Invites", None))
        self.menuHome.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

