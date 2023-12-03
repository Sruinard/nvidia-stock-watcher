import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging
from logging import StreamHandler
import sys

logger = logging.getLogger(__name__)
# create a handler and add it to the logger
handler = StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
# set log level
logger.setLevel(logging.INFO)


class Task:
    def is_success(self):
        raise NotImplementedError


class Nvidia4090Available(Task):
    def __init__(self, url) -> None:
        super().__init__()
        self.url = url

    def get_static_content(self):
        logger.info("Retrieving static content...")
        # Set up Chrome options for headless browsing with a custom user-agent
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

        # Create a new WebDriver instance for each call
        with webdriver.Chrome(options=chrome_options) as driver:
            # Open the website in the browser
            driver.get(self.url)

            # Wait for the page to load
            time.sleep(5)

            # Get the page source after JavaScript has rendered the content
            page_source = driver.page_source

        logger.info("Retrieving static content done.")
        return page_source

    def _product_available(self):
        page_content = self.get_static_content()
        soup = BeautifulSoup(page_content, "html.parser")
        product_to_search_for = "NVGFT490"

        # find div with class NVGFT490
        nvidia4090 = soup.find("div", class_=product_to_search_for)
        if nvidia4090 is None:
            return None

        # load text from div as json
        nvidia4090 = json.loads(nvidia4090.text)[0]
        if nvidia4090.get("productTitle") == product_to_search_for:
            logger.info("Found product %s", product_to_search_for)
            if nvidia4090.get("productIsAvailable") == True:
                logger.info("Product is available")
                return True
            logger.info("Product is not available")
            return False
        logger.info("Product not found")
        return False

    def extract_stock_from_url(self, url):
        pass

    def is_success(self):
        product_available = self._product_available()
        return product_available


class Scraper:
    def do_task(self, task: Task):
        return task.is_success()
