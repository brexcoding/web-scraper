# web scraper  

 
from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

URL = 'https://www.amazon.com/SAMSUNG-Unlocked-Smartphone-Processor-Graphite/dp/B0CD8NF62Z?ref=dlx_deals_dg_dcl_B0CD8NF62Z_dt_sl14_30&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

url = URL
response = requests.get(url , headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text , 'lxml')
# we got the element by the id in html 
title_element = soup.select_one('#availability')

availability = title_element.text.strip()

print(availability)

