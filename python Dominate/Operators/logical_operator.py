# # Ex:1 Check whether a person is eligible for voting using age and citizenship conditions.

age=int(input("enter your age:-"))
citizenship=input("enter your citizenship:-")

if age>=18 and citizenship=="india":
  print("you are eligible")
else:
  print("you are not eligible")  

# Ex2:-Check whether a student gets a scholarship based on marks and attendance.

marks=int(input("enter your marks:-"))
attendance=int(input("enter your attendance:-"))

if marks>=75 or attendance>=70:
  print("student are eligible")
else:
  print("student are not eligible")

# Ex:-3 Check whether a user is not logged in.

login=False

if not login:
  print("user is not login")
else:
  print("user is login")  

# ex4 Check whether a student is not failed.

failed=False

if not failed:
  print("student is not failed")
else:
  print("student is failed")  

  
# Ex5:-Check whether a user can login using username and password conditions.

username=input("enter your username:-")
password=input("enter your password:-")

if username=="sahil" and password == "shaikh":
  print("Login successful")
else:
  print("Login failed")  