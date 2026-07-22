class student:
  pass

s1=student()
s2=student()

class student:
  def __init__(self):
    print("constructor called")

s1=student()    
s2=student()


class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

s1=student("sahil",22)    
print(s1.name)
print(s1.age)

class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    print("student object is created")

  def display(self):
    print("name:-",self.name)  
    print("age:-",self.age)

  def __del__(self):
    print("student object is deleted")  

s1=student("sahil",22)    

s1.display()
del s1

class student:

  def __init__(self,name):
    self.name=name
    print("constructor called")

  def display(self):
    print(self.name)  

  def __del__(self)  :
    print("destructor called")

s1=student("sahil")   #1. object created
                #2.__init__ automatically call
s1.display()   #3.method manualy call                
del s1         #4.s1 reference delet\
                #5.Object destroy