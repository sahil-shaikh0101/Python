thislist=("apple","banana","cherry")
print(len(thislist))

thislist=("apple")
print(type(thislist))

tuple1=("apple","banana","cherry")
print(tuple1)


# indexing

thislist=("apple","banana","cherry")

print(thislist[0])
print(thislist[-1])

#slicing

fruits=("apple","banana","cherry","papaya","grapes")

print(fruits[1:])
print(fruits[::-1])
print(fruits[::-1])


# Convert the tuple into a list to be able to change it:

x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

car=("ertiga","inova","thar")
vehicle=list(car)
vehicle[0]="Scorpio"
car=tuple(vehicle)
print(car)

thislist=("apple","banana","cherry")
y=list(thislist)
y.append("orange")
thislist=tuple(y)
print(thislist)

#unpaking

fruits=("apple","banana","cherry")

(green,yellow,red)=fruits

print(green)
print(yellow)
print(red)


animal=("dog","cat","lion")

(a,b,c)=animal
print(a)
print(b)
print(c)


#loop

thislist=("apple","banana","cherry")

for x in thislist:
  print(x)

#tuple methods

thislist=(1,3,7,8,9,5,2,5,2,6,5,6,8,7)
print(thislist.count(5))
print(thislist.index(3))

#nested tuple

a=(("lion","elephant"),("dog","cat","tiger"))

print(a[0][0])
print(a[1][2])