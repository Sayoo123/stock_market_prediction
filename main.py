from flask import Flask, render_template, request, session,redirect
from sklearn.tree import DecisionTreeClassifier
from pyspark.ml.feature import Imputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd,numpy as np
from sklearn import model_selection, svm
from DBConnection import Db
from email.mime import image
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key="hii"

@app.route("/", methods=['get', 'post'])
def login():
    if request.method == "POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db = Db()
        res=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if res is not None:
            res1=db.selectOne("select count(username) as c from login where type='user'")
            session['c']=res1['c']
            res2=db.selectOne("select count(c_id) as c from complaint")
            session['c1']=res2['c']
            session['lin']="1"
            if res['type']=='admin':
                return redirect('/admin_home')
            elif res['type']=='user':
                session['e'] = username
                q4=db.selectOne("select * from user where user_id='"+str(res['login_id'])+"'")
                session['n'] = q4['user_name']
                session['lid']=res['login_id']
                return redirect('/user_uhome')
            else:
                return '''<script>alert("incorrect passwor");window.location="/"</script>'''
        else:
            return '''<script>alert("incorrect password");window.location="/"</script>'''
    else:

        return render_template("login.html")

@app.route("/forgt", methods=['get', 'post'])
def forgt():
    if request.method == "POST":
        username=request.form['textfield']
        db = Db()
        res=db.selectOne("select * from login where username='"+username+"'")
        if res is not None:

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('vvrr2731@gmail.com', 'ajay1490')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your Password  is " + str(res['password']))

            msg['Subject'] = 'Verification'

            msg['To'] = username

            msg['From'] = 'vvrr2731@gmail.com'

            try:

                gmail.send_message(msg)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))
            return '''<script>alert("Check your mail!!!");window.location="/"</script>'''



        else:
            return '''<script>alert("Incorrect email");window.location="/forgt"</script>'''
    else:

        return render_template("forgot.html")

@app.route("/admin_home")
def admin_home():
    if session['lin']=='1':
        return render_template("admin/home.html")
    else:
        return redirect('/')

@app.route("/logout")
def logout():
    session['lin']="0"
    return redirect('/')




@app.route("/adm_send_notification", methods=['get', 'post'])
def adm_send_notification():
    if session['lin'] == '1':
        if request.method=="POST":
            notification=request.form['textarea']
            db=Db()
            db.insert("insert into notification(notification,n_date) values ('"+notification+"',curdate())")
            return "<script>alert('Notification added');window.location='/adm_send_notification'</script>"
        else:
            return render_template("admin/send_notification.html")
    else:
        return redirect('/')

@app.route("/adm_send_reply/<c_id>", methods=['get','post'])
def adm_send_reply(c_id):
    if session['lin'] == '1':
        if request.method == "POST":
            notification = request.form['textarea']
            db=Db()
            db.update("update complaint set reply='"+notification+"', r_date=curdate() where c_id='"+ c_id +"'")
            return "<script>alert('Replied successfully');window.location='/adm_view_complaints'</script>"
        else:
            return render_template("admin/send_reply.html")
    else:
        return redirect('/')

@app.route("/adm_view_complaints")
def adm_view_complaint():
    if session['lin'] == '1':
        db=Db()
        res=db.select("select * from user,complaint where user.user_id = complaint.user_id and reply='pending'")
        return render_template("admin/view_complaints.html", data=res)
    else:
        return redirect('/')

@app.route("/adm_view_feedback")
def adm_view_feedback():
    if session['lin'] == '1':
        db=Db()
        res=db.select("select * from user,feedback where user.user_id = feedback.user_id")
        return render_template("admin/view_feedback.html", data=res)
    else:
        return redirect('/')

@app.route("/adm_view_notification")
def adm_view_notification():
    if session['lin'] == '1':
        db=Db()
        res=db.select("select * from notification")

        return render_template("admin/view_notification.html", data=res)
    else:
        return redirect('/')
@app.route("/adm_delete_notification/<n_id>")
def adm_delete_notification(n_id):
    if session['lin'] == '1':
        db=Db()
        db.delete("delete from notification where n_id='"+n_id+"'")
        return "<script>alert('deleted successfully');window.location='/adm_view_notification'</script>"
    else:
        return redirect('/')
@app.route("/adm_view_users")
def adm_view_users():
    if session['lin'] == '1':
        db=Db()
        res=db.select("select * from user")
        return render_template("admin/view_users.html", data=res)
    else:
        return redirect('/')


# ===================================================USER==========================================================================
@app.route("/user_registration", methods=['get', 'post'])
def user_registration():
    if request.method == "POST":
        db=Db()
        username=request.form['textfield']
        cr_password=request.form['textfield2']
        co_password=request.form['textfield3']
        dob = request.form['textfield4']
        phone = request.form['textfield6']
        email = request.form['textfield5']
        q3=db.selectOne("select year(curdate())-year('"+dob+"') as d")
        if q3['d']>=18:
            if cr_password == co_password:
                q2=db.selectOne("select * from login where username='"+email+"' ")


                if q2 is None:
                    res=db.insert("insert into login values('','"+email+"','"+co_password+"','user')")
                    db.insert("insert into user values('"+str(res)+"','"+username+"','"+phone+"','"+email+"','"+dob+"')")
                    return "<script>alert('USER added successfully');window.location='/'</script>"
                else:
                    return "<script>alert('USer already exist');window.location='/'</script>"


            else:
                return "<script>alert('Password Mismatch');window.location='/user_registration'</script>"

        else:
            return "<script>alert('You are no eligible!! Please enther a valid date of birth');window.location='/user_registration'</script>"

    else:
        return render_template("user_registration.html")

@app.route("/user_uhome")
def user_uhome():
    if session['lin'] == '1':
        return render_template("user/uhome.html")
    else:
        return redirect('/')

@app.route("/user_index")
def curren():
    if session['lin'] == '1':
        return render_template("user/index.html")
    else:
        return redirect('/')

@app.route("/usr_send_complaint", methods=['get', 'post'])
def send_complaint():
    if session['lin'] == '1':

        if request.method == "POST":
            complaint = request.form['textarea']
            db=Db()
            db.insert("insert into complaint(c_id,user_id,complaints,c_date,reply,r_date) values('','"+str(session['lid'])+"','"+complaint+"',curdate(),'pending','pending' )")
            return "<script>alert('successfully send');window.location='/user_uhome'</script>"
        else:
            return render_template("user/send_complaint.html")
    else:
        return redirect('/')
@app.route("/usr_view_reply")
def view_reply():
    if session['lin'] == '1':
        db=Db()
        res=db.select("select c_id,complaints,reply,r_date from complaint where user_id='"+str(session['lid'])+"'")
        return render_template("user/view_reply.html",data=res)
    else:
        return redirect('/')

@app.route("/usr_send_feedback",methods=['get','post'])
def send_feedback():
    if session['lin'] == '1':

        if request.method == "POST":
            db = Db()
            feedback = request.form['textarea']
            db.insert("insert into feedback (feedback,f_date,user_id,f_id )values('"+feedback+"',curdate(),'"+str(session['lid'])+"','')")
            return "<script>alert('successfully send');window.location='/user_uhome'</script>"
        else:
            return render_template("user/send_feedback.html")
    else:
        return redirect('/')
@app.route("/usr_view_profile")
def view_profile():
    if session['lin'] == '1':
        db=Db()
        res = db.selectOne("select * from user where user_id='"+str(session['lid'])+"'")
        return render_template("user/view_profile.html", data=res)
    else:
        return redirect('/')
@app.route("/usr_view_notification")
def view_notification():
    if session['lin'] == '1':
        db=Db()
        res = db.select("select * from notification ")
        return render_template("user/view_notification.html", data=res)
    else:
        return redirect('/')

@app.route("/a")
def sa():
    if session['lin'] == '1':

        return render_template("admin/index.html")
    else:
        return redirect('/')




@app.route('/prediction',methods=['get','post'])
def prediction():
    if session['lin'] == '1':
        if request.method=='POST':
            t1=request.form['t1']
            t2=request.form['t2']
            t3=request.form['t3']
            t4=request.form['t4']
            t5=request.form['t5']
            csv=pd.read_csv("D:\\stock_market_prediction\\static\\google2.csv")
            attributes = csv.values[:, 1:6]  # X
            labels = csv.values[:, 7]  # Y
            ar = []
            ar.append(t1)
            ar.append(t2)
            ar.append(t3)
            ar.append(t4)
            ar.append(t5)
            arr = []
            test_val = np.array(ar)
            arr.append(test_val)
            randomforest = RandomForestClassifier(random_state=0)
            randomforest.fit(attributes, labels)
            c = randomforest.predict(arr)
            decisiontree = DecisionTreeClassifier()
            decisiontree = decisiontree.fit(attributes, labels)
            predict = decisiontree.predict(arr)
            clf = svm.SVC()
            clf.fit(attributes, labels)
            p=clf.predict(arr)
            return render_template("user/prediction.html",d1=c,d2=predict,d3=p,d4="1")
        return render_template("user/prediction.html")
    else:
        return redirect('/')
if __name__ == '__main__':
    app.run()