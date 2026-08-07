# Ex:1

from abc import ABC , abstractmethod

class vehicle(ABC):

  @abstractmethod
  def start(self):
    pass

class car(vehicle):
  def start(self):
    return f"car is start   " 

class Bike(vehicle):
  def start(self):
    return f"bike is start "

class Bus(vehicle):
  def start(self):
    return f"bus is start "    

c1=car()   
print(c1.start())

# Ex:-2

from abc import ABC , abstractmethod

class payment(ABC):

  @abstractmethod
  def pay(self):
    pass

class upi(payment):

  def pay(self):
    return f"PYMENT DONE USING UPI "  

class creditcard(payment):
  def pay(self):
    return f"Payment done using Credit Card"

class cash(payment):
  def pay(self):
    return f"payment is done using cash"   

u1=upi()    
print(u1.pay())

c1=creditcard()
print(c1.pay())

c2=cash()
print(c2.pay())

# Ex:3

from abc import ABC ,abstractmethod

class Employee(ABC):

  @abstractmethod
  def calculate_salary(self):
    pass

class Programmer(Employee):

  def calculate_salary(self):
    return f"programmer salary calculated"  

class Manager(Employee):

  def calculate_salary(self):
    return f"Manager salary calculated"  

class Tester(Employee):

  def calculate_salary(self):
    return f"Tester salary calculated"    

p1=Programmer()
print(p1.calculate_salary())    

m1=Manager()
print(m1.calculate_salary())

t1=Tester()
print(t1.calculate_salary())

# EX:4

from abc  import ABC , abstractmethod

class shape_system(ABC):

  @abstractmethod

  def shape(self):
    pass

class circle(shape_system):
 
  
  def __init__(self,radius):
    self.radius=radius

  def shape(self):
    return f"circle area is {3.14*self.radius*self.radius}"


c1=circle(5)
print(c1.shape())

# Ex:-5

from abc import ABC , abstractmethod

class login(ABC):

  @abstractmethod
  def authentication(self):
    pass

class Google_login(login):

  def authentication(self):
    return f"Login successful using Google"

class Facebook_Login(login):

  def authentication(self):
    return f"Login successful using facebook"    

class EmailLogin(login):

  def authentication(self):
    return f"login successful using email"

g1=Google_login()  
f1=Facebook_Login()
e1=EmailLogin()

print(g1.authentication())
print(f1.authentication())
print(e1.authentication())
    

# Ex:6

from abc import ABC ,abstractmethod

class Storage(ABC):

  @abstractmethod
  def upload(self):
    pass

class Goggle_Drive(Storage):

  def __init__(self,rs):
    self.resume=rs

  def upload(self):
    return f"File {self.resume} upload to Google Drive"

class Aws_storage(Storage):

  def __init__(self,p):
    self.profile=p

  def upload(self):
    return f"File {self.profile} upload to AWS Storage"

class Local_storage(Storage):

  def __init__(self,pj):
    self.project=pj    

  def upload(self):
    return f"File {self.project} saved in Local Storage"

g1=Goggle_Drive("resume.pdf")
a1=Aws_storage("profile.jpg")
l1=Local_storage("project.zip")

print(g1.upload())
print(a1.upload())
print(l1.upload())