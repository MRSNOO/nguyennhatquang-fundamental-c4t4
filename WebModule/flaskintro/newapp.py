from flask import Flask,redirect,url_for

newapp = Flask(__name__)



Users = {
        'huy' :         {
                'name' : 'Nguyen Quang Huy',
                'age' : 29
        },
        'don' : {
                "name" : 'Don zoombie',
                'age' : 23
        },
        'quang' : {
                'name' : "Nguyen Nhat Quang",
                'age' : 17
        }
    }
def user_profile(username,Users):
    return_informations= ""
    if username in Users:
        for profile in Users[username]:
            return_informations += str(profile)
            return_informations += ":"
            return_informations += str(Users[username][profile])
            return_informations += "<br/>"
        return return_informations    
    else:
        return None    

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
def profile(username):
    printing=user_profile(username,Users)
    if printing is not None:
        return printing
    else:
        return "User not found"   


if __name__ == "__main__":
    newapp.run(debug = True)
    port = int(os.environ.get('PORT', 5000))
    newapp.run(host='0.0.0.0', port=port)
