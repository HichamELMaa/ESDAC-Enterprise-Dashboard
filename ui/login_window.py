# imports form PyQt6 for the application window
import sys 
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit,QMessageBox
from PyQt6.QtCore import Qt
from ui.dashboard_window import DashboardWindow


#Inheritance (The "Chassis" Strategy)
class LoginWindow(QWidget): # This is the inheritance part
    def __init__(self): # constructor
        super().__init__() #The Parent Call
        self.resize(500, 400)
        self.setWindowTitle("ESDA Security Console")

        layout = QVBoxLayout() # create layout object
        layout.setSpacing(20)
        layout.setContentsMargins(50, 50, 50, 50)

        title_label = QLabel("ESDAC Login") #create label object
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("HeaderLabel")
        self.username_input = QLineEdit() #create input object
        self.username_input.setPlaceholderText("Username")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        push_btn = QPushButton("Log in") #create btn object
        
        push_btn.clicked.connect(self.check_login)
        layout.addWidget(title_label) # adding label to the layout
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(push_btn)# adding btn to the layout 

        self.setLayout(layout)



    def check_login(self):

        user_text = self.username_input.text()
        user_password = self.password_input.text()

        if user_text.startswith("C##") and user_password == "admin123":
            QMessageBox.information(self, "Information", "ACCESS GRANTED: Success: Admin Panel Unlocked")
            # 1. Create the Dashboard (Save it to 'self' so it stays alive)
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()

        else:
            print("Error: Invalid Credentials")
            QMessageBox.warning(self, "Information", "Error: Invalid Credentials")

