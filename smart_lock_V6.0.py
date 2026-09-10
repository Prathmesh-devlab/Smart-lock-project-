from flask import Flask,request,render_template
app=Flask(__name__)
import csv
import re

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

#All passwords of members are store here
passcode={}
class Passcode :
  # All passwords will load from csv file and add to passcode{}
  with open("members.csv") as file :
      csv_reader=csv.DictReader(file)
      for row in csv_reader :
        password=row["password"].strip()
        name=row["name"].strip()
        passcode[password]=name

@app.route("/", methods=["post","get"])
def index():
    return render_template("smart_lock.html")

@app.route("/test", methods=["POST"])
def test():
      Password=request.form.get("password")
      if Password in passcode:
         name=passcode.get(Password)
         return render_template("pass.html",Name=name)
      else :
        return render_template("fail.html")

@app.route("/attempt", methods=["post"])
def attempt():
    return render_template("attempt.html")

@app.route("/add", methods=["post"])
def add():
   return render_template("add.html")

@app.route("/member", methods=["post"])
def member():
     nam=request.form.get("name")
     matches=re.match(r"[a-z]+[^0-9]$",nam,flags=re.IGNORECASE)
     if matches :
        code=request.form.get("Password")
        with open("members.csv", "a") as file :
                member=csv.DictWriter(file, fieldnames=("password","name"))
                member.writerow({"password":code,"name":nam})
                passcode[code]=nam  
        return render_template("successfull.html")
     else:
        return render_template("error.html")   
  
@app.route("/guest", methods=["post"])
def guest():
   return render_template("guest.html")

@app.route("/guest_details", methods=["post"])
def details():
    name=request.form.get("name")
    mobile=request.form.get("mobile")
   # All guests list will load from csv file and add to guest{}
    with open("guests.csv" , "a") as file :
         GUEST=csv.DictWriter(file, fieldnames=("name","mobile"))
         GUEST.writerow({"name": name , "mobile" : mobile})
    return render_template("thankyou.html")

@app.route("/admin", methods=["post"])
def admin():
    return render_template("access.html")

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