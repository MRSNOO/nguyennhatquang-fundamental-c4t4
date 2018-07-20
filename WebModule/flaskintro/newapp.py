from flask import Flask,redirect,url_for

newapp = Flask(__name__)

@newapp.route("/")
def index():
    return "Hello C4T4, this is homepage"
@newapp.route("/about-me")
def aboutme():
    return """Hi I am Quang
              I am 17 years old
              I am studying at Ha Noi Amsterdam
              I like reading, playing games, playing sport and coding.
              Nice to meet you!
            """
@newapp.route("/school")
def school():
    return redirect("http://techkids.vn")
@newapp.route("/personal")
def personal():
    return """  I am Quang,
              I am 17 years old,
              I am studying at Ha Noi Amsterdam,
              I like reading, playing games, playing sport and coding.
            """ 
@newapp.route("/user/<username>")
def user(username):
    if username == "Quang":
        return redirect("http://127.0.0.1:5000/personal")
    else :
        return "User not found"


if __name__ == "__main__":
    newapp.run(debug = True)
    port = int(os.environ.get('PORT', 5000))
    newapp.run(host='0.0.0.0', port=port)
