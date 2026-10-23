# Pre-requisite for Asynchrouns execution
# install  pytest-asyncio
# command:   pip install pytest-asyncio

from playwright.async_api import async_playwright,Page, expect
import pytest


from playwright.async_api import async_playwright, expect
import pytest


@pytest.mark.asyncio
async def test_verifyPageUrl_async():

    async with async_playwright() as p:

        # Launch Chromium in headed mode
        browser = await p.chromium.launch(headless=False)

        try:
            # Open a new browser page
            mypage = await browser.new_page()

            # Navigate to the website
            await mypage.goto(
                "https://demowebshop.tricentis.com/"
            )

            # Verify the page URL
            await expect(mypage).to_have_url(
                "https://demowebshop.tricentis.com/"
            )

        finally:
            # Close the browser even if the assertion fails
            await browser.close()


