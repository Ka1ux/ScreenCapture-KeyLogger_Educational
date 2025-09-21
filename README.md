# Screen Capture & Key Logger (Educational)

**⚠️ Disclaimer:** This project is for **educational purposes only**. Do **not** use it to capture data from other people without permission. Only test on your own computer.

---

## Description

This Python script runs in the background and provides two main functionalities:

1. **Key Logger (Legal)** – captures the keys typed on your own machine and saves them into a text file.
2. **Screen Capture** – takes a screenshot of your desktop every few seconds and saves it with a timestamp.

The script also generates a **status log** so you can track the script's activity.

---

## Features

* Runs in the background without opening a console window (`.pyw`)
* Records letters, numbers, spaces, and Enter key
* Captures screenshots every 2 seconds by default
* Saves files in organized folders (`prints/` for screenshots, `logs/` for activity)
* Timestamped filenames prevent overwriting of files
* Logging system shows key presses and screenshot activity

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

2. Navigate to the project folder:

```bash
cd YOUR_REPOSITORY
```

3. Install required Python libraries:

```bash
pip install pynput pyautogui
```

---

## Usage

### Run with console (for testing)

```bash
python my_app.py
```

You can see console logs confirming screenshots and key presses.

### Run in background (no console)

```bash
python my_app.pyw
```

* The script will run silently in the background.
* Screenshots will be saved in `prints/`.
* Key logs will be saved in `keylogs.txt`.
* Activity logs will be saved in `logs/status.log`.

---

## Configuration

* **Screenshot interval:** Adjust `time.sleep(2)` in the script to change the screenshot frequency.
* **Folders:** Ensure `prints/` and `logs/` exist; the script will create them automatically if they do not.

---

## Notes

* This project is **for learning and experimentation only**.
* Do **not** deploy it on someone else’s machine without consent.
* Test safely on your own computer.
