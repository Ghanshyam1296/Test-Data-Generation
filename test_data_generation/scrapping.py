from bs4 import BeautifulSoup
import requests

source=requests.get('http://www.coreyms.com').text

soup=BeautifulSoup(source,'lxml')

print(soup.prettify())

