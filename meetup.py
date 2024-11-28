import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from pythonUI.ui_loginCreate import Ui_MainWindow
from pythonUI.ui_login import Ui_LoginWindow
from pythonUI.ui_homepage import Ui_HomepageWindow
import mysql

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


username = ''
userID = None
main_app = None
mycursor = None




class MeetUpApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeetUP!")
        self.ui_loginCreate = Ui_MainWindow()
        self.ui_loginCreate.setupUi(self)
        
        self.ui_loginCreate.loginButton.clicked.connect(self.open_login_window)
        
    def open_login_window(self):
         # Hide the current window
        self.hide()

        # Create and show the second window
        self.ui_login = LoginWindow()
        self.ui_login.show()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the second UI
        self.ui_login = Ui_LoginWindow()
        self.ui_login.setupUi(self)
        
        self.ui_login.loginButton.clicked.connect(self.submit_login)
        self.ui_login.actionLogout.triggered.connect(lambda: logout(self))
        
    def submit_login(self):
        # Retrieve the username and password
        self.username = self.ui_login.username.text()
        self.password = self.ui_login.password.text()

        # Set these as attributes, or you can validate/store them as needed
        print(f"Username: {self.username}")
        print(f"Password: {self.username}")

        # Optional: Add validation or proceed to another action
        if self.username == "admin" and self.password == "password123":
            print("Login successful!")
            global username
            username = self.username
            self.hide()
            self.ui_homepage = HomepageWindow()
            self.ui_homepage.show()
        else:
            print("Invalid credentials.")

        # Optional: Connect buttons in the second UI to other methods
        # Example: self.ui_second.backButton.clicked.connect(self.go_back)


class HomepageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the second UI
        self.ui_homepage = Ui_HomepageWindow()
        self.ui_homepage.setupUi(self)
        scrollArea = self.ui_homepage.scrollAreaWidgetContents
        
        self.ui_homepage.actionLogout.triggered.connect(lambda: logout(self))
        
    def myEvents(self):
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
        brush = QBrush(QColor(85, 170, 255, 255))
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
        brush1 = QBrush(QColor(255, 255, 255, 255))
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
        
        # self.groupEvent_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        # self.event_halloween_2.setText(QCoreApplication.translate("MainWindow", u"Game Night", None))
        # self.label_2.setText(QCoreApplication.translate("MainWindow", u"11/05", None))


def logout(current_page):
    global username, main_app
    
    current_page.hide()
    username = None
    main_app.show()
    


# Main function to run the application
def main():
    app = QApplication(sys.argv)
    
    global main_app, mycursor
    
    conn = mysql.connector.connect(
    host= '216.137.179.68'
    )   

    mycursor = conn.cursor()
    
    main_app = MeetUpApplication()
    main_app.show()
    sys.exit(app.exec())

# Entry point for the application
if __name__ == "__main__":
    main()