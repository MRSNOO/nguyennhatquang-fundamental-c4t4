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

# create a list
link_list = []
string = "https://www.treehugger.com/"
pictures_list = []
title_list = []

new_items = []
new_items_eachweb = []
for article in article_news:
    div = article.find("div","c-article__container")
    if div is not None:
        div2 = div.find("div","c-article__summary")
        div3 = div2.h3.a
        title = div3.text 
        link= string + div3["href"]
        link_list.append(link)
        

        div4 = div.find("div","c-article__image")
        div5 = div4.a.img
        picture = div5["src"]
        item_content = {
                "Title" : title,
                "Link"  : link,
                "Picture" : picture
                
            }
        new_items.append(item_content)

for link in link_list:
	url = link
	connection = urlopen(url)
	raw_data = connection.read()
	text = raw_data.decode("utf-8")
	soup = BeautifulSoup(text, "html.parser")
	
	
	web_title = soup.find("header","c-article__header")
	web_title2 = web_title.h1


	primary_content = soup.find("div","c-article__primary-content")
	pictures = primary_content.find_all("div","th_img")
	content = primary_content.find_all("p")
	
	
	item_content2 = {
	"Content":content,
	"Web Title" : web_title2
}		


	new_items_eachweb.append(item_content2)

	for pic in pictures:
		pic_link_1 = pic.img
		pic_link_2 = pic_link_1["src"]
		item_content3 = {
			"Content_side_picture_link" : pic_link_2 
		}
		new_items_eachweb.append(item_content3)


    # for pic in pictures:
    #     div1_1 = pic.img
    #     picture1_1 = div1_1["src"]



pyexcel.save_as(records = new_items_eachweb, dest_file_name="treehugger.xlsx")



