from bs4 import BeautifulSoup
import requests

head_Html_lotto='http://traderoom.cnyes.com/tse/quote2FB.aspx?code=3231'
res = requests.get(head_Html_lotto, timeout=30)
print(res.text)
