''' V5.2 Features :-
More strict checking on user's input 
Rest all features are same as V5
'''
import csv
import re

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

#All guest that visited the house are store here
guest={}
class Guest:
   # All guests list will load from csv file and add to guest{}
   with open("guests.csv") as file :
      csv_reader=csv.DictReader(file)
      for row in csv_reader :
        mobile=row["mobile"].strip()
        name=row["name"].strip()
        guest[name]=mobile

class add :
  def __init__(self,Member):
    self.Member=Member
  #New members are added here and store in passcode{}
  def Add(self) :
    #Verification of security code
    b=input("Enter security code").strip().lower()
    if b=="add@123" :
       print("Add member")
       i=10000
       while i>0 :
        nam=input("Enter your name").strip()
        matches=re.match(r"[a-z]+[^0-9]$",nam,flags=re.IGNORECASE)
        if matches :
           break
        else :
           print("Name should contain only characters")
           i=i-1
       x=10000
       while x>0 :
          code=input("Set new pasword").strip()
          matches=re.match(r"[^a-z][0-9]{4,6}+$",code,flags=re.IGNORECASE)
          if matches :
             #Added member is store in members.csv
             with open("members.csv", "a") as file :
                   member=csv.DictWriter(file, fieldnames=("password","name"))
                   member.writerow({"password":code,"name":nam})  
                   passcode[code]=nam  
                   print("sucessfully added")
                   break
          elif code.strip().lower()=="exit" :
              z=input("Are you sure want to exit yes/no")
              if z.lower().strip()=="yes" :
                  break
          else :
             print("Password can contain only numbers")
             x=x-1    
    else :
      print("Wrong security code")

#All admin rights
class Admin :
  def __init__(self,admin):
    self.admin=admin   
  def Admin(self) :
    admin=input("Enter Admin Mode yes/no")
    if admin.strip().lower()=="yes" :
      #Verification of admin code
      passcode=input("Enter Admin Code")
      if passcode.strip().lower()=="santosh@123" :
        print("Admin mode access granted")
        Member=input("Add member yes/no")
        #To add new member
        if Member.strip().lower()=="yes" :
           Member=add(Member)
           Member.Add()
        #To see guests which visited the house
        else :
          a=input("See guest which visited house yes/no")
          print(guest)
      else :
        print("Access Denied")

#The main feature 
class Password :
  def __init__(self,check):
    self.check=check
  def password(self) :
    i=3
    while i>0:
      if i>0 :
        #Check password
        try :
           a=input("Enter password")
           if a.strip().lower()=="exit" :
             admin=input("Do you want to enter admin mode").strip().lower()
             if admin=="yes" :
               admin=Admin(admin)
               admin.Admin()
               break
             else :
               print("Thank you")
               break
           else :
              print("welcome",passcode[a.strip()])
              break
        #Attempt counter
        except KeyError :
          print("Incorrect password you have only",i-1,"attempts")
          i=i-1
      else :
         print("error")

check=input("Are you guest yes/no")
if check.lower().strip()=="yes" :
 # In this block guest details will be taken and stored in csv file
 y=100
 while y>0 :
     name=input("What's your name")
     matches=re.match(r"[a-z]+[^0-9]$",name,flags=re.IGNORECASE)
     if matches :
            break
     else :
         print("Name can contain only characters")
         y=y-1
 z=100
 while z>0 :
     mobile=input("Enter your mobile no.")
     Matches=re.match(r"^9|8|7[^a-z][0-9]{10}+$",mobile,flags=re.IGNORECASE)
     if Matches :
            with open("guests.csv" , "a") as file :
                guest=csv.DictWriter(file, fieldnames=("name","mobile"))
                guest.writerow({"name": name , "mobile" : mobile})
                print("welcome to home",name, "but currently there is no one at home")
                break
            break     
     else :
         print("please enter valid mobile no.")
         print("mobile no. should contain only numbers")
         z=z-1
else :
   check=Password(check)
   check.password()