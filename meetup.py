import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from pythonUI.ui_loginCreate import Ui_MainWindow
from pythonUI.ui_login import Ui_LoginWindow
from pythonUI.ui_homepage import Ui_HomepageWindow
from pythonUI.ui_createAccount import Ui_CreateUserWindow
from pythonUI.ui_createEvent import Ui_CreateEventWindow
from pythonUI.ui_invites import Ui_InviteWindow
from pythonUI.ui_manageEvent import Ui_ManageEventWindow
from pythonUI.ui_viewEvent import Ui_ViewEventWindow
import mysql.connector

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


username = None
main_app = None
mycursor = None
mydb = None


class MeetUpApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeetUP!")
        self.ui_loginCreate = Ui_MainWindow()
        self.ui_loginCreate.setupUi(self)
        
        self.ui_loginCreate.loginButton.clicked.connect(self.open_login_window)
        self.ui_loginCreate.loginButton_2.clicked.connect(self.open_create_window)
        
    def open_login_window(self):
         # Hide the current window
        self.hide()

        # Create and show the second window
        self.ui_login = LoginWindow()
        self.ui_login.show()
        
    def open_create_window(self):
        self.hide()
        self.ui_create = CreateUserWindow()
        self.ui_create.show()


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
        print(f"Password: {self.password}")
        
        query = """SELECT valid_login(%s, %s) AS isValid;"""
        mycursor.execute(query, (self.username, self.password))
        valid = mycursor.fetchone()
        print(valid)
        # Optional: Add validation or proceed to another action
        if valid[0]:
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


class CreateUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_createUser = Ui_CreateUserWindow()
        self.ui_createUser.setupUi(self)
        
        self.ui_createUser.loginButton.clicked.connect(self.createUser)
        
    def createUser(self):
        global username, mydb, mycursor
        self.username = self.ui_createUser.username.text()
        self.password = self.ui_createUser.password.text()
        self.firstName = self.ui_createUser.nameFirst.text()
        self.lastName = self.ui_createUser.nameLast.text()
        self.email = self.ui_createUser.emailInput.text()
        self.phone = self.ui_createUser.phoneInput.text()
        
        query = """SELECT * FROM user WHERE userID = %s;"""
        mycursor.execute(query, (self.username,))
        valid = mycursor.fetchone()
        while mycursor.nextset():
            pass
        
        if not valid:
            query = """CALL create_user(%s, %s, %s, %s, %s, %s);"""
            mycursor.execute(query, (self.username, self.firstName, self.lastName, self.email, self.phone, self.password))
            mydb.commit()
            username = self.username
            self.hide()
            self.ui_homepage = HomepageWindow()
            self.ui_homepage.show()
        
        


class HomepageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global username
        # Set up the second UI
        self.ui_homepage = Ui_HomepageWindow()
        self.ui_homepage.setupUi(self)
        self.scrollArea = self.ui_homepage.scrollAreaWidgetContents
        self.ui_homepage.actionLogout.triggered.connect(lambda: logout(self))
        self.ui_homepage.pushButton.clicked.connect(self.open_new_event)
        self.ui_homepage.pushButton_2.clicked.connect(self.open_invites)
        
        # print(f"QUERY: CALL list_all_invitedto_and_hosted_events('{username}');")
        query = """CALL list_all_invitedto_and_hosted_events(%s);"""

        try:
            # print("TRYING")
            # mycursor.execute(query, (username,), multi=True)
            mycursor.callproc('list_all_invitedto_and_hosted_events', (username,))
            # print(username)
            
            # Check if rows are returned
            results = mycursor.stored_results()
            for result in results:
                allEvents = result.fetchall()
                if allEvents:
                    # print(f"Found {len(allEvents)} events")
                    for event in allEvents:
                        # print("An INVITE!")  # Debugging message
                        eventID, name, day, time = event
                        # print(eventID, name, day, time)  # Debugging message
                        self.myEvents(name, day, time, eventID)
                else:
                    print("No events found!")
        except Exception as e:
            print(f"Error: {e}")

    
    
    def open_new_event(self):
        self.hide()
        self.ui_newEvent = CreateEventWindow()
        self.ui_newEvent.show()
        
        
    def open_invites(self):
        self.hide()
        self.ui_inviteView = InviteWindow()
        self.ui_inviteView.show()
    
    
    def myEvents(self, name, day, time, eventID):
        self.line_2 = QFrame(self.ui_homepage.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.ui_homepage.verticalLayout_2.addWidget(self.line_2)
        
        self.newGroup = QGroupBox(self.scrollArea)
        # self.groupEventHalloween = QGroupBox(self.scrollAreaWidgetContents)
        self.newGroup.setObjectName(f"eventBox{name}")
        # self.groupEventHalloween.setObjectName(u"groupEventHalloween")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newGroup.sizePolicy().hasHeightForWidth())
        self.newGroup.setSizePolicy(sizePolicy1)
        self.newGroup.setMinimumSize(QSize(0, 100))
        self.newGroup.setStyleSheet(u"border:0;")
        self.newGroup.setFlat(True)
        self.tempEvent = QPushButton(self.newGroup)
        self.tempEvent.setObjectName(f"event{name}")
        self.tempEvent.setGeometry(QRect(20, 10, 161, 51))
        palette2 = QPalette()
        brush = QBrush(QColor(85, 170, 255, 255))
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
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
        self.tempEvent.setPalette(palette2)
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(14)
        font.setBold(True)
        self.tempEvent.setFont(font)
        self.tempEvent.setStyleSheet(u"QPushButton:hover {\n"
                                    "            background:  rgb(170, 0, 0);\n"
                                    "}")
        self.tempEvent.setFlat(True)
        self.label = QLabel(self.newGroup)
        self.label.setObjectName(u"label" + name)
        self.label.setGeometry(QRect(20, 60, 311, 21))
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

        self.ui_homepage.verticalLayout_2.addWidget(self.newGroup)
        
        # self.newGroup.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.tempEvent.setProperty("eventID", eventID)
        # self.tempEvent.setProperty("isHost", is_host)
        self.tempEvent.clicked.connect(self.open_event_details)
        self.tempEvent.setText(name)
        self.label.setText(day + u" at " + time)
        
        # self.groupEvent_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        # self.event_halloween_2.setText(QCoreApplication.translate("MainWindow", u"Game Night", None))
        # self.label_2.setText(QCoreApplication.translate("MainWindow", u"11/05", None))

    def open_event_details(self):
        button = self.sender()
        
        eventID = button.property("eventID")
        isHost = self.is_Host(eventID)
        
        if isHost:
            print(isHost, "IS HOST!")
            self.hide()
            self.ui_openEvent = ManageEventWindow(eventID)
            self.ui_openEvent.show()
        else:
            print(isHost, "IS NOT HOST!")
            self.hide()
            self.ui_openEvent = ViewEventWindow(eventID)
            self.ui_openEvent.show()
        
    def is_Host(self, eventID):
        global username
        query = """SELECT userID FROM event WHERE eventID = %s;"""
        print("SEARCHING", eventID, "FOR HOST", username)
        mycursor.execute(query, (eventID,))
        valid = mycursor.fetchone()
        
        
        print("IS HOST?:", valid[0])
        
        return valid[0] == username


class CreateEventWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global username
        # Set up the second UI
        self.ui_createEvent = Ui_CreateEventWindow()
        self.ui_createEvent.setupUi(self)
        self.invitees = []
        self.activities = []
        self.ui_createEvent.submitButton.clicked.connect(self.submit_event)
        self.ui_createEvent.inputUsername.returnPressed.connect(self.add_invitee)
        self.ui_createEvent.inputActivity.returnPressed.connect(self.add_activity)
        
    def submit_event(self):
        #test
        self.eventID = self.ui_createEvent.inputEventID.text()
        self.eventName = self.ui_createEvent.nameInput.text()
        self.eventDate = self.ui_createEvent.dateInput.date().toString("yyyy-MM-dd")
        self.eventStart = self.ui_createEvent.timeStart.time().toString("HH:mm:ss")
        # self.eventEnd = self.ui_createEvent.timeEnd.time().toString("HH:mm:ss")
        self.budget = self.ui_createEvent.inputBudget.value()
        
        if self.valid_eventID():
            query = "CALL create_event(%s, %s, %s, %s, %s, %s)"
            mycursor.execute(query, (self.eventID, self.eventName, self.eventDate, self.eventStart, self.budget, username))
            mydb.commit()
            while mycursor.nextset():
                pass
            for activity in self.activities:
                query = "CALL add_activity(%s, %s)"
                mycursor.execute(query, (activity, self.eventID))
                mydb.commit()
            for invite in self.invitees:
                query = "CALL invite_guest(%s, %s)"
                mycursor.execute(query, (invite, self.eventID))
                mydb.commit()
            self.hide()
            self.ui_home = HomepageWindow()
            self.ui_home.show()
        else:
            self.ui_createEvent.eventIDError.setVisible(True)
    
    def add_invitee(self):
        # Get the username from the input field
        print("Attempting to add Invitee")
        invitee = self.ui_createEvent.inputUsername.text()
        self.ui_createEvent.inputUsername.clear()
        
        query = """SELECT * FROM user WHERE userID = %s;"""
        mycursor.execute(query, (invitee,))
        valid = mycursor.fetchone()
        print(valid)
        while mycursor.nextset():
            pass

        if valid and invitee and invitee != username and invitee not in self.invitees:
            print("valid Invitee")
            # Add the username to the list
            self.invitees.append(invitee)
            buttonName = u"pushButton" + invitee
            # Create a button for the invitee
            self.pushButton = QPushButton(self.ui_createEvent.inviteList)
            self.pushButton.setObjectName(buttonName)
            sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
            sizePolicy1.setHorizontalStretch(0)
            sizePolicy1.setVerticalStretch(0)
            sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy1)
            self.pushButton.setMinimumSize(QSize(125, 0))
            self.pushButton.setAutoFillBackground(False)
            self.pushButton.setStyleSheet(u"QPushButton {\n"
                                            "border: 10;\n"
                                            "border-radius: 11;\n"
                                            "border-color: grey;\n"
                                            "color: white;\n"
                                            "font: 16pt \"MV Boli\";\n"
                                            "background: rgb(0, 170, 255);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background: rgb(0, 0, 127);\n"
                                            "}")
            self.pushButton.setText(invitee)
            row_limit = 5
            row = len(self.invitees) // row_limit
            column = len(self.invitees) % row_limit
            self.ui_createEvent.gridLayout.addWidget(self.pushButton, row, column, 1, 1)
            button = QPushButton(invitee, self)
            button.clicked.connect(lambda: print(f"{invitee} clicked!"))

            # # Add the button to the layout
            # self.invitees_layout.addWidget(button)

            # # Clear the input field
            # self.username_input.clear()

            print("Current Invitees:", self.invitees)  # Debugging output
    
    def add_activity(self):
        activity_name = self.ui_createEvent.inputActivity.text()
        
        # Check if the input is not empty
        if activity_name:
            # Add the activity to the list widget
            self.ui_createEvent.activityList.addItem(activity_name)
        
            # Clear the input field
            self.ui_createEvent.inputActivity.clear()
            self.activities.append(activity_name)

    
    def valid_eventID(self):
        query = """SELECT * FROM event WHERE eventID = %s;"""
        mycursor.execute(query, (self.eventID,))
        valid = mycursor.fetchone()
        while mycursor.nextset():
            pass
        
        return not valid


class ManageEventWindow(QMainWindow):
    def __init__(self, eventID):
        super().__init__()
        global username
        self.ui_manageEvent = Ui_ManageEventWindow()
        self.ui_manageEvent.setupUi(self)
        
        
        
class ViewEventWindow(QMainWindow):
    def __init__(self, eventID):
        super().__init__()
        global username
        self.ui_viewEvent = Ui_ViewEventWindow()
        self.ui_viewEvent.setupUi(self)
        self.ui_viewEvent.submitButton.clicked.connect(self.return_home)
        
        
        if mycursor.with_rows:
            mycursor.fetchall()  # Clear current result set

        query = """SELECT eventName, eventDay, eventTime, budget FROM event WHERE eventID = %s;"""
        mycursor.execute(query, (eventID,))
        self.eventName, self.eventDay, self.eventTime, self.eventBudget = mycursor.fetchone()
        self.activities = []
        
        query = """SELECT activityName FROM activity WHERE eventID = %s;"""
        mycursor.execute(query, (eventID,))
        for activity in mycursor.fetchall():
            print(activity)
            self.activities.append(activity[0])
            self.ui_viewEvent.activityList.addItem(activity[0])
        self.textStart = '<html><head/><body><p align="center"><span style=" font-size:16pt; color:#00007f;">'
        self.textEnd = '</span></p></body></html>'
        self.ui_viewEvent.eventName.setText(self.eventName)
        self.ui_viewEvent.label_3.setText(self.textStart + self.eventDay + self.textEnd)
        self.ui_viewEvent.label.setText(self.textStart + self.eventTime + self.textEnd)
        self.ui_viewEvent.label_2.setText(self.textStart + str(self.eventBudget) + self.textEnd)
        self.ui_viewEvent.label_4.setText(self.textStart + eventID + self.textEnd)
        
    def return_home(self):
        self.hide()
        self.ui_homepage = HomepageWindow()
        self.ui_homepage.show()
        
        
class InviteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global username
        self.ui_inviteEvent = Ui_InviteWindow()
        self.ui_inviteEvent.setupUi(self)

def logout(current_page):
    global username, main_app
    
    current_page.hide()
    username = None
    main_app.show()
    


# Main function to run the application
def main():
    app = QApplication(sys.argv)
    
    global main_app, mycursor, mydb
    
    mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost', database='meetup',
                              auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    myresponce = mycursor.fetchall()

    print(myresponce)
    
    main_app = MeetUpApplication()
    main_app.show()
    sys.exit(app.exec())

# Entry point for the application
if __name__ == "__main__":
    main()