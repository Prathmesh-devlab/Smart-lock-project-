"""V4 Features:-
New member registeration
Admin security
Store huge family members
Store guest details 
Check password
Attempt counter
"""
password={"1234":"santosh",
          "4567":"sunil",
          "7000":"prathmesh",
          "9000":"shreya",
          "5000":"pranjal"}
# All visited guest names will be stored in this dictionary :- guest{}
guest={}
# To add new member
if __name__=="__main__" :
 d=input("Add member yes/no")
 if d.strip().lower()=="yes" :
     e=input("Enter admin password")
     if e.strip().lower()=="santosh@123" :
          print("access granted")
          nam=input("Enter your name")
          passcode=input("Set new pasword").strip()
          password[passcode]=nam
          print("sucessfully added")
          print(password)
     else : 
          print("access denied")
 b=input("Are you guest yes/no")
 if b.lower().strip()=="yes" :
 # In this block guest details will be taken and stored
     name=input("What's your name")
     mobile=input("Enter your mobile no.")
     guest[name]=mobile
     print("welcome to home",name, "but currently there is no one at home")
     print(name,"has visited the house")
 else :
     i=3
     while i>0:
          try :
               a=input("Enter password")
               print("welcome",password[a.strip()])
               break
          except KeyError:
               print("Incorrect password you have only",i-1,"attempts")
               i=i-1