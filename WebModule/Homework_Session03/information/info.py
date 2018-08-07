from mongoengine import *
import mlab
mlab.connect()

class Post(Document): #ten collection
    title = StringField()
    author = StringField()
    content = StringField()

quang = Post(author = "Quangg", title = "Lop rat vui va cac anh tro giang va giang vien rat vui tinh + tot bung",
                    content = "Cac em nho hoc hanh cham chi")

class Customers(Document):
    name = StringField()
    age = IntField()
    address = StringField()
    ref = StringField()

list_customers = Customers.objects()
event = 0 
ad = 0
word = 0
for customer in list_customers:
    if customer.ref == "events":
        event += 1
    elif customer.ref == "ads":
        ad += 1
    elif customer.ref == "wom":
        word += 1
list_ref = [event, ad, word]





import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'event', 'ads', 'wom'
sizes = [event , ad, word]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
    