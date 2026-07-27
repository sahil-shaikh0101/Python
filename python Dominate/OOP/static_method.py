
# EX:-1 This is not static example 
class student:
  college_id="cb101"
  def __init__(self):
   self.sid="101"

  def display(self):
    print("student id",self.sid) 
    print(student.college_id)

s1=student()    
s1.display()

# Ex:2 Static start from here

class time:
 count=0
 def __init__(self,hr,min,sec):
   self.hr=hr
   self.min=min
   self.sec=sec
   time.count+=1

 def display(self):
   print("{0} : {1} :{2}".format(self.hr,self.min,self.sec))

   #static method will not contain self
 @staticmethod
 def displaycount(): 
   print("Number of object",time.count) 

time.displaycount()
t1=time(10,20,30)
t2=time(20,50,40)
t3=time(50,40,10)
time.displaycount()


# Ex:-3
class Student:
  total_student=0

  def __init__(self,name):
    self.name=name
    Student.total_student+=1

  def display(self):  
    print("student name:-",self.name)

  @staticmethod
  def display_total_student():
    print("total student",Student.total_student)  

Student.display_total_student()

s1=Student("sahil")
s2=Student("Ashif")
s3=Student("salman")

s1.display()
s2.display()
s3.display()

Student.display_total_student()

# Ex:4
class BankAccount:
  total_account=0
  def __init__(self):
    self.account_holder=input("Enter account holder name:-")
    self.balance=input("Enter your balance:-")
    BankAccount.total_account+=1
  def display(self):
    print(" The account detail of customer is:-")
    print("account holder name and balance:-",self.account_holder,self.balance)  
   
  @staticmethod
  def display_total_account():
    print("the total account holder is:-",BankAccount.total_account)  

BankAccount.display_total_account()
b1=BankAccount()
b1.display()
b2=BankAccount()
b2.display()
b3=BankAccount()
b3.display()

BankAccount.display_total_account()


# Ex:-5

class Library:
  total_book=0

  def __init__(self):
    self.book_name=input("Enter the book name:-")
    self.author=input("Enter thebook author:-")
    Library.total_book+=1

  def display(self):
    print("The book name is",self.book_name)  
    print("The book author is :-",self.author)

  @staticmethod
  def display_total_book():
    print("total no of book:-",Library.total_book)  
  

l1=Library()
l2=Library()
l3=Library()

l1.display()
l2.display()
l3.display()

Library.display_total_book()