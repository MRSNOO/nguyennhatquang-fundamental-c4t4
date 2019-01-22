from mongoengine import Document, StringField, IntField
from mlab import *
connect()


class Person(Document):
  name = StringField(max_length=200)
  age = IntField()
  weight = IntField()
  height = IntField()
class School(Document):
    name = StringField(max_length=200)
    location = StringField()
    age = IntField()
    student = StringField() 
class Movie(Document):
    name = StringField(max_length=200)
    duration = IntField()
    catagory = StringField()
    actor = StringField()


newPerson = Person(name="ABCXYZ", age=12, weight=60, height=170)
newSchool = School(name="Ha Noi Ams", age=35, location="Hoang Minh Giam Street", student="high school students")
newMovie = Movie(name="Spider Man", duration=2,catagory="hero",actor="Tom Holland")
newPerson.save()
newMovie.save()
newSchool.save() 
# # save push len db
# # Collection ten cua class \

# post : {
#     title: ",adasd",
#     like: 12,
#     comment: [
#         {
#             name: "adasd",
#             comment: "Bai hay qua"
#         }
#     ]
# }
dataGet_person = Person.objects()
dataGet_school = School.objects()
dataGet_movie = Movie.objects()
print(dataGet_person,dataGet_movie,dataGet_school)