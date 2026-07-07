'''V1 Features:-
Ask hello to user
works on one single password
Handle guest
attempt counter
'''
name=input("what's your name")
print("hello,",name) 
i=3
# In this block password is checked
while i>0:
     a=input("Enter password")
     if a.strip()=="123":
       print("welcome")
       break
# This block handles guest 
     else :
         a=input("Are you guest yes/no")
         if a.strip().lower()=="yes" :
             print("welcome home but currently no one is there at home")
             break
# This block count attempts
         else :
             print("incorrect password you have only",i-1,"attempt")
             i=i-1