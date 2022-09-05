import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/finance/quote/USD-TRY?sa=X&ved=2ahUKEwih1M2P1Mv5AhUGX_EDHcynBOAQmY0JegQIAxAb"
resp = requests.get(url)
resp.content
soup = BeautifulSoup(resp.content,"html.parser")
# .text komutu html bir veriyi yaziya çevirir.
fiyat_html =soup.find("div",{"class":"YMlKec fxKbKc"}).text
#bu degeri float yapıyoruz
float_dolar = float(fiyat_html)
print("Dolarin Güncel Fiyati  =  {}  \nNot = Veriler Google Finans"
      "Üzerinden çekilmiştir.".format(float_dolar))







