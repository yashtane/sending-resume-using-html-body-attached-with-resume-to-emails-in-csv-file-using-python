import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Function to send an email with HTML body and resume attachment
def send_email(to_email, subject, html_body, resume_file_path):
    # Email configuration
    sender_email = "example@gmail.com"  # update your email
    sender_password = "your password"  # update your password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Adjust the port accordingly

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach HTML body
    msg.attach(MIMEText(html_body, "html"))

    # Attach resume file
    with open(resume_file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f'attachment; filename="{resume_file_path}"'
        )
        msg.attach(part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())


# Read email addresses from the CSV file
def read_email_addresses(csv_file):
    email_addresses = []
    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email_addresses.append(row[0])
    return email_addresses


# Define the HTML body for the email
html_body = """<html>
<head>This is for resume</head>
  
</html>)"""

# Path to the resume file
resume_file_path = "YASH_TANEJA_Resume.pdf"

# Read email addresses from the CSV file
csv_file_path = "cheker.csv"  # update your path
email_addresses = read_email_addresses(csv_file_path)

# Send email to each recipient
for email in email_addresses:
    send_email(email, "Job Application", html_body, resume_file_path)
    print(f"Email sent to: {email}")
