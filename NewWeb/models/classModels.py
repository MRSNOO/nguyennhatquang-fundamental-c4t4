from mongoengine import Document, StringField, IntField, BooleanField

class Person(Document):
  name = StringField(max_length=200)
  age = IntField()
  weight = IntField()
  height = IntField()
  status = BooleanField()
# status = true -> alive
# status = false -> death

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