from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj)
# find span that class = green and red
nameList = bsObj.findAll("span",{"class":{"green"}})
for name in nameList:
    print(name.get_text())