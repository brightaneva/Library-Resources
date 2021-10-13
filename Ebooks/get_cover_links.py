import requests
from bs4 import BeautifulSoup
import os


def get_cover_link(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        return f"http://library.lol{image['src']}"
        # with open("cover_links.txt","a+") as f:
        #     f.write(link + "\n") 
        #     print("A cover link is appended")


    