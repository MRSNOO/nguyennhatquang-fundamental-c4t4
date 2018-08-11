#1. Download dantri page 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com.vn"
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
ul_news = soup.find("ul", "ul1 ulnew")


#3. Extract Data
li_list = ul_news.find_all("li")
# href, title, src : attribute  ;     content, text
new_items = []
for li in li_list: #li la 1 dictionary #li_list la 1 list 
    a = li.h4.a
    link = a["href"]
    title = a.text 
    item = {
        "Title" : title,
        "Link"  : link  
    }
    new_items.append(item)

#4. Save data 
pyexcel.save_as(records=new_items, dest_file_name="dantrinews2.xlsx")
