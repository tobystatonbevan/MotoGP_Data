import requests
from bs4 import BeautifulSoup

def getRiderNameNumbers(riderUrl = "https://www.motogp.com/en/riders/motogp"):

    #url = "https://www.motogp.com/en/riders/motogp"
    page = requests.get(riderUrl)

    soup = BeautifulSoup(page.content, "html.parser")

    nameAndNumberList = []

    nameResults = soup.find_all("div",class_="rider-list__info-name")
    for r in nameResults:
        #print(r)
        nameNumDict = {}
        nameNumDict['Name'] = r.find_all("span")[0].text.strip()+" "+r.find_all("span")[1].text.strip()
        nameNumDict['Number'] = r.parent.find("span",class_="rider-list__info-hashtag").text[3:]
        nameAndNumberList.append(nameNumDict)
        # print(f"""=========================================
        #     {r}
        #     ++++
        #       {r.parent.find("span",class_="rider-list__info-hashtag").text[3:]}
        #     =======================================
        #     """)

    # with open("output.txt", "w", encoding="utf-8") as f:
    #     f.write(str(soup))
    # f.close()

    return nameAndNumberList

# print(getRiderNameNumbers())