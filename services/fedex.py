import requests

def track_fedex(tracking_number):
    url = "https://apis.fedex.com/track/v1/trackingnumbers"

    headers = {
        "Authorization": "Bearer YOUR_FEDEX_TOKEN",
        "Content-Type": "application/json"
    }

    payload = {
        "trackingInfo": [{
            "trackingNumberInfo": {
                "trackingNumber": tracking_number
            }
        }]
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
