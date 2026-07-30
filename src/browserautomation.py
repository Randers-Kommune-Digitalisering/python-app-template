import time
from selenium import webdriver
from playwright.sync_api import sync_playwright

from utils.config import SELENIUM_URL, BROWSERLESS_URL


def test_selenium():
    print(f"Starting Selenium test with SELENIUM_URL: {SELENIUM_URL}")

    driver = webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=webdriver.ChromeOptions(),
    )

    print(f"Session acquired: {driver.session_id}")

    driver.get("https://example.com")
    print("Title:", driver.title)

    time.sleep(60)

    driver.quit()

    print("Selenium test completed for session")


def test_playwright_browserless():
    print(f"Starting Playwright Browserless test with BROWSERLESS_URL: {BROWSERLESS_URL}")

    with sync_playwright() as p:

        browser = p.chromium.connect(
            BROWSERLESS_URL
        )

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://example.com")

        print("Title:", page.title())

        time.sleep(60)

        browser.close()

        print("Playwright Browserless test completed for session")
