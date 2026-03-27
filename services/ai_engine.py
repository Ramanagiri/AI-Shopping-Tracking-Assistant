from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_deal(name, price):
    prompt = f"""
    Product: {name}
    Current Price: {price}

    Is this a good deal? Give short response.
    """

    res = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
