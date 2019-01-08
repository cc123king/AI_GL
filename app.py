from flask import Flask,render_template,request,session
import flask_bootstrap,time
from flask_sqlalchemy import SQLAlchemy
from yzm import dr

app = Flask(__name__)
app.secret_key='a5s1d3q7s.d-1qdf152'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:15370040@127.0.0.1/AI_gl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
flask_bootstrap=flask_bootstrap.Bootstrap(app)

class user(db.Model):
    __tablename__='users'
    usename=db.Column(db.String(12),primary_key=True)
    password=db.Column(db.String(20))

@app.route('/')
def hello_world():
    return render_template('index.html')

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
        if list1.password !=password:
            l=dr()
            return 'error2'
        else:
            session['user']=users
            l=dr()
            return 'OK'
@app.route('/updates',methods=['POST'])
def updates():
    old_passowrd=request.form.get('old_password')
    new_password=request.form.get('new_password')
    re_new_password=request.form.get('re_new_password')
    str0 =db.session.query(user).filter(user.usename=='admin').first()
    if old_passowrd !=str0.password:
        return 'error1'
    elif new_password !=re_new_password:
        print(new_password)
        print(re_new_password)
        return 'error2'
    else:
        str0.password=new_password
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
if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    user1=user(usename='admin',password='admin')
    db.session.add(user1)
    db.session.commit()
    l = dr()
    print("".join(l))
    app.run(debug=True,host='0.0.0.0',port=9090)
