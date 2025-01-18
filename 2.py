import os
from datetime import datetime, timezone
import pyautogui
from playsound import playsound  # Ensure playsound is installed

def capture_screenshot():
    # Get the current UTC date in the format MM-DD-YYYY
    current_utc_date = datetime.now(timezone.utc).strftime("%m-%d-%Y")
    
    # Define the path for the forexjournal folder and date-based subfolder
    base_folder = r"C:\forexjournal"
    date_folder = os.path.join(base_folder, current_utc_date)
    
    # Create the folders if they do not exist
    os.makedirs(date_folder, exist_ok=True)
    
    # Define the file name for the screenshot
    file_name = datetime.now().strftime("%H-%M-%S") + ".png"  # File name: 14-30-45.png
    screenshot_file = os.path.join(date_folder, file_name)
    
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot to the defined file
    screenshot.save(screenshot_file)
    
    print(f"Screenshot saved at: {screenshot_file}")
    
    # Play a camera shutter sound
    try:
        playsound('./camera_shutter.mp3')  # Make sure the file exists at this path
    except Exception as e:
        print(f"Error playing sound: {e}")

# Call the function
capture_screenshot()
