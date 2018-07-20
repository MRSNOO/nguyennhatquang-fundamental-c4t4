# 1. Create flask app
from flask import Flask #class

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello C4T4, this is homepage"


@app.route("/about-me")
def about_me_hihi():
    return "My name is Quang1"

@app.route("/hello/<name>")
def hello(name):
    return "hello " + name 

# 2. Run app 
if __name__ == "__main__":
    app.run(debug = True)

