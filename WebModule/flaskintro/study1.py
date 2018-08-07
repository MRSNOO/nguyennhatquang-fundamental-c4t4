from flask import Flask, render_template

study1 = Flask(__name__)

@study1.route("/")
def picture():
    return render_template("study.html", picture = "the-first-reactions-for-avengers-infinity-war-have-flooded-social-media-social" )

if __name__ == "__main__":
    study1.run(debug = True)
