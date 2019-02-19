from mongoengine import Document, StringField, IntField, BooleanField

class Post(Document):
  title = StringField(max_length=200)
  author = StringField()
  picture_link = StringField()
  content = StringField()
  status = BooleanField()