import json
print("choose login or sign up")
print("1_signup")
print("2_login")
user=int(input("enter your choice:-"))
if user==1:
    username=input("enter your name:-")
    password=input("enter your password:-")
    password_c=input("confirm the password:-")
    a=0
    b=0
    c=0
    d=0
    capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small="abcdefghijklmnopqrstuvwxyz"
    special="@$#&?!"
    digits="0123456789"
    if len(password)>=6:
        for i in password:
            if i in capital:
                a=a+1
            if i in small:
                b=b+1
            if i in special:
                c=c+1
            if i in digits:
                d=d+1
    if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(password)):
        print("strong password")
    else:
        print("weak password")
   