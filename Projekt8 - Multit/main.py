import multiprocessing
import requests as req
from bs4 import BeautifulSoup
import re

site = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
urls = []

def scrape_n_download(urls):
    site = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
    response = req.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        with open("file.png", 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = req.get(url)
            f.write(response.content)
    return urls

def scrape():
    response = req.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    return urls

def download(urls):
    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        with open(f'file{url}.png', 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = req.get(url)
            f.write(response.content)

def mp_handler(urls):
    p = multiprocessing.Pool(2)
    p.map(scrape_n_download,urls)

if __name__ == '__main__':
    links = scrape()
    download(links)
    mp_handler(links)
