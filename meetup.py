import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from pythonUI.ui_loginCreate import Ui_MainWindow
from pythonUI.ui_login import Ui_LoginWindow
from pythonUI.ui_homepage import Ui_HomepageWindow


username = ''
userID = ''


class MeetUpApplication(QMainWindow):
    def __init__(self):
        super().__init__()
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


# Main function to run the application
def main():
    app = QApplication(sys.argv)
    main_app = MeetUpApplication()
    main_app.show()
    sys.exit(app.exec())

# Entry point for the application
if __name__ == "__main__":
    main()