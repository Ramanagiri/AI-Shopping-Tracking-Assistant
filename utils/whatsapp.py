from twilio.rest import Client
from config import TWILIO_SID, TWILIO_AUTH, WHATSAPP_FROM

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_whatsapp(to, message):
    client.messages.create(
        body=message,
        from_=WHATSAPP_FROM,
        to=f"whatsapp:{to}"
    )
