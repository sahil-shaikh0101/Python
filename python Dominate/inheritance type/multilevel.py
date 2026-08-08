# Ex:1

class Base:
  def fbase(Self):
    print("i am  fbase from base")

class Drived(Base):
  def fDerived(Self):
    print("I am fDrived from Derived")    

class Subderived(Drived): 
  def fsubderived(Self):
    print("I am fsubderived from subderived")   

b1=Subderived()    
b1.fbase()
b1.fDerived()
b1.fsubderived()

# Ex:2

class vehicle:
  def display(self):
    print("I am vehicle")

class car(vehicle):
  def display(self):
    super().display()
    print(" i am car")    

class Electricalcar(car) :
  def display(self):
   super().display()
   print("I am electrical car" )

b1=Electricalcar()
b1.display() 

# Ex:-3

class Employee:
    def display(self):
        print("I am corporate majdoor")


class Manager(Employee):
    def display(self):
        super().display()
        print("I am Manager")


class SeniorManager(Manager):
    def display(self):
        super().display()
        print("I am senior manager")


s1 = SeniorManager()
s1.display()

# Ex:-4

class school:
    def displayschool(self): 
       print("Samta prathmik vidya mandir")

class teacher(school):
    def displayteacher(self):
        
        print("there are lots of teacher in the school")       

class mathteacher(teacher):
    def displaymath(self):   
     print("i am sahil i teach math here")

m1=mathteacher()    
m1.displayschool()
m1.displayteacher()
m1.displaymath()
