import csv
import webbrowser
import time
import urllib.parse
import subprocess
import pyautogui


def click_at(x, y):
    # Moves the mouse to the specific coordinates
    pyautogui.moveTo(x, y)
    # Performs a mouse click at the current location
    pyautogui.click()


def close_brave():
    script = 'tell application "Brave Browser" to quit'
    try:
        subprocess.run(["osascript", "-e", script], check=True)
        print("Brave browser has been quit successfully.")
    except subprocess.CalledProcessError:
        print("Failed to quit Brave browser.")


def open_urls_and_update_csv(file_path):
    # Define the message and the template URL

    message = "Hello there,\nI am Emon (IIT Roorkee CSE '23 batch). Got your contact from the IITRAA community.\nJust wanted to network with you. I am a co-founder at a startup based in GGN.\nMay I know a bit about you to break the ice XD?"
    encoded_message = urllib.parse.quote(message)
    template_url = f"https://web.whatsapp.com/send?phone={{}}&text={encoded_message}"

    # Read the existing data
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Convert iterator to a list to process and write back

    # Initialize fieldnames for writing
    fieldnames = reader.fieldnames
    if "link" not in fieldnames:
        fieldnames.append("link")
    if "ice-breaking" not in fieldnames:
        fieldnames.append("ice-breaking")

    # Process each URL
    updated_rows = []
    count = 0
    for row in rows:
        # Generate and update the link if necessary
        if "number" in row and row["number"]:
            row["link"] = template_url.format(row["number"].strip())

        # Skip rows already marked as done
        if row.get("ice-breaking") == "Done":
            updated_rows.append(row)
            continue

        # Open URL in default browser
        webbrowser.open(row["link"])
        # Assume successful opening as "Done"

        updated_rows.append(row)
        # Write the updated data to the CSV file after each operation
        with open(file_path, mode="w", newline="") as wfile:
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        # Wait for 20 seconds before the next operation
        time.sleep(21)
        # Replace these coordinates with the location where you want to click
        x_coordinate = 1650
        y_coordinate = 1063

        click_at(x_coordinate, y_coordinate)

        row["ice-breaking"] = "Done"
        count += 1

        if count > 30:
            count = 0
            close_brave()
            time.sleep(5)


# Example usage
open_urls_and_update_csv("contacts_with_links.csv")
