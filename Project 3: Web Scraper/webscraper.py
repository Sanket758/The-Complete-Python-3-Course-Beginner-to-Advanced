from bs4 import BeautifulSoup
import requests as r


search = input('Enter the thing you want to search for:')
params = {"q": search}

data = r.get('http://www.bing.com/search', params=params)

soup = BeautifulSoup(data.text, "html.parser")

# print(soup.prettify())

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
