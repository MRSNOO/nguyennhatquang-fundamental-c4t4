# 1. Create flask app
from flask import Flask, render_template #class

app = Flask(__name__)

class Movie:
    def __init__(self, title ,casts, thumbnail_url, ref_link):
        self.title = title
        self.casts = casts 
        self.thumbnail_url = thumbnail_url
        self.ref_link = ref_link
# nap bien vao Movie

The_Dark_knight = Movie("The Dark Knight",
        "Christian Bale, Heath Ledger",
        "https://7lwy5tgst9-flywheel.netdna-ssl.com/wp-content/uploads/2018/07/1200x630bb.jpg",
        "https://www.imdb.com/title/tt0468569/")
Batman_Begin = Movie("Batman Begins",
        "Christian Bale, Killian Murphy, Katie Holmes",
        "https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Bale_as_Batman.jpg/170px-Bale_as_Batman.jpg",
        "https://www.imdb.com/title/tt0372784/")
movie_list = [The_Dark_knight, Batman_Begin]

@app.route("/")
def index():
    return render_template("index.html", name = "Quang",
    image_url = "https://scontent.fhan4-1.fna.fbcdn.net/v/t1.0-9/35557482_688393151492144_1642431584600588288_n.jpg?_nc_cat=0&oh=50b1abeefba2f6cd465a540329e4e5fb&oe=5BD9C1C2")

@app.route("/movie") # ten route
def movie(): 
    return render_template("movie.html", movies = movie_list) #movies là trong for m in "movies" trong movie html 


@app.route("/casts")
def casts():
    return render_template("casts.html", casts = ["Christian Bale", "Heath Ledger", "Gary Oldman", "Micheal Cane"])
                        #gọi thư mục "casts.html"                     # cast trong for cast in casts ở trong casts.html
@app.route("/about-me")
def about_me_hihi():
    return "My name is Quang1"

@app.route("/hello/<name>")
def hello(name):
    return "hello " + name 

# 2. Run app 
if __name__ == "__main__":
    app.run(debug = True)

