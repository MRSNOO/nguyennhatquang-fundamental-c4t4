from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
connection = urlopen(url)  #open
raw_data = connection.read()  #read
text = raw_data.decode("utf-8") 

soup = BeautifulSoup(text, "html.parser")

section = soup.find("section", "section chart-grid")

div = section.find("div", "section-content")

song = []
if div is not None:
    ul = div.find("ul")
    li_list = ul.find_all("li")
    for li in li_list:
        a = li.h3
        name = a.text
        b = li.h4
        artist = b.text
        songs = {
            "Songs" : name,
            "Artists": artist    
        }
        song.append(songs)


options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': len(song), # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
for i in range(len(song)):
    dl = YoutubeDL(options)
    dl.download(song[i]["Songs"])

