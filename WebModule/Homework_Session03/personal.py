from flask import Flask,render_template
import mlab1

personal = Flask(__name__)
mlab1.connect()

@personal.route("/")
def index():
    return render_template("personal.html")

if __name__ == "__main__":
    personal.run(debug = True)