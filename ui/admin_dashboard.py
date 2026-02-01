import sys
import os
import time
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6 import uic


# This tells Python: "Look one folder up to find 'core'"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we can import your database function
from core.database import fetch_employees


class AdminDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        # This command loads your design directly
        # "self" means: "Put all the buttons and tables into my backpack"
        uic.loadUi("ui/dashboard_ESDAC.ui",self)

        # Test the button connection immediately
        self.scan_btn.clicked.connect(self.scan_action)

    def scan_action(self):
        # 1. Update text to show we are working
        self.result_lbl.setText("Scanning Database...")
        self.result_lbl.setStyleSheet("color: yellow;")
        # This tells Python: "Stop everything, paint the screen NOW, then continue."
        QApplication.processEvents()

        # This keeps the yellow text on screen for 2 seconds
        time.sleep(2)
        
        # 2. Call the Spy (Your Database Function)
        data = fetch_employees()
        
        # 3. Check what we got
        if data:
            print("--- DATA RECEIVED ---")
            for person in data:
                print(person)
            
            # Update the UI Label
            self.result_lbl.setText(f"SUCCESS: Retrieved {len(data)} records.")
            self.result_lbl.setStyleSheet("color: #00FF00;")
        else:
            self.result_lbl.setText("ERROR: Connection Failed.")
            self.result_lbl.setStyleSheet("color: red;")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = AdminDashboard()
    window.show()
    sys.exit(app.exec())