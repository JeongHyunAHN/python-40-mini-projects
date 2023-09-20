import requests
from bs4 import BeautifulSoup

# from currency_converter import CurrencyConverter

# # cc = CurrencyConverter()
# # print(cc.currencies)

# cc = CurrencyConverter("http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip")
# print(cc.convert(1,'USD','KRW'))

def get_exchange_rate(target1,target2):
    headers = {
        'User_Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text.html; charset=utf-8'
    } 
    
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2),headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers =content.find('span',{'id':'last_last'})
    print(containers.text)
    
get_exchange_rate('usd','krw')