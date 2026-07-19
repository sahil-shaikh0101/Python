thislist={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}
print(thislist)

print(thislist["brand"])
print(thislist["model"])
print(thislist["year"])

# Access item

thisdict={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}
print(thisdict["model"])
print(thisdict["year"])

# get()

print(thisdict.get("year"))

thislist={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

#keys

print(thisdict.keys())
print(thislist.keys())
print(thislist.keys())


car={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

print(car)

print(car["model"])
print(car["year"])

# get()

print(car.get("brand"))

# keys()
print(car.keys())

car={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

# value()

print(car.values())

#change

thislist={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

thislist["brand"]="Mahindra"
print(thislist)

# thislist["year"]=2018

# print(thislist)

# thislist["model"]="honda"
# print(thislist)

#update()

thisdict={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

# thisdict.update({"sahil":"name"})
# print(thisdict)

thisdict.update({"year":2026})
thisdict.update({"name":"sahil"})
print(thisdict)

# Removing Items

thislist={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

thislist.pop("model")
print(thislist)

# clear()

thislist.clear()
print(thislist)

#loop

car={
  "honda":"unicorn",
  "hero":"spelnder",
  "bajaj":"pelsar"
}

# for x in car:
#   print(car[x])

# value()

for x in car.values():
  print(x)

  #copy()

thisdict={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}  

mydict=thisdict.copy()
print(thisdict)
print(mydict)

