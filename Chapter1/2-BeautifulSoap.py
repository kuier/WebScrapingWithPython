from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsobj=BeautifulSoup(html.read(),"html.parser")
print(bsobj.h1)