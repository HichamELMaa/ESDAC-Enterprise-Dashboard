#imports
import sys
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit,QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic


#Class
class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # This command loads your design directly
        # "self" means: "Put all the buttons and tables into my backpack"
        uic.loadUi("ui/dashboard.ui",self)
        # Now we can talk to the items using the names you gave them
        self.setWindowTitle("Student Management System")

        # Test the button connection immediately
        self.refresh_btn.clicked.connect(self.test_click)


    def test_click(self):
        print("Button Clicked! The UI is alive.")

        
        
        
        
        
        
        
        
        
        """self.resize(800,600)
        self.setWindowTitle("Admin Dashboard")

        layout = QVBoxLayout()
        Dash_label = QLabel("Security Dashboard: ONLINE")
        Dash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Dash_label.setObjectName("DashLabel")

        Dash_btn = QPushButton("Logout")

        layout.addWidget(Dash_label)
        layout.addWidget(Dash_btn)

        self.setLayout(layout)"""


