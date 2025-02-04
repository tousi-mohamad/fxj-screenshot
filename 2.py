import os
import json
from datetime import datetime, timezone
import mss  # Import mss for accurate screen capture
from playsound import playsound

# Load config.json
CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"save_path": "C:\\forexjournal", "monitor": 1}  # Default values

config = load_config()

def capture_screenshot():
    # Get the current UTC date in the format MM-DD-YYYY
    current_utc_date = datetime.now(timezone.utc).strftime("%m-%d-%Y")

    # Define the path for the forexjournal folder and date-based subfolder
    base_folder = config["save_path"]
    date_folder = os.path.join(base_folder, current_utc_date)
    os.makedirs(date_folder, exist_ok=True)  # Create folders if they don't exist

    # Define the file name for the screenshot
    file_name = datetime.now().strftime("%H-%M-%S") + ".png"
    screenshot_file = os.path.join(date_folder, file_name)

    # Capture screenshot using MSS
    monitor_index = config.get("monitor", 1)  # Monitor numbers start from 1
    with mss.mss() as sct:
        monitors = sct.monitors  # List of available monitors
        if 1 <= monitor_index < len(monitors):
            screenshot = sct.grab(monitors[monitor_index])  # Capture specified monitor
        else:
            print(f"Invalid monitor number: {monitor_index}. Using primary monitor.")
            screenshot = sct.grab(monitors[1])  # Default to primary monitor

        # Save the screenshot
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=screenshot_file)

    print(f"Screenshot saved at: {screenshot_file}")

    # Play a camera shutter sound
    try:
        playsound('./camera_shutter.mp3')
    except Exception as e:
        print(f"Error playing sound: {e}")

# Call the function
capture_screenshot()
