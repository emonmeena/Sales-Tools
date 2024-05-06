import pywhatkit
import datetime
import webbrowser


# Function to send a WhatsApp message
def send_message(phone_number, message):
    # Get the current time
    now = datetime.datetime.now()

    # Set the time for sending the message (current time + 2 minutes)
    hours = now.hour
    minutes = now.minute + 2

    # Adjust for cases where minutes exceed 60
    if minutes >= 60:
        minutes -= 60
        hours += 1

    # Send the message
    pywhatkit.sendwhatmsg(
        phone_number,
        message,
        hours,
        minutes,
        wait_time=20,
        tab_close=True,
        close_time=3,
    )


# List of phone numbers and their respective messages
contacts = [
    "+123456788",
    "+123455678",
]

# Sending messages to multiple contacts
message = "hi sent from python"
for phone in contacts:
    send_message(phone, message)
