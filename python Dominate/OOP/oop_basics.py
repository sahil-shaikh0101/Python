# Ex:1

class book:
  def __init__(self):
    self.bid=int(input("Enter your book id:-"))
    self.bname=input("Enter book name:-")
    self.price=int(input("enter your price:-"))
    self.author=input("enter your author name:-")

  def showbook(self):
    print("Bid:-",self.bid)  
    print("banme:-",self.bname)
    print("price:-",self.price)
    print("author",self.author)

b1=book()
# b1.setbook()
b1.showbook()    

# Ex:-2

class student:
  def __init__(self):
    self.name="sahil"
    self.id=125
    self.collage="JSPM"

  def display(self):
    print("Student name:-",self.name)  
    print("student id:-",self.id)
    print("collage",self.collage)

s1=student()    
s1.display()


# Ex3

class product:
  def __init__(self):
    self.name=input("enter product name:-")
    self.company=input("enter company name:-")
    self.price=int(input("enter product price:-"))

  def display_details(self):
   print("The name of product:-",self.name)
   print("company of the product:-",self.company)
   print("the price of the productP",self.price)

p1=product()   
p1.display_details()


# Ex:-4

class Electricity:

 def __init__(self):
  self.name=input("Enter your electricity company name:-")
  self.price=input("Enter price per unit:-")
  self.area=input("Enter your area:-")

 def display(self):
  print("the electricity company name is",self.name) 
  print("the price of electricity is",self.price)
  print("the area of electricity is",self.area)


e1=Electricity()  
e1.display()

# Ex:-5

class vehicle:
 vehicle_code=12345 #static variable
 def __init__(self,name,price):
    self.name=name
    self.price=price

 def dislay(self):
    print("The name of vehucle:-",self.name)  
    print("the price of the vehicle",self.price)
    print("the code of the vehicle:-",vehicle.vehicle_code)

v1=vehicle("Honda ",50000)
v1.dislay()
