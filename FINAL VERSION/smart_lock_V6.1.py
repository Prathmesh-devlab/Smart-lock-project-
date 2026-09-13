from cs50 import SQL
from werkzeug.security import check_password_hash,generate_password_hash
import csv
import re
from flask import Flask,render_template,request,session

app=Flask(__name__)
app.secret_key='your_secret_key_here'

#Load Database
db=SQL("sqlite:///members.db")
#("CREATE TABLE members(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE,hash TEXT NOT NULL)")

MAX_ATTEMPTS=3

#All guest that visited the house are store here
GUEST={}
class Guest:
   # All guests list will load from csv file and add to guest{}
   with open("guests.csv") as file :
      csv_reader=csv.DictReader(file)
      for row in csv_reader :
        mobile=row["mobile no."].strip()
        name=row["name"].strip()
        GUEST[name]=mobile

@app.route("/", methods=["post","get"])
def index():
    if 'attempts' not in session:
       session['attempts']=0
    if 'is_locked' not in session:
       session['is_locked']=False

    remaining=MAX_ATTEMPTS-session['attempts']
    return render_template("smart_lock.html",remaining=remaining, is_locked=session['is_locked'])

#Password checking and session handling
@app.route("/test", methods=["POST"])
def test():
    if 'attempts' not in session:
       session['attempts']=0
    if 'is_locked' not in session:
       session['is_locked']=False

    if session['is_locked']:
       return render_template("smart_lock.html", is_locked=True)
    
    Password=request.form.get("password")
 
    members=db.execute("SELECT * FROM members")
    match_user=None

    for i in members :
       if check_password_hash(i["hash"],Password):
          match_user=i
          break

    if match_user:
       name=match_user['username']
       session['attempts']=0
       session['is_locked']=False
       return render_template("pass.html",Name=name)
    else:
       session['attempts'] +=1

       if session['attempts']>MAX_ATTEMPTS:
         return render_template("smart_lock.html",error="Too many failed attempts.",is_locked=True)
       else:
          return render_template("fail.html")

#Re-attempting   
@app.route("/attempt", methods=["post"])
def attempt():
    remaining=MAX_ATTEMPTS-session['attempts']
    return render_template("attempt.html",warning=remaining)

@app.route("/add", methods=["post"])
def add():
   return render_template("add.html")

#Add new member
@app.route("/member", methods=["post"])
def member():
     nam=request.form.get("name")
     matches=re.match(r"[a-z]+[^0-9]$",nam,flags=re.IGNORECASE)
     if matches :
        code=request.form.get("Password")
        hash_password=generate_password_hash(code)
        db.execute("INSERT INTO members(username,hash) VALUES(?,?)",nam,hash_password)
        return render_template("successfull.html")
     else:
        return render_template("error.html")

@app.route("/guest", methods=["post"])
def guest():
   return render_template("guest.html")

#Store guest in GUEST{}
@app.route("/guest_details", methods=["post"])
def details():
    name=request.form.get("name")
    mobile=request.form.get("mobile")
    with open("guests.csv" , "a") as file :
         GUEST=csv.DictWriter(file, fieldnames=("name","mobile"))
         GUEST.writerow({"name": name , "mobile" : mobile})
    return render_template("thankyou.html")
     
@app.route("/admin", methods=["post"])
def admin():
    return render_template("access.html")

#Checking password for admin rights
@app.route("/check", methods=["post"])
def check():
    check=request.form.get("check")
    if check.strip()=="Admin@123":
        return render_template("rights.html")
    else:
        return render_template("denied.html")

@app.route("/list", methods=["post"])
def lists():
    return render_template("list.html",guests=GUEST)

#To reset the session
@app.route("/reset",methods=["post"])
def reset():
   session['attempts']=0
   session['is_locked']=False
   return render_template("smart_lock.html")

if __name__=="__main__": app.run(debug=True)