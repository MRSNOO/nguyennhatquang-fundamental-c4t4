from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://genk.vn/"
connection = urlopen(url)  #open
raw_data = connection.read()  #read
text = raw_data.decode("utf-8")   #decode

# with open("") luu vao 1 cai file
# f = open("dantri.html","wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify())

#2. Find the ROI (Region of Interest)
genk_news = soup.find("ul", {"id": "LoadListCate"})

#3. Extract Data
li_list = genk_news.find_all("li")
# href, title, src : attribute  ;     content, text
new_items = []
for li in li_list: #li la 1 dictionary #li_list la 1 list 
    div = li.find("div","knswli-right elp-list")
    if div is not None:
        a = div.h4.a
        link = a["href"]
        title = a.text 
    div2 = li.find("div","knswli-left fl")    
    if div2 is not None:
        b = div2.a.img
        link_anh = b["src"]
    item = {
        "Title" : title,
        "Link"  : link, 
        "Link_Anh" :link_anh 
    }
    new_items.append(item)

#4. Save data 
pyexcel.save_as(records = new_items, dest_file_name="genknews2.xlsx")