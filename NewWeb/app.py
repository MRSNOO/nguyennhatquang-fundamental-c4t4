from flask import Flask, render_template, request, redirect, url_for
from models.classModels import *
from mlab import *
connect()
app = Flask(__name__)



@app.route('/abc')
def abc():
    return "Day laf abc"

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        dataGet_person = Person.objects()   #lay tu database ve
        return render_template('homepage/index.html', data = dataGet_person)
        
@app.route('/pending', methods = ["GET", "POST"])
def pending():
    if request.method == "GET":
        dataGet_person = Person.objects()   #lay tu database ve
        return render_template('homepage/pending.html', data = dataGet_person)

@app.route('/duyet/<userId>', methods = ["GET", "POST"])
def duyet(userId):
        if request.method == "GET":
                chooseUser = Person.objects.get(id=userId)
                chooseUser.update(set__status = True)
                return redirect(url_for("homepage/pending"))

@app.route('/add',methods = ["GET","POST"])
def indextest():
    # if request.method == "GET": #truy cap vao bat ki trang nao thi deu la GET 
    #     dataGet_school = School.objects()
    #     return render_template("indextest.html", data = dataGet_school)
    # elif request.method == "POST":
    #     form = request.form #nguoi dung nhap data(username, password,...) va lay ra o form 
    #     name = form["name"]
    #     location = form["location"]
    #     age = form["age"]
    #     student = form["student"]
    #     postNewSchool = School(name = name, location = location, age = age, student = student) #nap cac gia tri vao postnewschool
    #     postNewSchool.save()
    #     dataGet_school = School.objects()
    #     return render_template('result.html', data = dataGet_school)
    if request.method == "GET": #nhận từ server
        dataGet_person = Person.objects()
        return render_template('action/formCreate.html', data = dataGet_person) # 1 list cac data
    elif request.method == "POST": #post bài lên 
        # lay data sau khi nhap vao o form 
        form = request.form #lấy cái form từ html của indextest
        name = form["name"] #lấy dữ liệu người dùng nhập vào 
        age = form["age"]
        height = form["height"]
        weight = form["weight"]
        postNewPerson = Person(name=name, age=age, weight=weight, height=height, status=False)
        #dùng classModels để lưu lại dữ liệu 
        postNewPerson.save()
        # cho lên database trên mongoengine
        dataGet_person = Person.objects() 
        # return render_template('result.html', data = dataGet_person)
        return redirect(url_for("index")) #chay method GET cua def index() o ben tren 
                                                #url for la trỏ đến hàm def 

@app.route('/editUser/<userId>',methods = ["GET","POST"])
def editUser(userId):
    if request.method == "GET":
        userGet = Person.objects.get(id=userId)
        return render_template("action/formEdit.html", currentUser = userGet) #data cua 1 thang user

    elif request.method == "POST": #post = submit
        # HTML -> SERVER
        form = request.form #lấy cái form từ html của indextest
        name = form["name"] #lấy dữ liệu người dùng nhập vào 
        age = form["age"]
        height = form["height"]
        weight = form["weight"]

        #SERVER -> DATABASE
        userGet = Person.objects.get(id=userId)
        userGet.update(set__name = name, set__age = age, set__weight = weight, set__height = height)
        return redirect(url_for("index"))

@app.route('/deleteUser/<userId>',methods = ["GET","POST"])
def deleteUser(userId): #userId tu mlab
    userGet = Person.objects.get(id=userId)
    userGet.delete()  #xoa dong vua bam 
    return redirect(url_for("index")) #chay method GET cua def index() o ben tren 



    


if __name__ == '__main__':
  app.run(port=8000, debug=True)
 