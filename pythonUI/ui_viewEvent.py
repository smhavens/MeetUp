# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewEventYKbwSz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_ViewEventWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MeetUP!")
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 781, 531))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(83, 83, 83, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.scrollArea.setPalette(palette1)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 767, 563))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.eventName = QLabel(self.scrollAreaWidgetContents)
        self.eventName.setObjectName(u"eventName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventName.sizePolicy().hasHeightForWidth())
        self.eventName.setSizePolicy(sizePolicy)
        self.eventName.setMinimumSize(QSize(0, 50))
        palette2 = QPalette()
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(255, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.eventName.setPalette(palette2)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(24)
        font.setBold(True)
        self.eventName.setFont(font)
        self.eventName.setAutoFillBackground(True)
        self.eventName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.eventName)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QSize(0, 50))
        self.groupBox_5.setBaseSize(QSize(100, 100))
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 0, 211, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(0, 50))
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 10, 291, 31))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.groupBox.setBaseSize(QSize(100, 100))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 0, 91, 50))
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 50))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 10, 291, 31))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(0, 50))
        self.groupBox_2.setBaseSize(QSize(100, 100))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 261, 50))
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 10, 291, 31))
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setMinimumSize(QSize(0, 50))
        self.groupBox_3.setBaseSize(QSize(100, 100))
        self.budgetLabel = QLabel(self.groupBox_3)
        self.budgetLabel.setObjectName(u"budgetLabel")
        self.budgetLabel.setGeometry(QRect(20, 0, 261, 50))
        sizePolicy1.setHeightForWidth(self.budgetLabel.sizePolicy().hasHeightForWidth())
        self.budgetLabel.setSizePolicy(sizePolicy1)
        self.budgetLabel.setMinimumSize(QSize(0, 50))
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 10, 291, 31))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.groupBox_4.setMinimumSize(QSize(0, 200))
        self.activityList = QListWidget(self.groupBox_4)
        self.activityList.setObjectName(u"activityList")
        self.activityList.setGeometry(QRect(165, 31, 571, 161))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.activityList.sizePolicy().hasHeightForWidth())
        self.activityList.setSizePolicy(sizePolicy4)
        palette3 = QPalette()
        brush5 = QBrush(QColor(85, 85, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(95, 95, 95, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush7 = QBrush(QColor(85, 85, 255, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.activityList.setPalette(palette3)
        self.activityList.setStyleSheet(u"QListWidget {\n"
"	font: 12pt \"MV Boli\";\n"
"	color: rgb(85, 85, 255);\n"
"	background: rgb(95, 95, 95);\n"
"}")
        self.activityList.setAlternatingRowColors(True)
        self.activityList.setViewMode(QListView.ViewMode.ListMode)
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 281, 50))
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy2.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy2)
        self.groupBox_11.setMinimumSize(QSize(0, 50))
        self.submitButton = QPushButton(self.groupBox_11)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setEnabled(True)
        self.submitButton.setGeometry(QRect(260, 20, 241, 24))
        palette4 = QPalette()
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(0, 170, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush9)
        brush10 = QBrush(QColor(127, 255, 127, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush10)
        brush11 = QBrush(QColor(63, 255, 63, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush11)
        brush12 = QBrush(QColor(0, 127, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush12)
        brush13 = QBrush(QColor(0, 170, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        brush14 = QBrush(QColor(255, 255, 220, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush14)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush8)
        brush15 = QBrush(QColor(0, 0, 0, 127))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        brush16 = QBrush(QColor(255, 255, 255, 135))
        brush16.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        brush17 = QBrush(QColor(0, 255, 0, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush8)
        brush18 = QBrush(QColor(0, 127, 0, 127))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        brush19 = QBrush(QColor(76, 255, 76, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.submitButton.setPalette(palette4)
        self.submitButton.setAutoFillBackground(False)
        self.submitButton.setStyleSheet(u"QPushButton {\n"
"border: 10;\n"
"border-radius: 10;\n"
"border-color: grey;\n"
"color: red;\n"
"font: 16pt \"MV Boli\";\n"
"background: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(0, 0, 127);\n"
"}")

        self.verticalLayout_2.addWidget(self.groupBox_11, 0, Qt.AlignmentFlag.AlignVCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.eventName.setText(QCoreApplication.translate("MainWindow", u"event", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Unique EventID</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#00007f;\">eventID</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Day</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#00007f;\">dayInfo</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Time</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#00007f;\">timeInfo</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.budgetLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Budget</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#00007f;\">budgetInfo</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#000000;\">Activities</span></p></body></html>", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Return To Homepage", None))
    # retranslateUi

