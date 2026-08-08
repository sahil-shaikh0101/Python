class employee:
  def detail(self):
    print("i am employee")

class programmer(employee):
  def dprogrammer(self):
    print("i am programmer")    

class manager(employee):
  def dmanager(self):
    print("i am manager")

class teamlead(programmer,manager):
  def dteamlead(self):
    print("i am tech lead engineer")    

t1=teamlead()
t1.dprogrammer()
t1.dmanager()
t1.dteamlead()