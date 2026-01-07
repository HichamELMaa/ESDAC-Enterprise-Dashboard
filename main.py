import sys
from PyQt6.QtWidgets import QApplication
from ui.login_window import LoginWindow


if __name__ == "__main__":

    # 1. Create the App first
    app = QApplication(sys.argv)

    # 2. Dress (Load Style immediately after)
    with open("ui/style.qss", "r") as styleFile:
        app.setStyleSheet(styleFile.read())

    # 3. Work (Then create windows)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())