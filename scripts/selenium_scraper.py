### selenium_scraper.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from scripts.error_handling import handle_error

# Selenium Configuration
def scrape_trending_topics(proxy=None):
    options = webdriver.ChromeOptions()
    if proxy:
        options.add_argument(f"--proxy-server={proxy}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://twitter.com/login")

    try:
        # Log in to Twitter
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "session[username_or_email]")))
        username = driver.find_element(By.NAME, "session[username_or_email]")
        password = driver.find_element(By.NAME, "session[password]")

        username.send_keys("your_username")
        password.send_keys("your_password")
        password.send_keys(Keys.RETURN)

        # Wait for login to complete
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='What\u2019s happening']")))

        # Scrape trending topics
        trends = []
        trend_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@aria-label='Timeline: Trending now']//span"))
        )
        for element in trend_elements[:5]:
            trends.append(element.text)

        # Get IP Address for the request
        ip_address = driver.execute_script("return window.navigator.connection")

        # Save to MongoDB
        store_to_mongo(trends, ip_address)

    except Exception as e:
        handle_error(e)
    finally:
        driver.quit()


def store_to_mongo(trends, ip_address):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["twitter_trends"]
    collection = db["trends"]

    data = {
        "trends": trends,
        "ip_address": ip_address,
        "timestamp": time.time()
    }

    collection.insert_one(data)

if __name__ == "__main__":
    scrape_trending_topics()