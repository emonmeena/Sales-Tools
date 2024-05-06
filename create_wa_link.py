import csv
import urllib.parse


def create_whatsapp_links(input_csv, output_csv):
    # Define the message and the template URL
    message = "Hello there,\nI am Someone. Got your contact from somewhere.\nJust wanted to network with you. I am a co-founder at a startup based in somewhere.\nMay I know a bit about you to break the ice XD?"
    encoded_message = urllib.parse.quote(message)
    template_url = f"https://web.whatsapp.com/send?phone={{}}&text={encoded_message}"

    # Read the first line of the CSV to get the numbers
    with open(input_csv, "r") as file:
        reader = csv.reader(file)
        numbers = next(reader)  # Assumes numbers are in the first row

    # Prepare data for the new CSV
    rows = [["number", "link", "ice-breaking"]]
    for number in numbers:
        link = template_url.format(number.strip())
        rows.append([number, link])

    # Write the data to a new CSV file
    with open(output_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


# Example usage
create_whatsapp_links("degree_1_connections_a.csv", "contacts_with_links.csv")
