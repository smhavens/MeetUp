# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createAccountyKAUei.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_CreateUserWindow(object):
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 40, 91, 51))
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 80, 51, 51))
        self.label_3.setFont(font)
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(300, 430, 211, 41))
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(180, 390, 471, 21))
        palette1 = QPalette()
        brush1 = QBrush(QColor(80, 80, 80, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.password.setPalette(palette1)
        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(180, 190, 471, 21))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.username.setPalette(palette2)
        self.nameFirst = QLineEdit(self.centralwidget)
        self.nameFirst.setObjectName(u"nameFirst")
        self.nameFirst.setGeometry(QRect(180, 240, 201, 21))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.nameFirst.setPalette(palette3)
        self.nameLast = QLineEdit(self.centralwidget)
        self.nameLast.setObjectName(u"nameLast")
        self.nameLast.setGeometry(QRect(420, 240, 231, 21))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.nameLast.setPalette(palette4)
        self.emailInput = QLineEdit(self.centralwidget)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(180, 290, 471, 21))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.emailInput.setPalette(palette5)
        self.phoneInput = QLineEdit(self.centralwidget)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setGeometry(QRect(180, 340, 471, 21))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.phoneInput.setPalette(palette6)
        self.phoneInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700; color:#ff0000;\">Meet</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700; color:#ff0000;\">UP</span></p></body></html>", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.nameFirst.setText("")
        self.nameFirst.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.nameLast.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.emailInput.setText("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.phoneInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.menuHome.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

