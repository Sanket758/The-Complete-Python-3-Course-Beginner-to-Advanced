from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import requests as r
import os


def start_search():

    search = input('Search: ')
    params = {'q': search}
    dir_name = search.replace(" ", "_").lower()
    try:
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
    except IOError:
        print("can't create a folder")

    data = r.get('http://www.bing.com/images/search', params=params)

    soup = BeautifulSoup(data.text, 'html.parser')
    links = soup.findAll('a', {'class': 'thumb'})

    for item in links:
        try:
            img_obj = r.get(item.attrs['href'])
            print('Getting..', item.attrs['href'])
            title = item.attrs['href'].split('/')[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save('./Scraped_Images/' + title, img.format)
            except:
                print('Could not save image!')
        except:
            print('Server error!')

    start_search()


start_search()
