from flask import Flask, render_template, request, redirect
from datetime import *
from flask_mysqldb import MySQL
import mysql.connector

global count
app = Flask(__name__, template_folder="template", static_folder="static")

# configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1417'
app.config['MYSQL_DB'] = 'bus_transportation_system'

mysql = MySQL(app)

user_login = 0
@app.route('/')
def home():
    # if(user_login == 1):
    #     cur = mysql.connection.cursor()
    #     cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
    #     name1=cur.fetchone()
    #     for i in name1:
    #         disp_name = i
    #     return render_template('index.html',welcome = 'Welcome',user = display_name,exc = '!')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post', methods = ['GET','POST'])
def post():
    count = 0
    if count == 0:
        # count = 1
        cur = mysql.connection.cursor()
        fromValue = cur.execute("SELECT DISTINCT(b_from) FROM buses")
        if fromValue > 0:
            fromDetails = cur.fetchall()
        toValue = cur.execute("SELECT DISTINCT(b_to) FROM buses")
        if toValue > 0:
            toDetails = cur.fetchall()

        if request.method == 'POST':
            #add entry
            global fromu
            global tou
            global deptu
            global get_date
            global getdatetime
            global format_str

            departure = request.form.get("departure")
            fromm = request.form.get("from",None)
            too = request.form.get("to",None)
            name = request.form.get("name",None)

            if departure != None and len(departure)!=0 :
                deptu = departure
                format_str = '%Y-%m-%d'
                get_date = datetime.strptime(deptu,format_str)
                getdatetime = get_date
            if fromm != None:
                fromu = fromm
            if too != None:
                tou = too
            


            if count == 0:
                # cur = mysql.connection.cursor()
                resultValue = cur.execute("SELECT * FROM buses where b_from = %s and b_to = %s",(fromu,tou))
                count= count + 1



            if resultValue == 0 and count ==1:
                return render_template('post.html',not_found='Oops! Buses aren\'t available')
            if resultValue > 0 and count == 1:
                userDetails = cur.fetchall()
                count = count + 1
                
                if count == 2 and name!=None :
                    finale = cur.execute("SELECT bus_id FROM buses where b_from = %s and b_to = %s and bus_name = %s",(fromu,tou,name))
                    busid = cur.fetchone()
                    for i in busid:
                        busidd = i
                        # print(i)
                    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
                    name1=cur.fetchone()
                    for i in name1:
                        userid = i
        
                    cur.execute("INSERT into bookings(user_id,bus_id,depart,bk_from,bk_to) VALUES(%s,%s,%s,%s,%s)",(userid,busidd,getdatetime,fromu,tou))
                    mysql.connection.commit()
                    return redirect("/mybookings")
                return render_template('post.html',userDetails = userDetails)
        return render_template('post.html',fromDetails=fromDetails,toDetails=toDetails)
    return render_template('post.html')


@app.route('/contact', methods = ['GET','POST'])
def contact():
    if(request.method == 'POST'):
        #add entry
        userDetails = request.form
        name = userDetails['name']
        if len(name)==0:
            return render_template("invalid.html",error_msg="No Name",error_msg2="You did not enter the name")
        email = userDetails['email']
        if len(email)==0:
            return render_template("invalid.html",error_msg="No Email",error_msg2="You did not enter the Email")
        phone = userDetails['phone']
        if len(phone)==0:
            return render_template("invalid.html",error_msg="No Number",error_msg2="You did not enter the Phone Number")
        message = userDetails['message']
        if len(message)==0:
            return render_template("invalid.html",error_msg="No message",error_msg2="You did not enter the Message")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact(name,email,phone,msg) VALUES(%s,%s, %s,%s)",(name,email,phone,message))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    return render_template('contact.html')

@app.route('/signin', methods = ['GET','POST'])
def signin():
    if(request.method == 'POST'):
        userDetails = request.form
        email = userDetails['email']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        
        cur.execute("SELECT email from users")
        emails = cur.fetchall()
        size = len(emails)

        if len(email) == 0:
            return render_template('invalid.html',error_msg = 'No Email',error_msg2 = 'You cannot leave email blank!')
            # return "NO EMAIL"
        if len(password) == 0:
            return render_template('invalid.html',error_msg = 'No Password',error_msg2 = 'You did not enter your password!')
            # return "NO PASSWORD"

        email_flag = 0
        pass_flag = 0
        
        count = 0
        cur.execute("SELECT email,password,user_id from users")

        sum = cur.fetchone()
        for i in range(size):
            for j in sum:
                temp = j
                if email == temp:
                    email_flag = 1
                if password == temp:
                    pass_flag = 1
                if pass_flag == 1 and email_flag == 1:
                    if count == 0 :
                        count=1
                        # print(count)
                        cur.execute("SELECT user_id FROM users where email = %s",[email])
                        busid = cur.fetchone()
                        for k in busid:
                            userid = k
                            # print(count)
                            # userid = temp
                        cur.execute("SELECT email,password,user_id from users")
                    users = temp    
                    # print(userid)
            sum = cur.fetchone()

        if email_flag == 1 and pass_flag == 1:
            cur.execute("SELECT user_id from admin")
            sum = cur.fetchone()
            # for i in range(size):
            for j in sum:
                temp = j
                # print(j)
            sum = cur.fetchone()
            # print(userid)
            if temp == userid:
                cur.execute("INSERT INTO signin(user_id,email) VALUES (%s,%s)",(userid,email))
                mysql.connection.commit()
                cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
                name1=cur.fetchone()
                for i in name1:
                    disp_name = i
                cur.close()
                return render_template('admin.html',welcome = 'Welcome',user = disp_name,exc = '!')


            cur.execute("INSERT INTO signin(user_id,email) VALUES (%s,%s)",(userid,email))
            cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
            name1=cur.fetchone()
            for i in name1:
                disp_name = i
            mysql.connection.commit()
            cur.close()
            return render_template('index.html',welcome = 'Welcome',user = disp_name,exc = '!')
        
        if email_flag == 0:
            return render_template('invalid.html',error_msg = 'Incorrect_Email',error_msg2 = 'Oops! Please check your Email!')
        
        if pass_flag == 0:
            return render_template('invalid.html',error_msg = 'Incorrect_Password',error_msg2 = 'Oops! Please check your Password!')
    return render_template('login.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if(request.method == 'POST'):
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        password = userDetails['password']

        if len(name) == 0:
            return render_template('invalid.html',error_msg = 'No Name' ,error_msg2 = 'Name cannot be empty')
        if len(email) == 0:
            return render_template('invalid.html',error_msg = 'No Email',error_msg2 = 'Email cannot be empty')
            return "NO EMAIL"
        if len(password) == 0:
            return render_template('invalid.html',error_msg = 'No Password', error_msg2 = 'Password Cannot be empty')
            return "NO PASSWORD"

        cur = mysql.connection.cursor()
        cur.execute("SELECT MAX(user_id) from users")
        id = cur.fetchone()
        for i in id:
            user_id = i
        user_id = user_id + 1
        user_login = 1
        signup_login = user_login
        cur.execute("INSERT INTO users(user_id,name,email,password) VALUES(%s,%s,%s, %s)",(user_id,name,email,password))
        cur.execute("INSERT INTO signin(user_id,email)  VALUES(%s, %s)",(user_id,email))
        cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
        name2=cur.fetchone()
        for i in name2:
            display_name = i
        mysql.connection.commit()
        cur.close()
        return render_template('index.html',welcome = 'Welcome',user = display_name,exc = '!')
    return render_template('signup.html')

@app.route('/mybookings')
def bookings():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM bookings where user_id in (SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin))")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('bookings.html',userDetails = userDetails )
    return render_template('bookings.html')

@app.route('/details')
def info():
    cur = mysql.connection.cursor()
    busValue = cur.execute("SELECT * FROM buses")
    if busValue > 0:
        busDetails = cur.fetchall()
    userValue = cur.execute("SELECT * FROM users")
    if userValue > 0:
        userDetails = cur.fetchall()
    bookingValue = cur.execute("SELECT * FROM bookings")
    if bookingValue > 0:
        bookDetails = cur.fetchall()
        return render_template('users.html',userDetails = userDetails,busDetails = busDetails, bookDetails = bookDetails )

@app.route('/edit', methods = ['GET','POST'])
def edit():
    if(request.method == 'POST'):
        userDetails = request.form
        name = request.form.get('name',None)
        bustype = request.form.get('bustype',None)
        bfrom = request.form.get('bfrom',None)
        to = request.form.get('place',None)
        fare = request.form.get('fare',None)
        busid = request.form.get('busid',None)

        print(name)
        print(bustype)
        print(bfrom)
        print(to)
        print(fare)
        print(busid)

        cur = mysql.connection.cursor()
        if name!= None and bustype != None and bfrom != None and to != None and fare!=None:
            cur.execute("INSERT INTO buses(bus_name,bus_type,b_from,b_to,fare) VALUES(%s,%s,%s,%s,%s)",(name,bustype,bfrom,to,fare))
            mysql.connection.commit()
            return render_template('admin.html')
        if busid!=None:
            cur.execute("DELETE from buses where bus_id = %s",(busid,))
            mysql.connection.commit()
            return render_template('admin.html')
        return render_template('admin.html')
    return render_template('edit.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
app.run(debug=True)
