from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.nationalgeographic.com/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8") 

soup = BeautifulSoup(text, "html.parser")

blockcard = soup.find("div","mt_row")

blockcard_small = soup.find_all("div","ngp_col ngp_col-bottom-gutter-2 ngp_col-md-6 ngp_col-lg-4")

new_items = []
for block in blockcard_small:
    div_image = block.find("div","mt_promotile__header__image")
    if div_image is not None:
        div_image_2 = div_image.a
        image_link = div_image_2["href"]
print(image_link)
