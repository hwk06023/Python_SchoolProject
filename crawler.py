import requests as req
from bs4 import BeautifulSoup
import re

def crawler(url):
    header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'}

    page = req.get(url, headers = header)
    soup = BeautifulSoup(page.text, 'html.parser')
    divs = soup.findAll("div", {"class": "document_243457_2250 xe_content"})

    divs = str(divs)
    divs = re.sub('<.+?>', '', divs, 0).strip()

    return divs