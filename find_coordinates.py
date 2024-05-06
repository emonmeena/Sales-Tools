import pyautogui
import time

try:
    while True:
        # Prints the current mouse coordinates
        x, y = pyautogui.position()
        print(f"Current position: X={x} Y={y}", end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDone")
