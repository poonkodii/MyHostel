from flask import Flask
from flask import request, render_template, url_for
from flaskext.mysql import MySQL

import smtplib

app = Flask(__name__)
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pop'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


@app.route('/')
def hello_world():
    return render_template('kct_leave_home.html')


@app.route('/about', methods=["POST"])
def goo():
    return render_template('about.html')


@app.route('/hodd', methods=["POST"])
def hoddd():
    return render_template('hodlogin.html')


@app.route('/hodlogin', methods=["POST"])
def lohhh():
    return render_template('hodlog.html')


@app.route('/hodlog', methods=["POST"])
def lggy():
    u = request.form['username']
    p = request.form['password']
    if (u == 'devaki' and p == '123'):
        db = mysql.connect()
        cursor = db.cursor()
        query = "select roll_no,ldate,rdate,lt,reason from work_leave where hod_status ='1' "
        c = cursor.execute(query)
        c = cursor.fetchall()
        db.commit()
        db.close()

        return render_template('hodapprove.html', rows=c)
    else:
        return "invalid username or password"


@app.route('/hodapp', methods=["POST"])
def hodappp():
    db = mysql.connect()
    cursor = db.cursor()
    rollno = request.form['rollno']
    stat = request.form['stat']
    query = ("update work_leave set hod_status='%s' where roll_no='%s'") % (stat, rollno)
    cursor.execute(query)
    query = "select roll_no,ldate,rdate,lt,reason from work_leave where hod_status = '1'  "
    c = cursor.execute(query)
    c = cursor.fetchall()
    db.commit()
    db.close()
    return render_template('hodapprove.html', rows=c)


@app.route('/gym', methods=["POST"])
def gymm():
    return render_template('gymregister.html')


@app.route('/workday', methods=["POST"])
def workk():
    return render_template('workform.html')


@app.route('/leaveit', methods=["POST"])
def req():
    db = mysql.connect()
    cursor = db.cursor()
    email = request.form['email']
    ee = request.form['ldate']
    fi = request.form['ltime']
    er = request.form['rdate']
    ll = request.form['rtime']
    ej = request.form['lt']
    rh = request.form['reason']
    cursor.execute("SELECT roll_no from student where email='" + email + "'")
    c = cursor.fetchone()[0]
    cursor.execute("SELECT pmobileno from student where email='" + email + "'")
    d = cursor.fetchone()[0]
    cursor.execute("SELECT parent from student where email='" + email + "'")
    e = cursor.fetchone()[0]
    cursor.execute("SELECT pmail from student where email='" + email + "'")
    f = cursor.fetchone()[0]
    cursor.execute("SELECT name from student where email='" + email + "'")
    g = cursor.fetchone()[0]

    query = "insert into work_leave (name,roll_no,email,ldate,ltime,rdate,r,lt,reason,parent,pmail,pno) values('%s','%s' ,'%s','%s','%s' ,'%s','%s','%s' ,'%s','%s','%s' ,'%s')" % (
        g, c, email, ee, fi, er, ll, ej, rh, e, f, d)

    cursor.execute(query)
    db.commit()
    db.close()
    return render_template('homepage.html')


@app.route('/gymreg', methods=["POST"])
def gymregister():
    name = request.form['name']
    rol = request.form['rol']
    dep = request.form['dep']
    time = request.form['time']
    email = request.form['email']
    db = mysql.connect()
    cursor = db.cursor()
    query = "insert into gym (name,roll_no,email,dep,time) values('%s' ,'%s','%s' ,'%s','%s')" % (
    name, rol, email, dep, time)
    c = cursor.execute(query)
    db.commit()
    db.close()
    return render_template('homepage.html')


@app.route('/change', methods=["POST"])
def chg():
    return render_template('passchange.html')


@app.route('/passchg', methods=["POST"])
def paschg():
    rollno = request.form['rollno']
    old = request.form['old']
    new = request.form['new']
    newp = request.form['newp']
    if (new == newp):
        db = mysql.connect()
        cursor = db.cursor()
        query = ("update student  set password='%s' where roll_no = '%s'") % (new, rollno)
        cursor.execute(query)

        db.commit()
        db.close()
    return "password changed"


@app.route('/holiday', methods=["POST"])
def hols():
    return render_template('holiday_leave.html')


@app.route('/leave_db', methods=["POST"])
def holi_db():
    db = mysql.connect()
    cursor = db.cursor()
    email = request.form['email']
    ee = request.form['ldate']
    fi = request.form['ltime']
    er = request.form['rdate']
    ll = request.form['rtime']
    ej = request.form['lt']
    rh = request.form['reason']
    cursor.execute("SELECT roll_no from student where email='" + email + "'")
    c = cursor.fetchone()[0]
    cursor.execute("SELECT pmobileno from student where email='" + email + "'")
    d = cursor.fetchone()[0]
    cursor.execute("SELECT parent from student where email='" + email + "'")
    e = cursor.fetchone()[0]
    print e
    cursor.execute("SELECT pmail from student where email='" + email + "'")
    f = cursor.fetchone()[0]
    cursor.execute("SELECT name from student where email='" + email + "'")
    g = cursor.fetchone()[0]

    query = "insert into holi_leave (name,roll_no,email,ldate,ltime,rdate,rtime,lt,reason,parent,pmail,pno) values('%s','%s' ,'%s','%s','%s' ,'%s','%s','%s' ,'%s','%s','%s' ,'%s')" % (
    g, c, email, ee, fi, er, ll, ej, rh, e, f, d)
    cursor.execute(query)
    db.commit()
    db.close()

    return render_template('leave.html')


@app.route('/stat', methods=["POST"])
def nnn():
    return render_template('stat.html')


@app.route('/holi_status', methods=["POST"])
def poli():
    return render_template('holi_stat.html')


@app.route('/work_status', methods=["POST"])
def goku():
    return render_template('work_stat.html')


@app.route('/work_stat', methods=["POST"])
def pyaar():
    db = mysql.connect()
    cursor = db.cursor()
    rollno = request.form['rollno']
    late = request.form['ldate']

    query1 = "select hod_status from work_leave where roll_no = '%s' and ldate = '%s'" % (rollno, late)
    cursor.execute(query1)
    g = cursor.fetchone()[0]

    query2 = "select swo_status from work_leave where roll_no = '%s' and ldate = '%s'" % (rollno, late)
    cursor.execute(query2)
    n = cursor.fetchone()[0]

    if (g == "APPROVED" and n == "APPROVED"):
        status = 'LEAVE GRANTED'
        query3 = "update work_leave set status = '%s' where roll_no ='%s' and ldate = '%s' " % (status, rollno, late)
        cursor.execute(query3)
        db.commit()


    else:
        statusw = 'LEAVE NOT PERMITTED'
        query3 = "update work_leave set status = '%s' where roll_no ='%s' and ldate = '%s' " % (statusw, rollno, late)
        cursor.execute(query3)
        db.commit()

    query = "select roll_no,ldate,rdate,lt,reason,hod_status,swo_status,status from work_leave where roll_no = '%s' and ldate = '%s' " % (
    rollno, late)
    d = cursor.execute(query)
    d = cursor.fetchall()

    db.commit()
    db.close()
    return render_template('workcheck.html', rows=d)


@app.route('/passretrive', methods=["POST"])
def passwordretrieve():
    rollno = request.form['rollno']
    email = request.form['email']
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute("SELECT password  from student where roll_no='" + rollno + "' and email='" + email + "'")
    c = str(cursor.fetchone())
    print c
    db.commit()

    username = "poonkodithanapal@gmail.com"
    password = ""#your gmail password
    fromaddr = "poonkodithanapal@gmail.com"
    toaddrs = email
    msg = c
    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()

    server.login(username, password)

    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return "successful"


@app.route('/student', methods=["POST"])
def stud():
    return render_template('studenten.html')


@app.route('/studentlogin', methods=["POST"])
def studlogin():
    return render_template('kct.html')


@app.route('/studentsignup', methods=["POST"])
def studsign():
    return render_template('studentsignup.html')


@app.route('/food', methods=["POST"])
def food():
    return render_template('food.html')


@app.route('/passret', methods=["POST"])
def helo():
    return render_template('password.html')


@app.route('/foods', methods=["POST"])
def foods():
    fromaddr = 'poonkodithanapal@gmail.com'
    toaddrs = 'kpritheka@gmail.com'

    dep = request.form['dep']
    rol = request.form['roll']
    msg = request.form['msg']
    username = 'poonkodithanapal@gmail.com'
    password = ''# your gmail password

    db = mysql.connect()
    cursor = db.cursor()
    query = "insert into mess (message,department,roll_no) values('%s','%s' ,'%s')" % (msg, dep, rol)
    c = cursor.execute(query)
    db.commit()
    db.close()
    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()

    server.login(username, password)

    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return "THANK YOU!! YOUR RESPONSE IS SUBMITTED"


@app.route('/gymdet', methods=["POST"])
def gymdata():
    db = mysql.connect()
    cursor = db.cursor()
    query = "select * from gym"
    c = cursor.execute(query)
    c = cursor.fetchall()
    for row in c:
        name = row[0]
        roll_no = row[1]
        email = row[2]
        dep = row[3]
        time = row[4]

    db.commit()
    db.close()
    return render_template('test3.html', rows=c)


@app.route('/leavee', methods=["POST"])
def gu():
    return render_template('leave.html')


@app.route('/students', methods=["POST"])
def stu():
    username = request.form['username']
    email = request.form['email']
    dep = request.form['dep']
    block = request.form['block']
    roomno = request.form['roomno']
    mobileno = request.form['phno']
    rollno = request.form['rollno']
    pname = request.form['pname']
    pmob = request.form['pmob']
    pmail = request.form['pmail']
    create_pass = request.form['pass']
    password = request.form['passw']
    if (create_pass == password):
        db = mysql.connect()
        cursor = db.cursor()
        query = "insert into student (name, email,department,block, room_no,mobile_no,roll_no,password,parent,pmail,pmobileno) values('%s' ,'%s','%s' ,'%s','%s','%s','%s','%s','%s','%s','%s')" % (
        username, email, dep, block, roomno, mobileno, rollno, password, pname, pmail, pmob)
        c = cursor.execute(query)
        db.commit()
        db.close()
    return render_template('homepage.html')


@app.route('/staff', methods=["POST"])
def staff():
    return render_template('staffen.html')


@app.route('/stafflogin', methods=["POST"])
def stafflogin():
    return render_template('stafflogin.html')


@app.route('/staffsignup', methods=["POST"])
def ssignup():
    return render_template('staffsignup.html')


@app.route('/mess', methods=["POST"])
def mess():
    return render_template('mess.html')


@app.route('/admin', methods=["POST"])
def admin():
    return render_template('admin.html')


@app.route('/messdet', methods=["POST"])
def messdetails():
    db = mysql.connect()
    cursor = db.cursor()
    query = "select * from mess"
    c = cursor.execute(query)
    c = cursor.fetchall()

    db.commit()
    db.close()
    return render_template('test.html', rows=c)


@app.route('/staffsignupsubmit', methods=["POST"])
def staffdet():
    username = request.form['username']
    staff_email = request.form['email']
    dep = request.form['dep']
    emp_code = request.form['idw']
    if (len(emp_code) != 6):
        return "false"
    create_pass = request.form['pass']
    password = request.form['passw']
    if (create_pass == password):
        db = mysql.connect()
        cursor = db.cursor()
        query = "insert into staff (name, email,emp_code,dep, password) values('%s' ,'%s','%s' ,'%s','%s')" % (
        username, staff_email, emp_code, dep, password)
        c = cursor.execute(query)
        db.commit()
        db.close()
        return render_template('stafflsubmitt.html')
    else:
        return "your password doesn't match !!"


@app.route('/staffhome', methods=["POST"])
def staffhome():
    return render_template('staffhome.html')


@app.route('/staffloginsubmit', methods=['POST'])
def stafflogsin():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from staff where name='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return "Username or password is invalid or your account is invalid"
    else:

        return render_template('swo.html')


@app.route('/worksubmit', methods=["POST"])
def wrokky():
    db = mysql.connect()
    cursor = db.cursor()
    query = "select roll_no,ldate,rdate,lt,reason,hod_status from work_leave where swo_status ='1' "
    c = cursor.execute(query)
    c = cursor.fetchall()
    db.commit()
    db.close()

    return render_template('stafflsubmit.html', rows=c)


@app.route('/holisubmit', methods=["POST"])
def hilo():
    db = mysql.connect()
    cursor = db.cursor()
    query = "select roll_no,ldate,rdate,lt,reason from holi_leave where status ='1' "
    c = cursor.execute(query)
    c = cursor.fetchall()
    db.commit()
    db.close()

    return render_template('stafflsubmitt.html', rows=c)


@app.route('/approved', methods=['POST'])
def desc():
    db = mysql.connect()
    cursor = db.cursor()
    rollno = request.form['rollno']
    stat = request.form['stat']
    query = ("update holi_leave set status='%s' where roll_no='%s'") % (stat, rollno)
    cursor.execute(query)
    query = "select roll_no,ldate,rdate,lt,reason from holi_leave where status = '1'  "

    c = cursor.execute(query)
    c = cursor.fetchall()
    db.commit()
    db.close()
    return render_template('stafflsubmit.html', rows=c)


@app.route('/approve', methods=["POST"])
def heee():
    db = mysql.connect()
    cursor = db.cursor()
    rollno = request.form['rollno']
    stat = request.form['stat']
    query1 = "select hod_status from work_leave where roll_no ='%s'" % (rollno)
    cursor.execute(query1)
    query2 = ("update work_leave set swo_status ='%s' where roll_no ='%s' ") % (stat, rollno)
    cursor.execute(query2)
    query3 = "select roll_no,ldate,rdate,lt,reason,hod_status from work_leave where swo_status = '1' "
    cursor.execute(query3)
    v = cursor.fetchall()
    db.commit()
    db.close()
    return render_template('stafflsubmit.html', rows=v)


@app.route('/status', methods=['POST'])
def good():
    db = mysql.connect()
    cursor = db.cursor()
    rollno = request.form['rollno']
    query = "select roll_no,ldate,rdate,lt,reason,status from holi_leave where roll_no = '%s'  " % (rollno)
    d = cursor.execute(query)
    d = cursor.fetchall()
    db.commit()
    db.close()
    return render_template('holicheck.html', rows=d)


@app.route('/mail')
def mail():
    fromaddr = 'poonkodithanapal@gmail.com'

    toaddrs = 'pk@gmail.com'
    msg = 'mmma!'
    username = 'poonkodithanapal@gmail.com'
    password = ''# your gmail password

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()

    server.login(username, password)

    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return "<h1>sucess</h1>"


@app.route('/logout', methods=['POST'])
def loggy():
    return render_template('kct_leave_home.html')


@app.route('/studentdet', methods=["POST"])
def studdet():
    db = mysql.connect()
    cursor = db.cursor()
    query = "select name,email,department,room_no,mobile_no,roll_no from student"
    c = cursor.execute(query)
    c = cursor.fetchall()
    for row in c:
        name = row[0]
        email = row[1]
        department = row[2]
        room_no = row[3]
        mobile_no = row[4]
        roll_no = row[5]

    db.commit()
    db.close()
    return render_template('test1.html', rows=c)


@app.route('/staffdet', methods=["POST"])
def staffdets():
    db = mysql.connect()
    cursor = db.cursor()
    query = "select name,email,emp_code,dep from staff"
    c = cursor.execute(query)
    c = cursor.fetchall()
    for row in c:
        name = row[0]
        email = row[1]
        dep = row[2]
        emp_code = row[3]
    db.commit()
    db.close()
    return render_template('test2.html', rows=c)


@app.route('/submit', methods=["POST"])
def submit():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from student where roll_no='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return "Username or password is invalid or your account is invalid"
    else:
        return render_template('homepage.html')


@app.route('/signup', methods=["POST"])
def signup():
    n = request.form['name']

    cr_pass = request.form['pass']
    p = request.form['password']
    if (cr_pass == p):
        db = mysql.connect()
        cursor = db.cursor()
        query = "insert into student_det (name, password) values('%s' ,'%s')" % (n, p)
        c = cursor.execute(query)
        db.commit()
        db.close()
        return "password changed"
    else:
        return "incorrect password"


if __name__ == '__main__':
    app.run(host="localhost", port=8090, debug=True)
