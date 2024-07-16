
import smtplib
import pandas as pd 
from datetime import datetime

# SMTP email server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "starxammad@gmail.com"
GMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"

def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def check_and_send_wishes():
    today = datetime.today()
    dayName = today.strftime("%A")


    # Read the birthday CSV file
    fileData = pd.read_csv("index.csv")

    for index, row in fileData.iterrows():
        if dayName=="Tuesday":
            name = row["name"]
            email = row["email"]
            subject = "Quotes..!"
            message = row["quotes"]
            send_email(email, subject, message)

if __name__ == "__main__":
    check_and_send_wishes()