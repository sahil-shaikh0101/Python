#EX:1  A gym allows only people who are 18 years old or older to buy a membership. Write a program to check whether a person can get a membership.

age=int(input("Enter your age:-"))

if age>=18:
  print("buy a membership")
else:
  print("you don't required membership ")  

#Ex:2 A bank allows customers to withdraw money only if they have enough balance in their account. Write a program to check whether the withdrawal is possible

amount=int(input("Enter your amount:-"))

if amount>=1000:
  print("Widrawl is possible")
else:
  print("widrawl is not possible")  

#Ex:-3 An e-commerce website gives discounts based on the customer's total purchase amount.
# Write a program to display the discount the customer will receive.

amount=int(input("enter your amount:-"))

if amount>=500:
  dis=5
elif amount>=1000:
  dis=10
else:
  print("you don't have discount")  

discount=amount*dis/100
total=amount-discount

print(f"your total amount is {total}")
print(f"your discount is {discount}")


#EX:4 A company gives yearly bonuses to employees based on their years of experience.
# Write a program to display the employee's bonus category.

experience=int(input("Enter your year of experience:-"))

if experience>10:
  print("you get bonus 20%, of your salary")
elif experience>5:
  print("you get Bonus 10%, of your salary")  
elif experience>2:
  print("you get bonus 2%, of your salary")  
else:
  print("you don't get bonus GO and Work")  

#Ex:5 An electricity company charges different rates based on the number of units consumed.
# Write a program to calculate the bill using the correct rate.

unit=int(input("enter your electricity units:-"))

if unit>=20:
  charge=10
elif unit>=15:
  charge=5  
elif unit>=5:
  charge=2
else:
  print("you dont have charge")    

total=unit*charge

print(f"your total bill isv  {total}")

#Ex:6 A mobile recharge app has multiple recharge plans.
# Write a program to display the selected plan and its price.


plan=int(input("enter your plan budget:-"))

if plan>=2000:
  print("you get 5g unlimited a year and unlimited call and sms")
elif plan>=1000:
  print("you get 5g unlimited for 6 months and unlimited calls and sms")  
else:
  print("you get for 1 month 5g unlimited and free calls and sms")  
