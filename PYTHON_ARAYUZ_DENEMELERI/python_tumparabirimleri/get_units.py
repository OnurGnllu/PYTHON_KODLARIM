import requests
from bs4 import BeautifulSoup
from MYSQL_adapter import veri_gonder
# url de sadece isim değiştirerek veriler dağıtılmış
url1 = "https://www.google.com/finance/quote/"
url2 = "?sa=X&ved=2ahUKEwih1M2P1Mv5AhUGX_EDHcynBOAQmY0JegQIAxAb"


def get_dolar():
    parabirimi = "USD-TRY"
    total_url = url1 + parabirimi + url2
    resp = requests.get(total_url)
    resp.content
    soup = BeautifulSoup(resp.content, "html.parser")
    fiyat_html = soup.find("div", {"class": "YMlKec fxKbKc"}).text
    float_dolar = float(fiyat_html)
    return float_dolar

def get_euro():
    parabirimi = "EUR-TRY"
    total_url = url1 + parabirimi + url2
    resp = requests.get(total_url)
    resp.content
    soup = BeautifulSoup(resp.content, "html.parser")
    fiyat_html = soup.find("div", {"class": "YMlKec fxKbKc"}).text
    float_euro = float(fiyat_html)
    return float_euro

def get_sterlin():
    parabirimi = "GBP-TRY"
    total_url = url1 + parabirimi + url2
    resp = requests.get(total_url)
    resp.content
    soup = BeautifulSoup(resp.content, "html.parser")
    fiyat_html = soup.find("div", {"class": "YMlKec fxKbKc"}).text
    float_sterlin = float(fiyat_html)
    return float_sterlin















