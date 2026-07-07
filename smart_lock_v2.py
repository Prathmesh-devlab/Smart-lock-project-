'''V2 Features:-
Store different passwords for each member
Check password
Attempt counter
'''
# This block handles guest
b=input("Are you guest yes/no")
if b.lower().strip()=="yes" :
     print("welcome home but currently there is no one at home")
# This block check passwords for multiple users
else :
     i=3
     while i>0:
         a=input("Enter password")
         if a.strip().lower()=="1234" :
             print("welcome santosh")
             break
         elif a.strip().lower()=="7000":
             print("welcome prathmesh")
             break
         elif a.strip().lower()=="2008":
             print("welcome shreya")
             break
         elif a.strip().lower()=="8308":
             print("welcome pranjal")
             break
# This block count attempts
         else :
             print("incorrect password you have only",i-1,"attempt")
             i=i-1