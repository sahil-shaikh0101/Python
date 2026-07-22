class Book:
  lib_code="101" #static 
  def __init__(self):
    self.bid=74
    self.bname="sahil"
    self.price=10
    self.author="xyz"
  def setbook(self):
    self.bid=int(input("enter the book id:-"))
    self.bname=(input("Enter a book name:-"))
    self.price=int(input("enter the book price:-"))
    self.author=input("enter the book author:-")

  def showbook(self):
    print("Bid=",self.bid)  
    print("Bname=",self.bname)
    print("price=",self.price)
    print("author=",self.author)
    print("library code:-",Book.lib_code)

  def __del__(self):
    print("object is deleted")  

b1=Book()
b1.showbook()