# 🐾 Advanced Keylogger with Cat Game Overlay (Educational Tool)

> ⚠️ **DISCLAIMER**  
> This project is strictly for **educational and ethical research purposes only**. Unauthorized or malicious use is illegal and unethical. Always obtain **explicit permission** before deploying or testing such software in any environment.

---

## 🎯 Overview

This project simulates a realistic malware scenario, designed to educate students, researchers, and cybersecurity professionals on how keyloggers operate — with an added twist: a **Cat Game overlay** to distract users while data is collected silently in the background.

---

## 🛡️ Features

- 🎹 **Keystroke Logging** – Records all keyboard inputs.
- 🖼️ **Screenshot Capture** – Takes screenshots every second.
- 🖥️ **System Information Retrieval** – Gathers OS and hardware details.
- 📋 **Clipboard Monitoring** – Logs contents copied to clipboard.
- 📧 **Email Exfiltration** – Sends encrypted logs to a configured email address.
- 🕹️ **Cat Game Overlay** – Chrome Dino-style cat game to distract users.

---

## 🔍 How It Works

1. Runs invisibly, logging keystrokes and clipboard activity.
2. Captures screenshots in real-time.
3. Retrieves detailed system and environment info.
4. Encrypts all data and emails it periodically.
5. Meanwhile, a fullscreen cat game runs to keep the user engaged.

---

## ⚙️ Requirements

- Python 3.7 or higher
- Install dependencies:
  ```bash
  pip install pynput pyautogui pygame
