# Ex:-1

class Employee:

  def login (Self):
    print("Employee login")

class programmer(Employee):

  def write_code(self):
    print("programmer writes code")    

class system_manager(Employee):
  def manage_team(self):
    print("its manage team")

class Admin(Employee):
  def manage_system(self):
    print("Admin manage team") 
     

p=programmer()    
p.login()
p.write_code()

s=system_manager()
s.login()
s.manage_team()

a=Admin()
a.login()
a.manage_system()

# Ex:-2

class voter:
  def show_voter(self):
    print("voter is eligible to vote")

class student(voter):
  def student_vote(self):
    print("student is votting")  

class Adult(voter):
  def adult_vote(self):
    print("Adult is voting")  

class senior(voter):
  def senior_voting(self):
    print("seior is eligible for voting")        

s=student()
s.show_voter()   
s.student_vote()

v=voter()
v.show_voter()

a=Adult()
a.adult_vote()
a.show_voter()