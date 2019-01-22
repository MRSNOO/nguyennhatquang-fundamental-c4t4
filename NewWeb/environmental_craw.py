from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.treehugger.com/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")    # thu vien 


soup = BeautifulSoup(text, "html.parser")

cblockcards = soup.find("div","c-block__cards")

article_news = cblockcards.find_all("article","c-article c-article--card")

new_items = []
for article in article_news:
    div = article.find("div","c-article__container")
    if div is not None:
        div2 = div.find("div","c-article__summary")
        div3 = div2.h3.a
        title = div3.text 
        link = div3["href"]
        

        div4 = div.find("div","c-article__image")
        div5 = div4.a.img
        picture = div5["src"]
        item_content = {
                "Title" : title,
                "Link"  : link,
                "Picture" : picture
                
            }
        new_items.append(item_content)


pyexcel.save_as(records = new_items, dest_file_name="treehugger.xlsx")



