from googletrans import Translator
from bs4 import BeautifulSoup, Tag,NavigableString
html1 = open("/index.html").read()
soup = BeautifulSoup(html1)
tags = soup.find_all(["p","ul","span","ol","h1","h2","h3","h4","h5","h6","td"])
translator=Translator()
from_language, to_language = 'en', 'hi'

elements = ['span','h1','h2','h3','h4','h5','h6',a']
for i in soup.findAll(elements):
  i.string.replace_with(tss.google(html1, from_language, to_language))
print(soup)
with open("output2.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))