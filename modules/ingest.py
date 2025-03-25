import requests
from bs4 import BeautifulSoup

URL = "https://www.motogp.com/en/riders/motogp"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div",class_="rider-list__info-name")
for r in results:
    print(r.find_all("span")[0].text.strip(),r.find_all("span")[1].text.strip())

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(soup))
f.close()