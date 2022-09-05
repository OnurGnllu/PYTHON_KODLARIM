import xml.etree.ElementTree as ET
import urllib.request
import requests
from bs4 import BeautifulSoup
url = 'https://www.tcmb.gov.tr/kurlar/today.xml'

document = requests.get(url)

soup= BeautifulSoup(document.content,"lxml-xml")# .text ile gereksiz tablolandırmayı temizledi ve text formatına getirdi
# .split ile tüm kelimeleri bir array elemanı yaptı.
ayrik_hali = soup.text.split()
print(ayrik_hali)
print(float(ayrik_hali[5])) #dolar icin



