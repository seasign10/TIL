import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(kospi)