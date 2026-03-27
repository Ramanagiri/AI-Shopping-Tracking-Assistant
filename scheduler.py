import asyncio
from services.amazon import get_amazon_price
from services.ai_engine import analyze_deal
from utils.whatsapp import send_whatsapp

PRODUCT_URL = "https://www.amazon.in/dp/example"
USER_PHONE = "+91XXXXXXXXXX"

async def check_price():
    price = await get_amazon_price(PRODUCT_URL)

    analysis = analyze_deal("Sample Product", price)

    message = f"""
    🛍 Product Update

    Price: ₹{price}
    AI Insight: {analysis}
    """

    send_whatsapp(USER_PHONE, message)


async def run_scheduler():
    while True:
        await check_price()
        await asyncio.sleep(3600)  # every 1 hour

if __name__ == "__main__":
    asyncio.run(run_scheduler())
