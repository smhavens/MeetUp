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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 364, 525))
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

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.groupEventHalloween = QGroupBox(self.scrollAreaWidgetContents)
        self.groupEventHalloween.setObjectName(u"groupEventHalloween")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupEventHalloween.sizePolicy().hasHeightForWidth())
        self.groupEventHalloween.setSizePolicy(sizePolicy1)
        self.groupEventHalloween.setMinimumSize(QSize(0, 100))
        self.groupEventHalloween.setStyleSheet(u"border:0;")
        self.groupEventHalloween.setFlat(True)
        self.event_halloween = QPushButton(self.groupEventHalloween)
        self.event_halloween.setObjectName(u"event_halloween")
        self.event_halloween.setGeometry(QRect(20, 10, 161, 51))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 135))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.event_halloween.setPalette(palette2)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        font.setBold(True)
        self.event_halloween.setFont(font)
        self.event_halloween.setStyleSheet(u"QPushButton:hover {\n"
"            background:  rgb(170, 0, 0);\n"
"}")
        self.event_halloween.setFlat(True)
        self.label = QLabel(self.groupEventHalloween)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 81, 21))
        palette3 = QPalette()
        brush3 = QBrush(QColor(80, 80, 80, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label.setPalette(palette3)
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.groupEventHalloween)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.groupEvent_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupEvent_2.setObjectName(u"groupEvent_2")
        sizePolicy1.setHeightForWidth(self.groupEvent_2.sizePolicy().hasHeightForWidth())
        self.groupEvent_2.setSizePolicy(sizePolicy1)
        self.groupEvent_2.setMinimumSize(QSize(0, 100))
        self.groupEvent_2.setStyleSheet(u"border:0;")
        self.groupEvent_2.setFlat(True)
        self.event_halloween_2 = QPushButton(self.groupEvent_2)
        self.event_halloween_2.setObjectName(u"event_halloween_2")
        self.event_halloween_2.setGeometry(QRect(20, 10, 161, 41))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.event_halloween_2.setPalette(palette4)
        self.event_halloween_2.setFont(font)
        self.event_halloween_2.setStyleSheet(u"QPushButton:hover {\n"
"            background:  rgb(170, 0, 0);\n"
"}")
        self.event_halloween_2.setFlat(True)
        self.label_2 = QLabel(self.groupEvent_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 81, 21))
        palette5 = QPalette()
        brush4 = QBrush(QColor(93, 93, 93, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush5 = QBrush(QColor(95, 95, 95, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(100, 100, 100, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_2.setPalette(palette5)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.groupEvent_2)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.groupEvent3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupEvent3.setObjectName(u"groupEvent3")
        sizePolicy1.setHeightForWidth(self.groupEvent3.sizePolicy().hasHeightForWidth())
        self.groupEvent3.setSizePolicy(sizePolicy1)
        self.groupEvent3.setMinimumSize(QSize(0, 100))
        self.groupEvent3.setStyleSheet(u"border:0;")
        self.groupEvent3.setFlat(True)
        self.event_halloween_5 = QPushButton(self.groupEvent3)
        self.event_halloween_5.setObjectName(u"event_halloween_5")
        self.event_halloween_5.setGeometry(QRect(20, 10, 161, 51))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.event_halloween_5.setPalette(palette6)
        self.event_halloween_5.setFont(font)
        self.event_halloween_5.setStyleSheet(u"QPushButton:hover {\n"
"            background:  rgb(170, 0, 0);\n"
"}")
        self.event_halloween_5.setFlat(True)
        self.label_5 = QLabel(self.groupEvent3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 60, 81, 21))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_5.setPalette(palette7)
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.groupEvent3)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.groupEvent3_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupEvent3_2.setObjectName(u"groupEvent3_2")
        sizePolicy1.setHeightForWidth(self.groupEvent3_2.sizePolicy().hasHeightForWidth())
        self.groupEvent3_2.setSizePolicy(sizePolicy1)
        self.groupEvent3_2.setMinimumSize(QSize(0, 100))
        self.groupEvent3_2.setStyleSheet(u"border:0;")
        self.groupEvent3_2.setFlat(True)
        self.event_halloween_6 = QPushButton(self.groupEvent3_2)
        self.event_halloween_6.setObjectName(u"event_halloween_6")
        self.event_halloween_6.setGeometry(QRect(20, 10, 161, 51))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.event_halloween_6.setPalette(palette8)
        self.event_halloween_6.setFont(font)
        self.event_halloween_6.setStyleSheet(u"QPushButton:hover {\n"
"            background:  rgb(170, 0, 0);\n"
"}")
        self.event_halloween_6.setFlat(True)
        self.label_6 = QLabel(self.groupEvent3_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 81, 21))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_6.setPalette(palette9)
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.groupEvent3_2)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setBaseSize(QSize(100, 100))
        font2 = QFont()
        font2.setFamilies([u"MV Boli"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
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
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setFont(font2)
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
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
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
        self.groupEventHalloween.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.event_halloween.setText(QCoreApplication.translate("MainWindow", u"Halloween Party", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"10/30", None))
        self.groupEvent_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.event_halloween_2.setText(QCoreApplication.translate("MainWindow", u"Game Night", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"11/05", None))
        self.groupEvent3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.event_halloween_5.setText(QCoreApplication.translate("MainWindow", u"Movie Night", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"11/13", None))
        self.groupEvent3_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.event_halloween_6.setText(QCoreApplication.translate("MainWindow", u"Costume Party", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"12/01", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"New Events", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Event", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Invites", None))
        self.menuHome.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

