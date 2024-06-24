import cv2
import numpy as np
import pyautogui
import time
import logging
import keyboard

# Configuration
pyautogui.PAUSE = 0.003
IMAGE_PATH = './images2/image2.PNG'
LOWER_PINK = np.array([140, 50, 50])
UPPER_PINK = np.array([170, 255, 255])
CLICK_COUNT = 13

# Image paths
FIGHT_PATH = './images2/fight.PNG'
RANDOM_PATH = './images2/random.PNG'
NEW_GAME_PATH = './images2/newgame.PNG'
STARTING_PATH = './images2/starting.PNG'
SHARE_PATH = './images2/share.PNG'
SUPERKICK_PATH = './images2/superkick.PNG'
SWORD_PATH = './images2/sword.PNG'
SHIELD_PATH = './images2/shield.PNG'
END_PATH = './images2/end.PNG'
TIME1_PATH = './images2/time1.PNG'
TIME2_PATH = './images2/time2.PNG'

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global control variables
paused = False
running = True

# Capture screen function
def capture_screen(region=None):
    try:
        screenshot = pyautogui.screenshot(region=region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame
    except Exception as e:
        logging.error(f"Failed to capture screen: {e}")
        return None

# Find pink circle function
def find_pink_circle(frame):
    try:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWER_PINK, UPPER_PINK)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        max_contour = max(contours, key=cv2.contourArea) if contours else None
        if max_contour is not None:
            (x, y), radius = cv2.minEnclosingCircle(max_contour)
            if radius > 10:
                return int(x), int(y), int(radius)
        return None, None, None
    except Exception as e:
        logging.error(f"Error in find_pink_circle: {e}")
        return None, None, None

# Click pink circle function
def click_pink_circle():
    frame = capture_screen()
    if frame is None:
        return

    x, y, radius = find_pink_circle(frame)
    if x is not None and y is not None:
        end_time = time.time() + 3.225  # Click for 3.225 seconds
        while time.time() < end_time:
            for _ in range(CLICK_COUNT):
                pyautogui.mouseDown(x, y)
                time.sleep(0.1)
                pyautogui.mouseUp(x, y)
        logging.info(f"Clicked {CLICK_COUNT} times repeatedly at position ({x}, {y}) for 3.225 seconds.")
    else:
        logging.warning("Pink circle not found.")

# Find and click image function with error handling
def find_and_click_image(image_path, confidence=0.8):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location is not None:
            pyautogui.click(location)
            logging.info(f"Clicked on {image_path}")
            return True
        logging.warning(f"Image {image_path} not found on screen.")
        return False
    except pyautogui.ImageNotFoundException:
        logging.warning(f"Image {image_path} not found on screen.")
        return False
    except Exception as e:
        logging.error(f"Error in find_and_click_image for {image_path}: {e}")
        return False

# Pause/Continue handler
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        logging.info("Script paused.")
    else:
        logging.info("Script continued.")

# Exit handler
def exit_script():
    global running
    running = False
    logging.info("Exiting script.")

# Keyboard listener thread
def keyboard_listener():
    global running
    while running:
        if keyboard.is_pressed('esc'):
            exit_script()
        if keyboard.is_pressed('space'):
            toggle_pause()
        time.sleep(0.1)

# Main function
def main():
    import threading
    listener_thread = threading.Thread(target=keyboard_listener, daemon=True)
    listener_thread.start()

    if find_and_click_image(FIGHT_PATH):
        logging.info("Clicked on fight.PNG")
    time.sleep(1)  # Wait for 1 second

    if find_and_click_image(RANDOM_PATH):
        logging.info("Clicked on random.PNG")
    time.sleep(1)  # Wait for 1 second

    if find_and_click_image(NEW_GAME_PATH):
        logging.info("Clicked on newgame.PNG")
    time.sleep(1)  # Wait for 1 second

    while True:
        try:
            if pyautogui.locateCenterOnScreen(STARTING_PATH, confidence=0.8):
                break
            time.sleep(0.5)  # Wait for starting.PNG
        except pyautogui.ImageNotFoundException:
            logging.warning("starting.PNG not found on screen.")

    logging.info("Detected starting.PNG, starting pink circle clicks.")
    
    while running:
        if not paused:
            try:
                if pyautogui.locateCenterOnScreen(TIME1_PATH, confidence=0.8) or pyautogui.locateCenterOnScreen(TIME2_PATH, confidence=0.8):
                    logging.info("Detected time1.PNG or time2.PNG, searching for sword.PNG or shield.PNG.")
                    if find_and_click_image(SWORD_PATH) or find_and_click_image(SHIELD_PATH):
                        logging.info("Clicked on sword.PNG or shield.PNG")
                        time.sleep(1)  # Small delay after clicking sword or shield
            except pyautogui.ImageNotFoundException:
                logging.warning("time1.PNG or time2.PNG not found on screen.")

            if find_and_click_image(SUPERKICK_PATH):
                logging.info("Detected superkick.PNG, pausing pink circle clicks.")
                continue

            if find_and_click_image(SHARE_PATH):
                logging.info("Detected share.PNG, pausing pink circle clicks and searching for newgame.PNG.")
                while True:
                    try:
                        if find_and_click_image(NEW_GAME_PATH):
                            logging.info("Clicked on newgame.PNG, waiting for starting.PNG.")
                            while True:
                                try:
                                    if pyautogui.locateCenterOnScreen(STARTING_PATH, confidence=0.8):
                                        logging.info("Detected starting.PNG, resuming pink circle clicks.")
                                        break
                                    time.sleep(0.5)  # Wait for starting.PNG
                                except pyautogui.ImageNotFoundException:
                                    logging.warning("starting.PNG not found on screen.")
                            break
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        logging.warning("newgame.PNG not found on screen.")
                continue

            click_pink_circle()
            time.sleep(0.1)  # Small delay to prevent high CPU usage
        else:
            time.sleep(0.1)  # Small delay when paused to prevent high CPU usage

if __name__ == "__main__":
    main()
