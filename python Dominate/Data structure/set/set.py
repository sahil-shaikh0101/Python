thisset={"apple","banana","cherry"}
print(thisset)

#add item

thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

#update

thisset={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}

thisset.update(tropical)
print(thisset)

animal={"dog","cat","rat"}
a={"lion"}
animal.update(a)
print(animal)

thisset={"apple","banana","cherry"}
mylist=["kiwi","orange"]
thisset.update(mylist)
print(thisset)

#remove

fruits={"apple","banana","cherry"}
fruits.remove("apple")
print(fruits)

#its not give error when item is not exist

fruits.discard("papaya")
print(fruits)

#clear

fruits.clear()
print(fruits)

# Loop

thisset={"apple","banana","cherry"}

for x in thisset:
  print(thisset)


#union method

set1={"a","b","c","d"}
set2={10,20,30}

set3=set1.union(set2)
print(set3)

brands={"Samsung","lenovo","apple"}
brands2={"redmi","realme"}
company=brands.union(brands2)
print(company)

animal={"dog","cat","lion"}
animal2={"rat","tiger"}
result=animal | animal2
print(result)

laptop={"dell","lenovo","samsung"}
brands={"redmi","apple"}
companies= laptop | brands
print(companies)

#update

set1={"a","b","c","d"}
set2={1,2,3}
set1.update(set2)
print(set1)

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}

set3=set1.intersection(set2)
print(set3)

#difference

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}

print(set1.difference(set2))

# Symmetric Differences

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.symmetric_difference(set2)
print(set3)