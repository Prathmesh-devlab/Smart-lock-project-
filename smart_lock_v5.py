''' V5 Features :-
persistant storage for members
save all data of guest and members permanantly
more secure
password is not reveal in code it is hide inside csv file
rest all features of V4 are included
'''
import csv
# All passwords will load from csv file and store here
passcode={}
with open("members.csv") as file :
        csv_reader=csv.DictReader(file)
        for row in csv_reader :
           password=row["password"].strip()
           name=row["name"].strip()
           passcode[password]=name
# All guest will load from csv file and store here
guest={}
with open("guests.csv") as file :
        csv_reader=csv.DictReader(file)
        for row in csv_reader :
          mobile=row["mobile no."].strip()
          name=row["name"].strip()
          guest[name]=mobile
# In this block new member will be added and store in csv file
def add() :
    b=input("Enter security code")
    if b.strip().lower()=="add@123" :
        print("Add member")
        nam=input("Enter your name")
        code=input("Set new pasword").strip()
        with open("members.csv", "a") as file :
               member=csv.DictWriter(file, fieldnames=("password","name"))
               member.writerow({"password":code,"name":nam})  
        passcode[code]=nam  
        print("sucessfully added")
    else :
        print("Wrong security code")
# This is Admin mode which contain all admin rights
def admin() :
    admin=input("Enter Admin Mode yes/no")
    if admin.strip().lower()=="yes" :
        passcode=input("Enter Admin Code")
        if passcode.strip().lower()=="santosh@123" :
            print("Admin mode access granted")
            member=input("Add member yes/no")
            if member.strip().lower()=="yes" :
                add()
            else :
                a=input("See guest which visited house yes/no")
                print(guest)
        else :
            print("Access Denied")

b=input("Are you guest yes/no")
if b.lower().strip()=="yes" :
 # In this block guest details will be taken and stored in csv file
     name=input("What's your name")
     mobile=input("Enter your mobile no.")
     with open("guests.csv" , "a") as file :
         guest=csv.DictWriter(file, fieldnames=("name","mobile"))
         guest.writerow({"name": name , "mobile" : mobile})
     print("welcome to home",name, "but currently there is no one at home")
# Pasword checking and attempt countering
else :
    i=3
    while i>0:
         if i>0 :
              try :
                 a=input("Enter password")
                 if a.strip().lower()=="exit" :
                    admin()
                    break
                 else :
                    print("welcome",passcode[a.strip()])
                    break
              except KeyError :
               print("Incorrect password you have only",i-1,"attempts")
               i=i-1
         else :
            print("error")