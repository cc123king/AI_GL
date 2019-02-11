from flask import Flask,render_template,request,session
import flask_bootstrap,time
from flask_sqlalchemy import SQLAlchemy
from yzm import dr
from secure_pass import pa_jm

app = Flask(__name__)
app.secret_key='a5s1d3q7s.d-1qdf152'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:15370040@127.0.0.1/AI_gl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
flask_bootstrap=flask_bootstrap.Bootstrap(app)
class user(db.Model):
    __tablename__='users'
    usename=db.Column(db.String(12),primary_key=True)
    password=db.Column(db.String(90))

class Text(db.Model):
    __tablename__='texts'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    textname=db.Column(db.BLOB)
    content=db.Column(db.BLOB)

class Equipment(db.Model):
    __tablename__='equipment'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20))
    value=db.Column(db.Integer)

@app.route('/read2/<num>')
def read2(num):
    if num == '1':
        file1=db.session.query(Text).filter(Text.id==1).first()
        print(file1.textname.decode('utf8'))
        return render_template('txt.html',filename1=file1.textname.decode('utf8'),text1=file1.content.decode('utf8'))
    else:
        return "OK"


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/read')
def read_1():
    return render_template('txt.html')

@app.route('/flushyzm')
def f_yzm():
    global l
    l=dr()
    return 'OK'

@app.route('/login_yz',methods=['POST'])
def login_yz():
    users=request.form.get('users')
    password=request.form.get('password')
    str1=request.form.get('yzm')
    global l
    str2 =''.join(l)
    if str1.lower() !=str2.lower():
        l=dr()
        return 'error1'
    else:
        list1 =db.session.query(user).filter(user.usename==users).first()
        if list1.password !=pa_jm('admin',password):
            l=dr()
            return 'error2'
        else:
            session['user']=users
            l=dr()
            return 'OK'
@app.route('/updates',methods=['POST'])
def updates():
    old_password=request.form.get('old_password')
    new_password=request.form.get('new_password')
    re_new_password=request.form.get('re_new_password')
    mm=pa_jm('admin',old_password)
    str0 =db.session.query(user).filter(user.usename=='admin').first()
    if mm !=str0.password:
        return 'error1'
    elif new_password !=re_new_password:
        print(new_password)
        print(re_new_password)
        return 'error2'
    else:
        str0.password=pa_jm('admin',new_password)
        db.session.commit()
        return 'ok'
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    data=time.time()
    return render_template('login.html',val1=data)

@app.route('/nav_page')
def nav():
    data=time.time()
    return render_template('nav_page.html',val1=data)

db.drop_all()
db.create_all()
x=pa_jm('admin','admin')
user1=user(usename=u'admin',password=x)
db.session.add(user1)
db.session.commit()
l = dr()
text1=Text(textname=u'物联网在智能家居中应用情况分析'.encode('utf8'),content=u"1、对智能家居的相关认识智能家居，或称智能住宅。首先，它需要在一个家庭中建立一个通讯网络，为家庭信息提供必要的通路，在家庭网络操作系统的控制下，通过相应的硬件和执行机构，实现对连入家庭网络的所有家电和设备的控制和监测；其次，它们都要通过一定的媒介，构成与外界的通讯通道，以实现与家庭以外的世界沟通信息，满足远程控制、监测和交换信息的需求，其最终目的都是满足人们在家庭中对安全、舒适、方便地工作和生活的需求。智能家居是以家为平台，兼备自动化、智能化的高效、舒适、安全、便利的家居环境。智能家居是一个典型的集计算机、通讯和消费于一体的3C系统，是整个世界形成的一个巨型网络的末端，俗称是该网络的“最后100m”。".encode('utf8'))
db.session.add(text1)
db.session.commit()
#print("".join(l))
#    app.run(debug=True,host='0.0.0.0',port=9090)
