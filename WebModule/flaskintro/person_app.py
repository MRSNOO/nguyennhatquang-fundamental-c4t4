from flask import Flask, render_template

person_app = Flask(__name__)

class Sport:
    def __init__(self, name, best_teams, best_players, image_url, ref_link, tournaments):
        self.name = name 
        self.best_teams = best_teams
        self.best_players = best_players
        self.image_url = image_url
        self.ref_link = ref_link
        self.national_tournaments = tournaments

football = Sport("Football", 
            "France, Croatia, England, Belgium",
            "Messi, Rolnado, Mbappe",
            "https://i0.wp.com/www.infographicspedia.com/wp-content/uploads/2014/07/FIFA-World-Cup-Teams-Described-in-3-Words-infographic.jpg?resize=1024%2C724",
            "https://www.fifa.com/worldcup/",
            "Most Famous Football tournaments"  )
basketball = Sport("Basketball",
            "Golden State Warriors, Houston Rockets, Cleverland Cavaliers",
            "Stephen Curry, Lebron James, Micheal Jordan",
            "https://mk0slamonlinensgt39k.kinstacdn.com/wp-content/uploads/2015/09/nba-finals.jpg",
            "http://www.nba.com/#/",
            "Most Famous Basketball tournaments" )
lol = Sport("League of Legends",
        "SKT, KT Rolster, Kingzone",
        "Faker, Sofm, Levi",
        "https://am-a.akamaihd.net/image?quality=preserve&f=https://lolstatic-a.akamaihd.net/frontpage/apps/prod/playnow-global/en_US/cbe4e8d0768d5d7a7673d095daec915fe2f828ea/assets/img/cover-1.jpg",
        "https://na.leagueoflegends.com/en/",
        "Most famous LOL tournaments")
sport_list = [football, basketball, lol]

@person_app.route("/")
def index():
    return render_template("index.html", name = "Quang",
    image_url = "https://scontent.fhan4-1.fna.fbcdn.net/v/t1.0-9/35557482_688393151492144_1642431584600588288_n.jpg?_nc_cat=0&oh=50b1abeefba2f6cd465a540329e4e5fb&oe=5BD9C1C2")

@person_app.route("/sport")
def sport():
    return render_template("personal_info.html", sports = sport_list )

if __name__ == "__main__":
    person_app.run(debug = True)




