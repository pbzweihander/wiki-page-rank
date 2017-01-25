import requests
from bs4 import BeautifulSoup
import random
from pathlib import Path
import json
import time

random.seed()

next = "http://namu.wiki/random"

data = {}
links = []

path = Path('./data.json')
if path.is_file():
    with path.open('r') as f:
        data = json.load(f)

while True:
    r = requests.get(next)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.text.replace(' - 나무위키', '')
    if '파일:' in title:
        next = "http://namu.wiki" + random.choice(links)
        continue
    links = [link.get('href') for link in soup.find_all('a')
        if link.get('href') and '/w/' in link.get('href') and '.jpg' not in link.get('href')]
    if title in data:
        data[title] = data[title] + 1
    else:
        data[title] = 1
    with path.open('w') as f:
        json.dump(data, f)
    next = "http://namu.wiki" + random.choice(links)
    print(title)

