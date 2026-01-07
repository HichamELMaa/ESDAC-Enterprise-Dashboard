import oracledb
import os
from dotenv import load_dotenv

# 1. Load secrets immediately
load_dotenv()

# 2. Define the "Recipe" (The Function)
# (Notice this is NOT indented. It touches the left wall)
def connect_to_oracle():
    try:
        # Step A: Get the Key
        password = os.getenv("DB_PASSWORD")
        user = os.getenv("DB_USER")
        dsn = os.getenv("DB_DSN")

        # Step B: Open the Door
        connection = oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        print("Success: Connected to HR Database")
        return connection
        
    except oracledb.Error as e:
        print(f"Error: {e}")
        return None


# 3 Query Function
def test_hr_data():
    conn = connect_to_oracle()

    # SAFETY CHECK: Only proceed if conn is NOT None
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name FROM employees FETCH FIRST 5 ROWS ONLY")
        rows = cursor.fetchall()
        for row in rows:
            print (f"Employee: {row}")
        cursor.close()
        conn.close()
    else:
        print("Skipping query because connection failed.")


# 4. The "Trigger" (Cook the Meal)
# Only run this if we execute the file directly
if __name__ == "__main__":
    test_hr_data()