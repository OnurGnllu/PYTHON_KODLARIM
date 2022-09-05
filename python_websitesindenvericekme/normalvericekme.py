import requests
from bs4 import BeautifulSoup
url = "https://www.bloomberght.com/doviz/dolar"
resp = requests.get(url)
resp.content
soup = BeautifulSoup(resp.content,"html.parser")
fiyat_html =soup.find("span",attrs={"class":"LastPrice upGreen"}).text
c = float (fiyat_html.replace(",",".")) # stringte 17,254 i 17.254 e çevirip sonra float a çevirdim.


date = soup.find("span", attrs= {"class":"date"}).text
print ( "{} tarihi ile birlikte  " "USD güncel fiyatı  {} dir".format(date,fiyat_html))



