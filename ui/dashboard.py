import customtkinter as ctk
import sys
import os

# --- THE PATH FIX ---
# This tells Python: "Look one folder up to find 'core'"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we can import your database function
from core.database import fetch_employees

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ESDAC_Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ESDAC - Enterprise Security Dashboard")
        self.geometry("900x600")

        self.label = ctk.CTkLabel(
            self, 
            text="SYSTEM STATUS: ONLINE", 
            font=("Roboto", 24, "bold"),
            text_color="#00FF00"
        )
        self.label.pack(pady=40)

        self.button = ctk.CTkButton(
            self, 
            text="Scan HR Database", 
            command=self.scan_action # Connects to the function below
        )
        self.button.pack(pady=20)
        
        # A text box to show results in the UI later
        self.result_label = ctk.CTkLabel(self, text="Waiting for scan...", font=("Roboto", 14))
        self.result_label.pack(pady=10)

    def scan_action(self):
        # 1. Update text to show we are working
        self.result_label.configure(text="Scanning Database...", text_color="yellow")
        self.update() # Force refresh
        
        # 2. Call the Spy (Your Database Function)
        data = fetch_employees()
        
        # 3. Check what we got
        if data:
            print("--- DATA RECEIVED ---")
            for person in data:
                print(person)
            
            # Update the UI Label
            self.result_label.configure(text=f"SUCCESS: Retrieved {len(data)} records.", text_color="#00FF00")
        else:
            self.result_label.configure(text="ERROR: Connection Failed.", text_color="red")

if __name__ == "__main__":
    app = ESDAC_Dashboard()
    app.mainloop()