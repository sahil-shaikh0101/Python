
#EX:1 merrage eligibility criteria in INDIA

print("Legal age og merrage in india")

gender=input("Enter male (m) or female (f):-")
age=int(input("enter your age:-"))

if gender=="m":
  if age>=21:
    print("you are eligible for merrage")
  else:
    print("your are not eligible for merrage its a child merrage")  
elif gender=="f":
  if age>=18:
    print("you are eligible for merrage")
  else:
    print("you are not eligible for merrage its child merrage")  
else:
  print("inwalid word for gender use f and m ")    
    
# EX:2 A user can log in only if the username is correct. If the username is correct, then check whether the password is correct.

username=input("enter your useranme:-")
password=input("Enter your password:-")

if username=="sahil":
  if password=="sahil@123":
    print("login succesful")
  else:
    print("Inwalid password")  
else:
  print("Inwalid username")    

#Ex:3 A bank allows a customer to withdraw money only if the account is active. If the account is active, then check whether the balance is enough for the withdrawal. 

account=(input("enter your account detail (\"yes no\"):-"))
balance=int(input("Enter your balance:-"))

if account=="yes":
  if balance>=1000:
    print("your balance enough for withdrawal")
  else:
    print("balance is not enough for withdrawal")  
else:
  print("acount is inactive")   


#Ex:-4 A person can apply for a driving license only if they are 18 years or older. If eligible, then check whether they have passed the driving test. 

age=int(input("enter your age :-"))
driving_test=input("Enter they drive (yes/no:- )")

if age>=18:
  if driving_test=="yes":
    print("license approved")
  else:
    print("liecense not approved")  
else:
  print("you are not eligible")    


# Ex:5  A customer gets a discount only if they are a premium member. If they are a premium member, then check whether their purchase amount is ₹5000 or more.

premium=input("Enter your membership detail (yes/no:-)")
amount=int(input("enter your acount of shopping :-"))

if premium=="yes":
  if amount>=5000:
    print("you get discount")
  else:
    print("you don't get discount")  
else:
  print("your are not premium member ")    