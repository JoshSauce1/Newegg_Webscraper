from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

# Ask user for the product to search
search_term = input("Enter the product you want to search for: ")

# Base URL for search
base_url = f'https://www.newegg.com/p/pl?d={search_term}&N=4131'

# Setup Chrome options
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

# Start Chrome using undetected_chromedriver
driver = uc.Chrome(options=options, use_subprocess=True)

# Open the search page
driver.get(base_url)
print("Page loaded successfully.")

# Wait for the first batch of results
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "item-container")))

# Get total pages
try:
    pagination_text = driver.find_element(By.CLASS_NAME, "list-tool-pagination-text").text
    total_pages = int(pagination_text.split("/")[-1]) if "/" in pagination_text else 1
except:
    total_pages = 1

items_found = []

# Scrape product data
for page in range(1, total_pages + 1):
    page_url = f'https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}'
    driver.get(page_url)
    time.sleep(3)

    items = driver.find_elements(By.CLASS_NAME, "item-container")
    if not items:
        print(f"No items found on page {page}.")
        continue

    for item in items:
        try:
            title_tag = item.find_element(By.CLASS_NAME, "item-title")
            price_tag = item.find_element(By.CLASS_NAME, "price-current")
            link = title_tag.get_attribute("href")
            title = title_tag.text.strip()
            price = int(price_tag.find_element(By.TAG_NAME, "strong").text.replace(",", ""))

            print(f"Found item: {title} - ${price}")
            items_found.append({"Title": title, "Price": price, "Link": link})
        except:
            print("Skipping item due to missing details.")
            continue

# Close the browser
driver.quit()

# Analyze and export data
if items_found:
    df = pd.DataFrame(items_found)
    df.dropna(inplace=True)
    df['Brand'] = df['Title'].str.split().str[0]

    file_name = f"{search_term}_results.xlsx"
    df.to_excel(file_name, index=False)
    print(f"\n✅ Data has been saved to {file_name}")

    # Insights
    print("\n📊 Quick Analysis:")
    print(f"Average Price: ${df['Price'].mean():,.2f}")
    print("\nTop 5 Most Expensive Items:")
    print(df.sort_values(by='Price', ascending=False).head(5)[['Title', 'Price']])

    # Visualization
    top_brands = df['Brand'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    top_brands.plot(kind='bar', color='skyblue')
    plt.title("Top 10 Brands by Number of Listings")
    plt.xlabel("Brand")
    plt.ylabel("Listings Count")
    plt.tight_layout()
    plt.show()
else:
    print("❌ No valid items found.")
