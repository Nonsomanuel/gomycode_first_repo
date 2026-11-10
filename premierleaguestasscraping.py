import re

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = "https://www.premierleague.com/en/stats/top/players/goals"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#Scraping for top goal scorers
statTable = soup.find("td", class_="stats-table__table-body")
# scoreTable = statTable[0].find("tr")
# for row in scoreTable:
#     player = row.find("td", class_="stats-table__name").get_text(strip=True) if row.find("td", class_="stats-table__name") else None
#     goals = row.find("td", class_="stats-table__stat-value stat-value-cell").get_text(strip=True) if row.find("td", class_="stats-table__stat-value stat-value-cell") else None
#     print(f"Player: {player}, Goals: {goals}")

print(statTable)


# found = set()
# for tag in soup.find_all(class_=re.compile("stats-table")):
#     found.add((tag.name, " ".join(tag.get("class"))))
# for item in sorted(found):
#     print(item)
#
# # 2. Are there any <table> or <tr> elements at all?
# print("tables:", len(soup.find_all("table")), "rows:", len(soup.find_all("tr")))
#
# # 3. Is the data embedded as JSON in a script tag?
# for s in soup.find_all("script"):
#     text = s.string or ""
#     if "stats-table" in text or "__NEXT_DATA__" in str(s.get("id")):
#         print("script tag:", s.get("id"), text[:300])


# driver = webdriver.Chrome()
# driver.get(url)
#
# # Wait until at least one table row exists
# WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
# )
#
# soup = BeautifulSoup(driver.page_source, "html.parser")
# driver.quit()
#
# for row in soup.find_all("tr"):
#     cells = [td.get_text(strip=True) for td in row.find_all("td")]
#     if cells:
#         print(cells)

# print(page.status_code)          # 403 or 200?
# print(len(page.content))
# print("stats-table" in page.text)
# print(soup.prettify())