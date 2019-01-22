from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://vnexpress.net/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")

soup = BeautifulSoup(text, "html.parser")
vnexpress_news = soup.find("ul", {"id":"list_sub_featured"})

li_list = vnexpress_news.find_all("li")

new_items = []
for li in li_list:
    a = li.a
    title = a.title
    text = a.text
    link = a["href"]
    item = { 
        "Title" : title,
        "Link" : link,
        "Text": text
    }
    new_items.append(item)

pyexcel.save_as(records = new_items, dest_file_name = "vnexpressnews.xlsx")

