from playwright.async_api import async_playwright

async def get_amazon_price(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url)

        try:
            price = await page.locator(".a-price-whole").first.inner_text()
        except:
            price = "Not Found"

        await browser.close()
        return price
