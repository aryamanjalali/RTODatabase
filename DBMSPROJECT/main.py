from flask import Flask,render_template,request,session,redirect,url_for,flash
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
import MySQLdb.cursors
import json


# MY db connection
app = Flask(__name__)
app.secret_key='secretkey'
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'vehicleregistration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/vehicleregistration"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# # this is for getting unique user access
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index2')
def index2():
    return render_template("index2.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/about2')
def about2():
    return render_template("about2.html")

@app.route('/registrations',methods=['GET', 'POST'])
def registrations():
    if request.method == 'POST':
        aadhaar_no = request.form['aadhaar_no']
        name = request.form['name']
        vehicle_no = request.form['vehicle_no']
        ph_no = request.form['ph_no']
        addr = request.form['addr']
        user_id = request.form['user_id']
        vehicle_type=request.form['vehicle_type']
        vehicle_name=request.form['vehicle_name']
        RTO_branch=request.form['RTO_branch']
        d_id=request.form['d_id']

        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO owner VALUES(%s,%s,%s,%s,%s,%s)''',(aadhaar_no,name,vehicle_no,ph_no,addr,user_id))
        cur.execute(''' INSERT INTO vehicle VALUES(%s,%s,%s,%s,%s)''',(vehicle_type,vehicle_no,vehicle_name,RTO_branch,d_id))

        mysql.connection.commit()

        cur.close()
        return render_template("index.html")
    return render_template("registrations.html")

@app.route('/registrations2',methods=['GET', 'POST'])
def registrations2():
    if request.method == 'POST':
        aadhaar_no = request.form['aadhaar_no']
        name = request.form['name']
        vehicle_no = request.form['vehicle_no']
        ph_no = request.form['ph_no']
        addr = request.form['addr']
        user_id = request.form['user_id']
        vehicle_type=request.form['vehicle_type']
        vehicle_name=request.form['vehicle_name']
        RTO_branch=request.form['RTO_branch']
        d_id=request.form['d_id']

        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO owner VALUES(%s,%s,%s,%s,%s,%s)''',(aadhaar_no,name,vehicle_no,ph_no,addr,user_id))
        cur.execute(''' INSERT INTO vehicle VALUES(%s,%s,%s,%s,%s)''',(vehicle_type,vehicle_no,vehicle_name,RTO_branch,d_id))

        mysql.connection.commit()

        cur.close()
        flash("Registration successful","error")
        return render_template("index2.html")
    
    return render_template("registrations2.html")


@app.route('/dealer',methods=['GET', 'POST'])
def dealer():
    if request.method == 'POST':
        d_name = request.form['d_name']
        ph_no = request.form['ph_no']
        d_id = request.form['d_id']
        addr = request.form['addr']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO dealer VALUES(%s,%s,%s,%s)''',(d_name,ph_no,d_id ,addr ))
        mysql.connection.commit()
        cur.close()
        return render_template("index.html")
    return render_template("dealer.html")

@app.route('/dealer2',methods=['GET', 'POST'])
def dealer2():
    if request.method == 'POST':
        d_name = request.form['d_name']
        ph_no = request.form['ph_no']
        d_id = request.form['d_id']
        addr = request.form['addr']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO dealer VALUES(%s,%s,%s,%s)''',(d_name,ph_no,d_id ,addr ))
        mysql.connection.commit()
        cur.close()
        return render_template("index2.html")
    return render_template("dealer2.html")

@app.route('/license',methods=['GET', 'POST'])
def license():
    if request.method == 'POST':
        aadhaar_no = request.form['aadhaar_no']
        validity = request.form['validity']
        license_no = request.form['license_no']
        cov = request.form['cov']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO license VALUES(%s,%s,%s,%s)''',(aadhaar_no,validity,license_no,cov))
        mysql.connection.commit()
        cur.close()
        return render_template("index.html")

    return render_template("license.html")

@app.route('/license2',methods=['GET', 'POST'])
def license2():
    if request.method == 'POST':
        aadhaar_no = request.form['aadhaar_no']
        validity = request.form['validity']
        license_no = request.form['license_no']
        cov = request.form['cov']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO license VALUES(%s,%s,%s,%s)''',(aadhaar_no,validity,license_no,cov))
        mysql.connection.commit()
        cur.close()
        return render_template("index2.html")

    return render_template("license2.html")

@app.route('/signup',methods=['post','get'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        pass1 = request.form['pass1']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO user VALUES(%s,%s)''',(email,pass1))
        mysql.connection.commit()
        cur.close()
        return render_template("login.html")
    return render_template("signup.html")

@app.route('/login',methods=['post','get'])
def login():
            if request.method == 'POST':
            
                username = request.form['username']
                password = request.form['password']
                cur = mysql.connection.cursor()
                cur.execute(f"select * from user where user_id='{username}'")
                cur.execute(''' INSERT INTO login VALUES(%s,%s)''',(username,password))
                mysql.connection.commit()
                cur.close()
                flash("Login successful", "success")
                return render_template("index2.html")
            return render_template('login.html')
            

@app.route('/Display',methods=['post','get'])
def Display():
    if request.method == 'POST':
                vehicle_type=request.form.get("vehicle_type")
                vehicle_no=request.form.get("vehicle_no")
                RTO_branch = request.form.get("RTO_branch")
                vehicle_name = request.form.get("vehicle_name")
                d_id = request.form.get("d_id")
                cur = mysql.connection.cursor()
                cur.execute(f"select * from vehicle")
                vehicles = cur.fetchall()
                mysql.connection.commit()
                # cur.execute(f"delete from vehicle where vehicle_no='{vehicle_no}'")
                # mysql.connection.commit()

                # cur.close()
                return render_template("profile2.html",vehicles=vehicles)

    return render_template("profile.html")


@app.route('/logout')
def logout():
    return render_template("index.html")

# @app.route('/Display2',methods=['post','get'])
# def Display2():
#     if request.method == 'POST':
            
#                 cur = mysql.connection.cursor()
#                 cur.execute(f"select * from vehicle")
#                 vehicles = cur.fetchall()
#                 mysql.connection.commit()
#                 cur.close()
#                 return render_template("new2.html",vehicles=vehicles)
#     return render_template("new.html")
    
    


if __name__== "__main__":
     app.run(debug=True) 



# @app.route('/login',methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         email = request.form.get("email")
#         password = request.form.get("password")
#         print(email)
#         print(password)
#         return redirect(url_for("index"))
#     return render_template("login.html")

# @app.route('/About')
# def user():
#     return render_template("about.html")

# @app.route('/pricing')
# def pricing():
#     return render_template("pricing.html")

# @app.route('/register')
# def register():
#     return render_template("register.html")