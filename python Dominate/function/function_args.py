def fruits(*items):
  print(items)

fruits("apple","banana","laptop")  


def fruits(*items):
  for item in items:
    print(item)

fruits("apple","banana","grapes")  

def total(*numbers):
  result=0

  for number in numbers:
    result=result+number

  print(result)  

total(10,20,30,40,50,)

# Create a function show_numbers() that accepts any number of numbers using *args and prints all numbers.

def show_numbers(*numbers):
 print(numbers)

show_numbers(10,50,90,80,50,50) 


# Create a function calculate_sum() that accepts any number of numbers and prints their total.

def calculate_sum(*numbers):
  total=0
  for number in numbers:
    total=total+number
  print(total)  

calculate_sum(10,80,90,50,40)


# **krgs

# Create a function show_details() that accepts any number of keyword arguments and prints the dictionary.

def show_detail(**numbers):
  print(numbers)

show_detail(
  number1=1,
  number2=2,
  number3=3
)