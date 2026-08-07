# Ex:1

class Emp:
  def __init__(self,id,nm,bs):
    self.eid=id
    self.ename=nm
    self.basic=bs

  def __str__(self):
    data ="Eid ="+str(self.eid)
    data +="\nName="+self.ename
    data += "\nBasic ="+str(self.basic)
    return data
    

class programmer(Emp):
  def __init__(self, id, nm, bs,ec,cp):
    super().__init__(id, nm, bs)
    self.extra_charge=ec
    self.cost_per_hours=cp

  def __str__(self):
    data=super().__str__()  
    data +="\n Extra hours="+str(self.extra_charge)
    data +="\n cost per hrs="+str(self.cost_per_hours)
    return data

e1=programmer(1010,"pratik",25000,12, 25)
print(e1)
print(e1.__dict__)
  
# Ex:2

class vehicle:
  def __init__(self,b,m,p):
    self.brand=b
    self.model=m
    self.price=p

  def __str__(self):
    data="brand="+self.brand
    data+="\nmodel="+self.model
    data+="\nprice="+str(self.price)
    return data

class car(vehicle):
  def __init__(self,b,m,p,f,ml):
   super().__init__(b,m,p) 
   self.fuel=f
   self.mileage=ml

  def __str__(self):
    data=super().__str__()
    data+="\nfuel_type:-"+self.fuel
    data+="\nmileage:-" +self.mileage
    return data

c1=car("honda","unicorn",125000,"petrol","50km")  
print(c1)

# Ex:3

class student:
  def __init__(self,nm,age):
    self.name=nm
    self.age=age

  def __str__(Self):
    return f"name of student is {Self.name} and age of student {Self.age}"     

class sahil(student):
  def __init__(self, nm, age,id ,add):
    super().__init__(nm, age)
    self.id=id
    self.address=add

  def __str__(self):
    data = super().__str__()
    return data +  f"\nthe id of student is {self.id} \n and adress of student {self.address}"  

s12=sahil("sahil",22,2525,"Pune")    
print(s12)

