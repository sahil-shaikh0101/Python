def display():
  print("hello ")

display()

def display(n):
  for i in range(n):
    print("hello")
    print("Welcome")

display(5)
  
def sum():
  x=int(input("Enter your number:-"))  
  y=int(input("enter your number:-"))
  return x +y


result=sum()
print(result)


def sum(x,y):
  return x+ y

x=int(input("enter your number:-"))
y=int(input("enter your number:-"))

result=sum(x,y)
print(result)

# Write a function greet() that prints "Hello, Python!".

def greet():
  print("hello, python")

greet()  

# Write a function greet_user(name) that takes a name and prints a greeting message.

def greet_user(name):
  print(name,"i am good")

greet_user("sahil")  

# Write a function square(n) that returns the square of a number

def square(n):
  return n*n

n=int(input("enter your number:-"))
result=square(n)
print(result)

# Write a function is_even(n) that returns True if the number is even, otherwise False.

def is_even(n):
 
 if n%2==0:
  return True
 else:
  return False
 
n=int(input("enter your number:-")) 
result=is_even(n)
print(result)

# Write a function find_largest(a, b) that returns the larger number.

def find_largest(a,b):
  if a>b:
    return a
  else:
    return b

a=int(input("enter your number:-"))  
b=int(input("enter your number:-"))

result=find_largest(a,b)
print(result)

# Write a function calculate_area(length, width) that returns the area of a rectangle.

def calculate_area(length,width):
  area=length*width
  return area

length=int(input("enter your length:-"))  
width=int(input("enter your width:-"))

result=calculate_area(length,width)
print(result)

# Write a function calculate_age(birth_year, current_year) that returns a person's age

def calculate_age(birth_year,current_year):
  age=current_year - birth_year
  return age

birth_year=int(input("enter your birth year:-"))  
current_year=int(input("enter your current year:-"))

result=calculate_age(birth_year,current_year)
print(result)

# # Write a function calculate_total(price, quantity) that returns the total shopping bill.

def calculate_total(price,quantity):
 total=price*quantity
 return total

price=int(input("enter product price:-"))
quantity=int(input("enter product quatity:-"))

result=calculate_total(price,quantity)
print(result)

#Write a function calculate_discount(price, discount_percent) that returns the final price after discount.

def calculate_discount(price,discount_percentage):
  discount=price*discount_percentage//100
  final_price=price-discount
  return final_price

price=int(input("enter your price:-"))
discount_percentage=int(input("enter your dicount:-"))

result=calculate_discount(price,discount_percentage)
print("final price is",result)