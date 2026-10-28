import pyautogui
import time

print("Starting mouse automation...")

print("Screen width:", pyautogui.size().width)
print("Screen height:", pyautogui.size().height)

pyautogui.moveTo(500, 300, duration=1)  # Move the mouse to (500, 300) over 1 second
pyautogui.moveTo(800, 450, duration=2)  # Move the mouse to (800, 450) over 2 seconds
pyautogui.moveTo(200, 600, duration=1.5)  # Move the mouse to (200, 600) over 1.5 seconds
pyautogui.moveTo(400, 200, duration=1)  # Move the mouse to (400, 200) over 1 second

pyautogui.click()  # Perform a mouse click at the current position

time.sleep(2)  # Wait for 2 seconds

screenshot = pyautogui.screenshot()  # Take a screenshot of the current screen
screenshot.save("screenshot.png")  # Save the screenshot as "screenshot.png"

print("Screenshot saved as 'screenshot.png'.")