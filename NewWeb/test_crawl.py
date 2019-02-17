from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.theguardian.com/uk/environment"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")    # thu vien 


soup = BeautifulSoup(text, "html.parser")

big_content = soup.find("div","")



