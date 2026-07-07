'''V3 Features:-
Can store huge family members
Store guest details
check password
counter attempt
'''
# This block stores passwords
password={"1234":"santosh",
          "4567":"sunil",
          "7000":"prathmesh",
          "9000":"shreya",
          "5000":"pranjal"}
guest={}
# This block handle guest and stores guest data
b=input("Are you guest yes/no")
if b.lower().strip()=="yes" :
     name=input("What's your name")
     mobile=input("Enter your mobile no.")
     guest[name]=mobile
     print("welcome to home",name, "but currently there is no one at home")
     print(guest)
# This block check passwords
else :
     i=3
     while i>0:
          try:
               a=input("Enter password")
               print("welcome",password[a.strip()]) 
               break
# This block count attempts
          except KeyError:
               print("Incorrect password you have only",i-1,"attempts")
               i=i-1