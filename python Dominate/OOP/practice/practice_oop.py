# Ex:1
class book:
  def __init__(self):
    self.book_name="python learning"
    self.author="Sahil shaikh"
    self.price=500
  def display(self):
    print("book name:-",self.book_name)  
    print("book author:-",self.author)
    print("book price:-",self.price)

b1=book()
b1.display()

# Ex:2

class Employee:
  def __init__(self):
    self.name="sahil"
    self.salary="12 LPA"
    self.department="Brilient Software Engineer"
  def display(self)  :
    print("Name of employe:-",self.name)
    print("Salary of employee:-",self.salary)
    print("Department of employee:-",self.department)

e1=Employee()    
e1.display()

# Ex:3

class Product:
  def __init__(self,name,price,quality):
    self.name=name
    self.price=price
    self.quality=quality
  def display(self):
    print("name of product:-",self.name)  
    print("price of product:-",self.price)
    print("quality of product:-",self.quality)

p1=Product("Laptop",42000,2)
p1.display()

# EX:-4

class cricketer:
  def __init__(self,player,age,runs,Team):
    self.player=player
    self.age=age
    self.runs=runs
    self.Team=Team
  def Display(self):
    print("Name of player:-",self.player)  
    print("Age of player:-",self.age)
    print("Runs of player:-",self.runs)
    print("Team of player:-",self.Team)

c1=cricketer("Hardik Pandya",32,10000,"India")    
c1.Display()
    
#Ex:-5

class Mobile:
  def __init__(self):
    self.mobile=(input("enter your mobile:-"))
    self.price=int(input("enter your price:-"))
    self.storage=input("enter your storage:-")
    self.color=input("enter your color:-")
  def display(self):
    print("name of the mobile",self.mobile)  
    print("Enter price of the mobile:-",self.price)
    print("Enter storage of mobile:-",self.storage)
    print("enter color of the mobile:-",self.color)

m1=Mobile()    
m1.display()
