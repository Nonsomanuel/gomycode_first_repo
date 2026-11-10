import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
books = soup.find_all("article", class_="product_pod")

data = []

#Extracting book information
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    # print(f"Title: {title}, Price: {price}, Availability: {availability}")
    data.append({
        "title": title,
        "price": price,
        "availability": availability
    })
df = pd.DataFrame(data)
book_price = pd.to_numeric(df["price"].str.replace("£", ""))

# df.to_csv("books.csv", index=False)
print(df)
print(book_price)
# print(f'Number of books found: {len(books)}')
# print(soup.prettify())
# print(soup.title.get_text())