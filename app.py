from fastapi import FastAPI
from services.fedex import track_fedex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Shopping Assistant Running"}

@app.get("/track/{tracking_number}")
def track(tracking_number: str):
    return track_fedex(tracking_number)
