import pyautogui
import time

pyautogui.PAUSE = 1
time.sleep(10)

# ------- Typing with pyautogui -------

pyautogui.write("Hello World!")

# ------- Press with pyautogui -------

pyautogui.press("tab", presses=2)
pyautogui.press("enter")

time.sleep(10)

# ------- Hotkey with pyautogui -------

pyautogui.hotkey("ctrl", "a")
pyautogui.write("This is an automated message typed using pyautogui!")

time.sleep(10)

# ------- Keyboard shortcuts with pyautogui -------

# Click the first field
pyautogui.moveTo(800, 700)
pyautogui.click()

pyautogui.write("Turbo")

# Move to the next field
pyautogui.press("tab")
pyautogui.write("Max")

# Move to the next field
pyautogui.press("tab")
pyautogui.write("playscript007@gmail.com")

# Move to the next field
pyautogui.press("tab")
pyautogui.write("12345678")

print("Please check the fields.")

time.sleep(10)

# ------- Workflow with pyautogui -------

# Enter a simple report.
pyautogui.write("DAILY WORK SUMMARY\n")
pyautogui.write("------------------\n")
pyautogui.write("Files processed: 42\n")
pyautogui.write("Errors found: 2\n")
pyautogui.write("Status: Completed with warnings\n")

# Save the document using the Save As dialog.
pyautogui.hotkey("ctrl", "shift", "s")

# Give the dialog time to appear.
time.sleep(2)

# Enter a filename, assuming the dialog accepts filename input.
pyautogui.write("daily_summary.txt")
pyautogui.press("enter")

# Allow the application to finish saving.
time.sleep(2)

# Capture the resulting screen.
pyautogui.screenshot().save("workflow_result.png")

print("Automation sequence finished.")