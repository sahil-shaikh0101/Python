def my_fuction():
  print("sahil shaikh")

my_fuction()  

def get_greeting():
  return "hello from a function"

message=get_greeting()

print(message)

#function with argument

def my_function(fname):
  print(fname + "refnes")

my_function("email ")  
my_function("Tobias ")
my_function("linus ")

def my_fuction(name):
  print("hello",name)

my_fuction("sahil")  

def my_fuction(fname,lname):
  print(fname +lname )

my_fuction("email"," refsnes")  

#default argument

def my_fuction(name="friends"):
  print("hello",name)

my_fuction("email")
my_fuction("tobias")
my_fuction()
my_fuction("linus")

def greet(name="sahil"):
  print(name)

greet("amit")  
greet()
greet()
greet("imran")

def countries(country="japan"):
  print(country)

countries("India")
countries()

# keyword argument

def my_function(animal,name):
  print("i have a",animal)
  print("my",animal + "s name is",name)

my_function("Dog","sheru")  
my_function(animal="lion",name="Don")


#sending list as an argument
def my_function(fruits):
  for fruit in fruits:
    print(fruits)

my_fruits=["apple","banana","cherry"]

my_function(my_fruits)

#return value

def my_function(x,y):
  return x+y

result=my_function(5,3)
print(result)
