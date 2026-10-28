from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.britishairways.com/nx/b/airselect/en/gbr/book/search/?from=DCA&to=EAS&departureDate=2026-10-31&adults=1&youngAdults=0&children=0&infants=0&travelClass=economy&trip=oneWay&bound=outbound",
        wait_until="domcontentloaded",
    )

    print("Page title:", page.title())

    page.screenshot(path="browser_page.png")

    browser.close()