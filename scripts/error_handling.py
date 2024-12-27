### error_handling.py
import time

def handle_error(error):
    with open("logs/error.log", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {str(error)}\n")
    print(f"Error logged: {error}")
