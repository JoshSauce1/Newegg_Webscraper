import requests, re
from bs4 import BeautifulSoup

search_term = input("What product do you want to search for? ")

# Creating search URL with user's search term
url = f'https://www.newegg.com/p/pl?d={search_term}&N=4131'
page=requests.get(url).text

# Parsing the HTML content using BeautifulSoup
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong

# Determining the total number of pages of search results
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])


items_found = {}

# Dont want to start at 0 because page 0 does not exist
for page in range(1, pages + 1):                    
    url = f'https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}'
    #Send a req and grabbing every single page
    page = requests.get(url).text                   
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))
    
    for item in items: 
        parent = item.parent

        # Ensuring that only search results with valid links are included
        if parent.name !="a":
            continue
        
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            # Storing price and link data in a dictionary for each item
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except: 
            pass
       

# Sorting items by price and printing them out in order
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items: 
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("--------------------------")