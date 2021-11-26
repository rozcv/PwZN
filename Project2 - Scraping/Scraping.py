from rich.console import Console
import rich.traceback
import requests
from bs4 import BeautifulSoup
import json
import argparse

parser = argparse.ArgumentParser(description="Scraping")
parser.add_argument('file', help='name of file')
args = parser.parse_args()
print(f'File name: {args.file}')

console = Console()
console.clear()
rich.traceback.install()

req = requests.get('https://www.billboard.com/charts/hot-100/')
console.print(req.status_code)

soup = BeautifulSoup(req.text, 'html.parser')
divs = soup.find_all('div', class_="o-chart-results-list-row-container")
tab = []

for div in divs:
    b = div.find('h3').text.strip()
    tab.append(b)

with open('args.file', 'w', encoding='utf-8') as f:
    json.dump(tab, f)

with open('args.file', 'r', encoding='utf-8') as f:
    y = json.load(f)
    console.print(y)
