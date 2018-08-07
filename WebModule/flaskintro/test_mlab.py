from mongoengine import *

class Movie(Document):
    title = StringField()
    image_url = StringField()
    link = StringField()

# connect to mlab
import mlab
mlab.connect()
# # create a movie
# movie = Movie(title = "The Dark Knight",
#         image_url = "https://7lwy5tgst9-flywheel.netdna-ssl.com/wp-content/uploads/2018/07/1200x630bb.jpg",
#         link = "https://www.imdb.com/title/tt0468569/")
# movie.save()
# # send newly create movie to mlab
movie_list = Movie.objects() #lazy loading
for movie in movie_list:
    print(movie.title)

