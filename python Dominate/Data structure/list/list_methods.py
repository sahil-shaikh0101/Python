# Add items

fruits=["apple","banana"]
fruits.append("mango")
print(fruits)

num=[10,20,30,40]
num.append(50)
print(num)

names=["rahul","amit"]
names.append("sahil")
print(names)

#insert()

fruits=["apple","banana","mango"]
fruits.insert(1,"orange")
print(fruits)

num=[10,20,30,40,50,60]
num.insert(2,25)
print(num)


names=["rahul","amit","raj"]
names.insert(0,"sahil")
print(names)

colors=["red","blue","green"]
colors.insert(1,"yellow")
print(colors)

laptop=["dell","samsung","lenovo","macbook"]
laptop.insert(0,"asus")
print(laptop)


#extend()

fruits=["apple","banana"]
more_fruits=["mango","orange"]
fruits.extend(more_fruits)
print(fruits)

a=[1,2]
a.extend([3,4])
print(a)

names=["rahil","amit"]
names.extend(["sahil","rohan"])
print(names)

colors=["red","blue"]
colors.extend(["green","yellow","black"])
print(colors)

numbers=[1,2,3]
new_num=[4,5,6,7]
numbers.extend(new_num)
print(numbers)


car=["toyato","inova","thar"]
car.append("Ertiga")
print(car)

car.insert(1,"BMW")
print(car)

car.extend(["wagnor","punch"])
print(car)

#remove items

fruits=["apple","banana","mango"]
fruits.remove("banana")
print(fruits)

bike=["unicorn","splender","shine"]
bike.remove("shine")
print(bike)

#pop()

fruits=["apple","banana","mango"]
fruits.pop(1)
print(fruits)

mobile=["samsung","nokia","iphone"]
mobile.pop(2)
print(mobile)

#clear

numbers=[10,20,30,40,50]
numbers.clear()
print(numbers)

names=["sahil","vaibhav","rohan"]
names.clear()
print(names)

names=["sahil","vaibhav","rohan"]
names.reverse()
print(names)

