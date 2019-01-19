from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://vnexpress.net/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")

soup = BeautifulSoup(text, "html.parser")
ul_news = soup.find("ul", "ul1 ulnew")