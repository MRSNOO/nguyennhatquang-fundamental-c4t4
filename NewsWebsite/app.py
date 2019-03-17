# -_- python 2.7.15 zz
# tải python 3.7.0 về cài đi e

from flask import Flask, render_template, request, redirect, url_for
from models.classModels import *
from mlab import *
import math
connect()
app = Flask(__name__)

record_per_page = 8 

@app.route('/test', methods = ["GET","POST"])
def test():
    if request.method == "GET":
        dataGet_post = Post.objects() 
        return render_template('homepage/test.html', data = dataGet_post)

# HomePage
@app.route('/home',methods = ["GET","POST"])
def home():
    if request.method == "GET":
        page_nb = 1 
        offset = (page_nb - 1) * record_per_page
        allPost = Post.objects()
        paginationLength = math.ceil(len(allPost) / 8)
        dataGet_post = Post.objects.skip( offset ).limit( record_per_page) #no chi lay 8 thang
        return render_template('homepage/home.html', data = dataGet_post, paginationLength = paginationLength)

@app.route('/cleenproject',methods = ['GET','POST'])
def cleenproject():
    if request.method == "GET":
        dataGet_post = Post.objects()
        return render_template('homepage/cleenproject_home.html', data = dataGet_post)

@app.route('/home/<number>',methods = ["GET","POST"])
def home_page(number):
    if request.method == "GET":
        print(number)
        number = int(number)
        page_nb = number
        offset = (page_nb - 1) * record_per_page
        allPost = Post.objects()
        paginationLength = math.ceil(len(allPost) / 8)
        dataGet_post = Post.objects.skip( offset ).limit( record_per_page )
        return render_template('homepage/home.html', data = dataGet_post, paginationLength = paginationLength)

@app.route('/news/<idNew>', methods = ["GET", "POST"])
def new(idNew):
    if request.method == "GET":
        dataGet_post = Post.objects()
        new = Post.objects.get(id=idNew)
        return render_template('homepage/each_new.html', new = new, data = dataGet_post)




@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        dataGet_post = Post.objects()   
        return render_template('homepage/index.html', data = dataGet_post)


@app.route('/pending', methods = ["GET", "POST"])
def pending():
    if request.method == "GET":
        dataGet_post = Post.objects()   
        return render_template('homepage/pending.html', data = dataGet_post)

@app.route('/duyet/<userId>', methods = ["GET", "POST"])
def duyet(userId):
        if request.method == "GET":
                chooseUser = Post.objects.get(id=userId)
                chooseUser.update(set__status = True)
                return redirect(url_for("pending"))

@app.route('/add',methods = ["GET","POST"])
def add():
    if request.method == "GET": 
        dataGet_post = Post.objects()
        return render_template('action/postCreate.html', data = dataGet_post) # 1 list cac data
    elif request.method == "POST": 
        # lay data sau khi nhap vao o form 
        form = request.form 
        title = form["title"] 
        author = form["author"]
        picture_link = form["picture_link"]
        content = form["content"]
        authorize_code = form["authorize_code"]
        content_editor = form["content_editor"]

        postNewPost = Post(title = title, author = author,picture_link=picture_link, content = content, status=False,authorize_code = authorize_code)
        #dùng classModels để lưu lại dữ liệu 
        print(content_editor)
        postNewPost.save()
        # cho lên database trên mongoengine
        dataGet_post = Post.objects() 
        # return render_template('result.html', data = dataGet_person)
        return redirect(url_for("pending")) #chay method GET cua def index() o ben tren 
                                            #url for la trỏ đến hàm def 


        
                                

@app.route('/editUser/<userId>',methods = ["GET","POST"])
def editUser(userId):
    if request.method == "GET":
        userGet = Post.objects.get(id=userId)
        return render_template("action/postEdit.html", currentUser = userGet) #data cua 1 thang user

    elif request.method == "POST": #post = submit #xu ly nut submit 
        # HTML -> SERVER
        form = request.form #lấy cái form từ html của indextest
        title = form["title"] #lấy dữ liệu người dùng nhập vào 
        author = form["author"]
        picture_link = form["picture_link"]
        content = form["content"]

        #SERVER -> DATABASE
        userGet = Post.objects.get(id=userId)
        userGet.update(set__title = title, set__author = author, set__picture_link = picture_link , set__content = content)
        return redirect(url_for("index"))

@app.route('/deleteUser/<userId>',methods = ["GET","POST"])
def deleteUser(userId): #userId tu mlab
    userGet = Post.objects.get(id=userId)
    userGet.delete()  #xoa dong vua bam 
    return redirect(url_for("pending"))

      


if __name__ == '__main__':
  app.run(port=8000, debug=True)