day=int(input("enter your day:-"))

match day:
  case 1:
    print("monday")
  case 2 :
    print("tuesday")  
  case 3:
    print("wednesday")  
  case 4:
    print("thursday")
  case 5 :
    print("Friday")  
  case 6:
    print("saturday")  
  case 7:
    print("sunday")  
  case _:
    print("Inwalid number")  

# # combile Value

day=int(input("enter your value:-"))

match day:
  case 1 | 2| 3 | 4 | 5 | 6 :
    print("today is weekday")
  case 7:
    print("today is holiday")  
  case _:
    print("inwalid number")  


#practice:-

# EX:-1: Write a program to take a number from the user and print its name using match-case .

num=int(input("enter your number:-"))

match num:
  case 1 :
    print("one")
  case 2:
    print("two")  
  case 3:
    print("three")
  case 4:
    print("four")  
  case 5:
    print("five")  
  case _:
    print("you only take one to five ")  
 
# EX:-2
# Write a calculator program using match-case that takes two numbers and an operator (+, -, *, /) from the user.

num1=int(input("enter your number:-"))
num2=int(input("enter your number:-"))
operator=input("enter your operator:-")

match operator:
  case "+":
    print(num1+num2)
  case "-":
    print(num1-num2)  
  case "*":
    print(num1*num2)  
  case "/":
    print(num1/num2)  
  case _:
    print("inwali operator")  

# Ex:-3 Write a program to take a traffic light color as input and print the action using match-case (Red → Stop, Yellow → Wait, Green → Go).

trafic_light_color=input("enter your color:-")

match trafic_light_color :
  case "red" :
    print("stop")
  case "yellow":
    print("Wait")
  case "green":
    print("Go")  
  case _:
    print("you don't know traffic color")  

# Ex:4
# Write a program to create a food menu system using match-case and display the price of the selected item
# 

print("\t\t\tFood menu system")    
print("\t\t\tAvailable food:-")
print("\t\t\t1.Biryani")
print("\t\t\t2.Dalcha Rice")
print("\t\t\t3.Korma Rice")
print("\t\t\t4.veg paneer")


food=input("enter your food Item:- ")

match food:
  case "Biryani":
    print("price:-180rs full 90 half")
  case "Dalcha Rice":
    print("price:-150rs")  
  case "Korma Rice":
    print("price:- 200rs") 
  case "veg paneer":
    print("price:-210")   
  case _:
    print("Go to next hotel and don't come again here")  

# Ex:5 Write a program to take a payment method (cash, card, UPI) and print .

payment_method=input("Enter your payment method:-")

match payment_method :
  case "cash":
    print("thank you for cash but you should learn how to used upi and card also ")
  case "card":
    print("its credit or debit")  
  case "upi":
    print("Phone pay or Google pay") 
  case _:
    print("here only three payment method available so go in different shop")  

