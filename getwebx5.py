import requests
from bs4 import BeautifulSoup

r = requests.get("http://traderoom.cnyes.com/tse/quote2FB.aspx?code=3231")
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "lxml")

#fp = open("test2.txt", "w", encoding="utf8")
#fp.write(soup.prettify())
#print("寫入檔案test2.txt...")
#fp.close()

#tag = soup.table
#print(type(tag))
#print(tag)
#print(tag.name)
#print(tag["id"])
#print(tag["class"])

print("====================================================")
tag_div = soup.find(id="bxrt")
print(soup.div)
#tag_ul = tag_div.find("hd5") 
#print(tag_ul.string)

