from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import time

# Ask user for the product to search
search_term = input("Enter the product you want to search for: ")

# Base URL for search
base_url = f'https://www.newegg.com/p/pl?d={search_term}&N=4131'

# Setup Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Automatically install and use the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the page
driver.get(base_url)
print("Page loaded successfully.")

# Wait for product listings to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item-container")))

# Get total number of pages
try:
    pagination_text = driver.find_element(By.CLASS_NAME, "list-tool-pagination-text").text
    total_pages = int(pagination_text.split("/")[-1]) if "/" in pagination_text else 1
except:
    total_pages = 1  # Default to 1 if pagination is not found

items_found = []

# Loop through all pages
for page in range(1, total_pages + 1):
    page_url = f'https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}'
    driver.get(page_url)
    
    # Wait for items to load
    time.sleep(3)  # Allow dynamic content to load
    
    # Find all product listings
    items = driver.find_elements(By.CLASS_NAME, "item-container")

    if not items:
        print(f"No items found on page {page}.")  # Debug statement for empty pages

    for item in items:
        try:
            title_tag = item.find_element(By.CLASS_NAME, "item-title")
            price_tag = item.find_element(By.CLASS_NAME, "price-current")
            link = title_tag.get_attribute("href")

            title = title_tag.text.strip()
            price = int(price_tag.find_element(By.TAG_NAME, "strong").text.replace(",", ""))

            print(f"Found item: {title} - ${price}")  # Debug statement

            items_found.append({"Title": title, "Price": price, "Link": link})
        except:
            print("Skipping item due to missing details.")
            continue

# Close Selenium driver
driver.quit()

# Check if any items were found
if not items_found:
    print("No valid items found.")
else:
    print(f"Found {len(items_found)} items.")

# Save data to Excel file
df = pd.DataFrame(items_found)

if not df.empty:
    file_name = f"{search_term}_results.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data has been saved to {file_name}")
    os.startfile(file_name)  # Open the Excel file
else:
    print("No data to save.")
