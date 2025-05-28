# 💻 Newegg Product Scraper & Price Analysis Dashboard

This project automates the collection and analysis of GPU product listings from [Newegg.com](https://www.newegg.com). It uses **Selenium** for scraping, **Pandas** for data wrangling, and **Matplotlib** for insights — then exports everything to Excel with a **fully interactive dashboard** for business-ready visuals.

---

## 📌 Features

### 🔍 Search-Based Product Scraping
- Search by keyword (e.g., `"4080"`, `"gaming laptop"`)
- Scrapes product **title**, **price**, and **link**
- Handles pagination to get full listing data

### 🧹 Data Cleaning & Processing
- Extracts product brand from title
- Filters out incomplete entries
- Converts price strings to numerical values

### 📊 Excel Report + Dashboard
- Exports data to `.xlsx` format
- Creates **interactive dashboard**:
  - KPIs (Total Listings, Avg Price, Highest Price)
  - Pivot table summarizing average/max/sum price per brand
  - Brand slicer for filtering
  - Bar chart for brand price breakdown

### 📤 Dashboard PDF Export
- Exports final formatted Excel dashboard as a polished `.pdf`
- Clean layout with header, slicer, chart, and summary metrics

---

## 📂 Included Files

| File | Description |
|------|-------------|
| `scraper.py` | Python script for scraping and Excel generation |
| `4080_figure.png` | Matplotlib chart of top brands |
| `4080_results.xlsx` | Final Excel report with dashboard |
| `4080_results.pdf` | PDF export of the dashboard |
| `README.md` | Project documentation |
| `WS Console Look.png` | Console example output |

---

## 📈 Skills Demonstrated
- Web scraping automation (Selenium)
- Data transformation & visualization (Pandas + Matplotlib)
- Excel reporting: **pivot tables**, **charts**, **conditional formatting**, **dashboards**
- Clean PDF exports for business-facing deliverables

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




