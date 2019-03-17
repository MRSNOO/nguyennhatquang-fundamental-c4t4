from mongoengine import Document, StringField, IntField, BooleanField, DateTimeField

class Post(Document):
  title = StringField(max_length=200)
  author = StringField()
  picture_link = StringField()
  content = StringField()
  content_editor = StringField()
  status = BooleanField()
  author_pic = StringField()
  date = DateTimeField()
  link = StringField()
  picture_type = StringField()
  authorize_code = StringField()
  
  Title_post = StringField()
  author_name = StringField()
  author_link = StringField()
  author_pic_small = StringField()
  Time = DateTimeField()
  Picture_post = StringField()
  Content = StringField()





 