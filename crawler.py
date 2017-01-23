import requests
from bs4 import BeautifulSoup
import random
from pathlib import Path
import json

random.seed()

prevurl = "http://namu.wiki/random"

data = {}

path = Path('./data.json')
if path.is_file():
    with path.open('r') as f:
        data = json.load(f)

while True:
    r = requests.get(prevurl)
    soup = BeautifulSoup(r.text, 'html.parser')
    print([link.get('href') for link in soup.find_all('a')
        if link.get('href') and '/w/' in link.get('href') and '.jpg' not in link.get('href')])
    break

