# Ex:1

class vehicle:
  def __init__(self,id,nm,ml):
    self.vid=id
    self.vname=nm
    self.mileage=ml

  def displayv(self):
    print("The id of vehicle:-",self.vid)  
    print("the name of vehicle:-",self.vname)
    print("The mileage of the vehicle:-",self.mileage)

    
class car(vehicle):
  def __init__(self,id,nm,ml,bk,ft):
    super().__init__(id ,nm,ml)
    self.breaks=bk
    self.fuelt=ft

  def display(self):
    print("the breaks types:-",self.breaks)  
    print("The fuel types is:-",self.breaks)


c1=car(101,"BMW","5km","Drum break","petrol")
c1.displayv()
c1.display()

# EX:-2

class animal:
  def __init__(self,nm,ag):
    self.name=nm
    self.age=ag

  def displaya(self):
    print("The name of Animal:-",self.name)  
    print("The age of Animal:-",self.age)

class dog(animal):
  def __init__(self,nm,ag,bd,cl):
    super().__init__(nm,ag)
    self.breed=bd
    self.color=cl

  def display(self):
    print("the breed of dog:-",self.breed)  
    print("the color of the dog:-",self.color)

a1=dog("Sheru",5,"German shefhard","black")
a1.displaya()    
a1.display()

# Ex:-3

class Bank_account:
  def __init__(self,an,hn,bl):
    self.account_number=an
    self.holder_name=hn
    self.balance=bl

  def displays(self):
    print("the account number :-",self.account_number)  
    print("the account holder name:-",self.holder_name)
    print("the bank balance:-",self.balance)

class savingAccount(Bank_account):
  def __init__(self,an,hn,bl,ir,at):
    super().__init__(an,hn,bl)
    self.interest_rate=ir
    self.account_type=at

  def displayA(self):
    print("the interest rate is:-",self.interest_rate)  
    print("the account type:-",self.account_type)

b1=savingAccount(10042004,"Engineer Sahil","10cr","5%","saving account")    

b1.displays()
b1.displayA()

# Ex:-4

class product:
  def __init__(self,pi,nm,pr):
    self.product_id=pi
    self.name=nm
    self.price=pr

  def displayP(self):
    print("Tne id of product:-",self.product_id)  
    print("The name of product:-",self.name)
    print("the price of the product:-",self.price)

class mobile(product):
  def __init__(self,pi,nm,pr,rm,sg):
    super().__init__(pi,nm,pr)
    self.ram=rm
    self.storage=sg

  def displaym(self):
    print("the ram of mobile:-",self.ram)
    print("The storage of the mobile:-",self.storage)

p1=mobile(101,"apple",100000,"12gb","512gm")    
p1.displayP()
p1.displaym()