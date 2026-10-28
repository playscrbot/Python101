import pyautogui as pg
import time
from datetime import datetime
from urllib.parse import urlparse

pg.FAILSAFE = True
pg.PAUSE = 0.3

def open_website(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        print("Please enter a valid HTTP or HTTPS URL.")
        return

    print(f"Opening {url}...")
    pg.hotkey("ctrl", "l")
    pg.write(url, interval=0.02)
    pg.press("enter")
    time.sleep(3)


def type_text(text):
    pg.write(text, interval=0.02)


def click(x, y):
    width, height = pg.size()

    if not (0 <= x < width and 0 <= y < height):
        print(f"Coordinates must be within {width} x {height}.")
        return

    pg.click(x, y)


def press_key(key):
    allowed_keys = {
        "enter", "tab", "esc", "space",
        "backspace", "delete", "up", "down",
        "left", "right", "home", "end",
        "pageup", "pagedown"
    }

    if key.lower() not in allowed_keys:
        print("That key is not supported by this menu.")
        return

    pg.press(key.lower())


def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"office_screenshot_{timestamp}.png"

    pg.screenshot().save(filename)
    print(f"Screenshot saved as {filename}")


def wait_seconds(seconds):
    if not 0 <= seconds <= 300:
        print("Choose a wait time between 0 and 300 seconds.")
        return

    print(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)

def fill_office_form():
    print("\n--- Office Form Assistant ---")
    print("Example: customer forms, inventory records, or invoice entry.")
    print("Make sure the target application is open.")

    try:
        x = int(input("X coordinate of the first field: "))
        y = int(input("Y coordinate of the first field: "))
    except ValueError:
        print("Coordinates must be whole numbers.")
        return

    width, height = pg.size()

    if not (0 <= x < width and 0 <= y < height):
        print("Coordinates are outside the screen.")
        return

    fields = []

    while True:
        value = input(
            f"Enter value for field {len(fields) + 1} "
            "(blank to finish): "
        )

        if value == "":
            break

        fields.append(value)

    if not fields:
        print("No fields entered.")
        return

    print("\nReview the record:")
    for number, value in enumerate(fields, start=1):
        print(f"{number}. {value}")

    confirm = input(
        "\nClick the first field and fill this record? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Cancelled.")
        return

    print("Starting in 3 seconds. Switch to the target application.")
    time.sleep(3)

    pg.click(x, y)

    for index, value in enumerate(fields):
        pg.write(value, interval=0.02)

        if index < len(fields) - 1:
            pg.press("tab")

    print("\nRecord entered.")
    print("Review the fields manually before saving the record.")


def prepare_office_message():
    print("\n--- Standard Office Messages ---")
    print("1. Follow-up reminder")
    print("2. Meeting reminder")
    print("3. Document request")
    print("4. Custom message")

    choice = input("Choose a message: ").strip()

    if choice == "1":
        recipient = input("Recipient name: ").strip()
        message = (
            f"Hello {recipient},\n\n"
            "I am following up on the pending task. "
            "Please share an update when convenient.\n\n"
            "Thank you."
        )

    elif choice == "2":
        recipient = input("Recipient name: ").strip()
        meeting = input("Meeting date and time: ").strip()
        message = (
            f"Hello {recipient},\n\n"
            f"This is a reminder about our meeting scheduled for {meeting}.\n\n"
            "Thank you."
        )

    elif choice == "3":
        recipient = input("Recipient name: ").strip()
        document = input("Document name: ").strip()
        message = (
            f"Hello {recipient},\n\n"
            f"Could you please share the {document} when convenient?\n\n"
            "Thank you."
        )

    elif choice == "4":
        message = input("Enter your message: ")

    else:
        print("Invalid choice.")
        return

    print("\n--- Message Preview ---")
    print(message)

    confirm = input(
        "\nType this message into the currently focused field? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        type_text(message)
        print("Message typed. Review it before sending.")
    else:
        print("Cancelled.")


def office_shortcuts():
    print("\n--- Office Keyboard Shortcuts ---")
    print("1. Select all       (Ctrl+A)")
    print("2. Copy             (Ctrl+C)")
    print("3. Paste            (Ctrl+V)")
    print("4. Save             (Ctrl+S)")
    print("5. Find             (Ctrl+F)")
    print("6. Switch window    (Alt+Tab)")
    print("7. New browser tab  (Ctrl+T)")
    print("8. Undo             (Ctrl+Z)")

    shortcuts = {
        "1": ("ctrl", "a"),
        "2": ("ctrl", "c"),
        "3": ("ctrl", "v"),
        "4": ("ctrl", "s"),
        "5": ("ctrl", "f"),
        "6": ("alt", "tab"),
        "7": ("ctrl", "t"),
        "8": ("ctrl", "z"),
    }

    choice = input("Choose a shortcut: ").strip()

    if choice not in shortcuts:
        print("Invalid shortcut.")
        return

    if choice == "4":
        confirm = input(
            "Save the current document? Type yes to confirm: "
        ).strip().lower()

        if confirm != "yes":
            print("Cancelled.")
            return

    pg.hotkey(*shortcuts[choice])
    print("Shortcut executed.")

def task_assistant():
    while True:
        print("\n================================")
        print("       OFFICE TASK ASSISTANT")
        print("================================")
        print("1. Open website")
        print("2. Type text")
        print("3. Click screen position")
        print("4. Press a key")
        print("5. Take screenshot")
        print("6. Wait")
        print("7. Fill an office form")
        print("8. Prepare an office message")
        print("9. Office keyboard shortcuts")
        print("10. Exit")

        choice = input("\nChoose a task: ").strip()

        try:
            if choice == "1":
                url = input("Enter website URL: ").strip()
                open_website(url)

            elif choice == "2":
                text = input("Enter text to type: ")
                confirm = input(
                    "Type into the currently focused field? (yes/no): "
                ).strip().lower()

                if confirm == "yes":
                    type_text(text)

            elif choice == "3":
                x = int(input("Enter X coordinate: "))
                y = int(input("Enter Y coordinate: "))
                click(x, y)

            elif choice == "4":
                key = input("Enter key (e.g. tab, enter, esc): ")
                press_key(key)

            elif choice == "5":
                take_screenshot()

            elif choice == "6":
                seconds = float(input("Seconds to wait: "))
                wait_seconds(seconds)

            elif choice == "7":
                fill_office_form()

            elif choice == "8":
                prepare_office_message()

            elif choice == "9":
                office_shortcuts()

            elif choice == "10":
                print("Office Task Assistant stopped.")
                break

            else:
                print("Invalid choice. Try again.")

        except pg.FailSafeException:
            print("\nEmergency stop triggered.")
        except (ValueError, OSError) as error:
            print(f"Could not complete the task: {error}")


if __name__ == "__main__":
    task_assistant()