import csv  # Import the csv module
import tkinter as tk   # Import the tkinter module as "tk"  used to create GUI
# Multipurpose Internet Mail Extensions, which is a standard for formatting files to be sent via email
from email.mime.application import MIMEApplication
from tkinter import messagebox    # Import messagebox from tkinter
import smtplib    # Simple Mail Transfer Protocol - connect to an SMTP server and send an email message
from email.mime.multipart import MIMEMultipart  # Import MIMEMultipart class from email.mime.multipart module
from email.mime.text import MIMEText   # Import MIMEText class from email.mime.text module
from tkinter import filedialog   # Import filedialog from tkinter


class EmailMarketingBot(tk.Frame):
    def __init__(self, master=None):   # __init__ method is a constructor that initializes the object's state
        super().__init__(master)
        self.master = master
        self.master.title("Email Marketing Bot")   # title of the main window
        self.pack()  # packs the main window into its parent widget

        self.sender_label = tk.Label(self, text="Sender Email Address:")   # label to enter email address
        self.sender_label.pack()
        self.sender_entry = tk.Entry(self)    # allows the user to enter email address
        self.sender_entry.pack()

        self.password_label = tk.Label(self, text="Sender Email Password:")   # label to enter email password
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")    # allows the user to enter email password
        self.password_entry.pack()

        self.subject_label = tk.Label(self, text="Email Subject:")    # label to enter email subject
        self.subject_label.pack()
        self.subject_entry = tk.Entry(self)   # allows the user to enter email subject
        self.subject_entry.pack()

        self.message_label = tk.Label(self, text="Email Message:")   # label to enter email message
        self.message_label.pack()
        self.message_entry = tk.Text(self)   # allows the user to enter email message
        self.message_entry.pack()

        # Attachments Input
        tk.Label(self.master, text="Attachments").pack()
        self.attachment_button = tk.Button(self.master, text="Add Attachment", command=self.add_attachment)
        self.attachment_button.pack()

        # CSV Input
        tk.Label(self.master, text="Email Recipients CSV").pack()
        self.csv_button = tk.Button(self.master, text="Select CSV file", command=self.open_csv)
        self.csv_button.pack()

        self.send_button = tk.Button(self, text="Send Email", command=self.send_email)
        self.send_button.pack()

        self.files = []   # Create an empty list to store file attachments

    def send_email(self):
        email_sender = self.sender_entry.get()   # Get the sender email address
        email_password = self.password_entry.get()  # Get the sender email password
        email_subject = self.subject_entry.get()   # Get the email subject
        email_message = self.message_entry.get("1.0", "end")  # Get the email message

        try:    # Connect to the SMTP server
            smtp = smtplib.SMTP('smtp.gmail.com', 587)         #sets up SMTP server (GMAIL smtp server) and logs in with
                                                               # sender's email and pass
            smtp.starttls()   # Start TLS encryption
            smtp.login(email_sender, email_password)    # Login to the SMTP server

            with open(self.csv_file, newline='') as csvfile:   # Open the CSV file containing email recipients
                reader = csv.reader(csvfile)                    # Create a CSV reader object
                email_recipients = [row[0] for row in reader]   # Extract email addresses from the CSV file

            for email_recipient in email_recipients:             #loops through each email recipient and sets up the
                # Create a message object                                              #email message with specified subject,message and attachments
                msg = MIMEMultipart()
                msg['From'] = email_sender   # Set the email sender
                msg['To'] = email_recipient   # Set the email recipient
                msg['Subject'] = email_subject   # Set the email subject
                msg.attach(MIMEText(email_message, 'plain'))   # Add the email message

                # Attach the files to the email
                for file in self.files:
                    with open(file, 'rb') as f:
                        attachment = MIMEApplication(f.read(), _subtype='pdf')
                        attachment.add_header('Content-Disposition', 'attachment', filename=file)
                        msg.attach(attachment)

                smtp.sendmail(email_sender, email_recipient, msg.as_string())

            messagebox.showinfo("Success", "Email sent successfully.")
            smtp.quit()

        except smtplib.SMTPAuthenticationError:                                     #handles the errors while email sending
                                                                                    #processes like invalid user/pass
            messagebox.showerror("Authentication Error", "Invalid username or password.")
        except:
            messagebox.showerror("Error", "Failed to send email.")

    def add_attachment(self):
        attachment = filedialog.askopenfilename()

        self.files.append(attachment)

    def open_csv(self):
        self.csv_file = filedialog.askopenfilename()

#the add attachment and open_csv file methods are called when the user clicks on "add attachments" or "open csv file"
#buttons,respectively. They open a file dialog box to allow the user to select the desired file.

root = tk.Tk()
app = EmailMarketingBot(master=root)   #this code initializes the GUI and starts the programm running.
app.mainloop()