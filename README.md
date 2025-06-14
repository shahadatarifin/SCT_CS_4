# 🛡️ Basic Keylogger (For Educational Purposes Only)

> ⚠️ **Disclaimer**: This keylogger is built strictly for educational and ethical learning purposes. Do not use this tool for unauthorized monitoring or in violation of privacy laws.

---

## 🎯 Task Objective

The objective of this project is to develop a **basic keylogger** in Python that records user keystrokes to a log file. This is meant to help understand how keylogging works and to raise awareness about potential security risks.

---

## ⚙️ Approach

The keylogger is implemented using the `keyboard` module in Python. Here's how it works:

1. Captures all key press events using a listener.
2. Logs each key to a specified file (`keylog.txt` by default).
3. Handles special keys like `space`, `enter`, and others for readability.
4. Runs in the background using a thread, allowing the user to stop it with the `Enter` key.

The use of threading allows the keylogger to run continuously while keeping the main program responsive.

---

## 🧰 Tools Used

- **Python**: Core language for implementation
- **keyboard**: For capturing real-time key press events
- **threading**: To run the keylogger in the background
- **datetime**: (Imported but unused, could be used for timestamps)
- **time**: To keep the keylogger active in a loop

---

## 📚 What I Learned

- How to use the `keyboard` module to detect and respond to keyboard input.
- Writing background processes using Python's `threading`.
- Handling user inputs and logging data to a file.
- Basic ethical considerations around keylogging and digital privacy.
- How special characters and system keys differ from regular input characters.

---

## 🚀 How to Run

### 1. Install required package:
```bash
pip install keyboard
