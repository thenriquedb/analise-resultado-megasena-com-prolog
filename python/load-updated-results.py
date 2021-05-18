import asyncio
from pyppeteer import launch

uri = 'https://redeloteria.com.br/mega-sena/todos-os-resultados-da-mega-sena'


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(uri)

    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
