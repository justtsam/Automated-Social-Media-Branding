import csv
import os

# Get the desktop path
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
csv_filename = os.path.join(desktop_path, 'email_list.csv')

# Define the list of email addresses
email_list = ['gkawad10@gmail.com', 'ssmnwc16054@gmail.com']

# Open the CSV file in write mode and write the email addresses
with open(csv_filename, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for email in email_list:
        writer.writerow([email])
