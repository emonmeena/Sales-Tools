import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Email settings
smtp_server = ""
port = 111111111
username = ""
password = ""

# Email content
subject = "Subject"


def get_body(name, company):
    body = f"""
    <html>
        <body>
            frame accordingly
        </body>
    </html>
    """
    return body


# Read CSV file
csv_file = "email_all.csv"  # Path to your CSV file
mailing_list = pd.read_csv(csv_file)

# Set up the SMTP server
server = smtplib.SMTP(smtp_server, port)
server.starttls()  # Start TLS encryption
server.login(username, password)

# Send the emails
for index, row in mailing_list.iterrows():
    fullname = row["Name"]
    first_name = fullname.split()[0]  # Extract the first name
    company = row["Company"]
    recipient = row["Email"]
    cc_recipients = ["123@company.com", "123@123.com"]
    message = MIMEMultipart("related")
    message["From"] = f"ee <{username}>"
    message["To"] = recipient
    message["CC"] = ", ".join(cc_recipients)
    message["Subject"] = subject
    body_ = get_body(first_name, company)
    message.attach(MIMEText(body_, "html"))

    # Attach the image as an inline image
    with open("image.png", "rb") as image_file:
        img = MIMEImage(image_file.read())
        img.add_header("Content-ID", "<image>")  # Use Content-ID for inline image
        message.attach(img)

    server.sendmail(username, [recipient] + cc_recipients, message.as_string())
    print(f"Email sent to {recipient}")

# Close the SMTP server
server.quit()
