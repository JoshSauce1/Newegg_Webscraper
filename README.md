# 🖥️ Newegg Product Scraper & Price Analysis Dashboard

This project automates the collection and analysis of GPU product listings from [Newegg.com](https://www.newegg.com). It uses **Selenium** for scraping, **Pandas** for data wrangling, and **Matplotlib** for insights — then exports everything to an Excel report ready for business decisions.

---

## 📌 Features

- 🔍 **Search-based product scraping** (e.g., "4080", "gaming laptop")
- 📊 Extracts **product title, price, and link**
- 🧹 Cleans and processes scraped data
- 💼 Exports full listing data to Excel
- 📈 Analyzes:
  - Average price
  - Top 5 most expensive items
  - Brand frequency distribution
- 📊 Visualizes brand breakdown with a bar chart

---

## 📁 Output Example

- `4080_results.xlsx`:
  - Columns: Title, Price, Link, Brand, Refurbished?
  - Pivot-ready data
- Auto-generated visualization:
  ![brand_chart](example_bar_chart.png)

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Selenium** (browser automation)
- **Pandas** (data manipulation)
- **Matplotlib** (visualization)
- **Excel via openpyxl** (reporting)

---

## 🚀 How to Run

1. **Install dependencies:**
bash:
pip install selenium pandas matplotlib openpyxl webdriver-manager

2. Download or clone the repository:
git clone https://github.com/JoshSauce1/Newegg_Webscraper.git
cd Newegg_Webscraper

3. Run the script:
python scraper.py

4. When prompted, enter the product you want to search (e.g., 4080).

5. The script will:

Launch a Chrome browser

Navigate through all result pages on Newegg

Scrape product titles, prices, and links

Clean and analyze the data

Export it to Excel as 4080_results.xlsx

Display a bar chart of top product brands




