import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
WHATSAPP_FROM = "whatsapp:+14155238886"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

FEDEX_API_KEY = os.getenv("FEDEX_API_KEY")
