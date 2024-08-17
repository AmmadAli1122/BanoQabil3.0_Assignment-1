import requests
import smtplib
from datetime import datetime, timedelta

SHEETY_API_URL = "https://api.sheety.co/9557311ab04759c8ec506992150d74af/eventRemainder/sheet1"

def fetch_events():
    response = requests.get(SHEETY_API_URL)
    if response.status_code == 200:
        data = response.json()
        print("Fetched Data:", data)  
        return data.get('sheet1', [])
    else:
        print("Failed to fetch events:", response.text)
        return []

def send_reminder_email(to_address, event):
    from_address = "starxammad@example.com"
    password = "isvt eusi tdtt msmn"   
    subject = f"Reminder: {event['event_name']} on {event['date']}"
    body = f"Dear {event['recipient_name']},\n\nThis is a reminder for the upcoming event:\n\nEvent: {event['event_name']}\nDate: {event['date']}\n\n{event['message']}"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, message)
        print(f"Reminder email sent to {to_address} for {event['event_name']}")

def should_send_reminder(event):
    event_date = datetime.strptime(event['date'], "%Y-%m-%d")
    reminder_days = int(event.get('reminder_days',7))
    reminder_date = event_date - timedelta(days=reminder_days)
    return datetime.now().date() >= reminder_date.date()

if __name__ == "_main_":
    events = fetch_events()
    for event in events:
        if should_send_reminder(event):
            send_reminder_email(event['email'], event)


