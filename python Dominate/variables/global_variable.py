# teach by w3school

x="aweosme"

def myfunc():
  x="fantastic"
  print("python is ",x)

myfunc()

print("python is",x)

x="sahil"
def myfunc():
  global x
  x="fantastic"
 
myfunc()  

print("python is ",x)


# EX:-1

x="sahil"
def shaikh():
  global x
  x="software"
  print("sahil is",x)

shaikh()  

print(x)

# Ex:-2

y="dell"
def sahil():
  global y
  y="samsung"
  print("my laptop is",y)

sahil()  
print("my laptop is ",y)

# Ex:-3

h="virat"
def cricket():
  global h
  h="hardik pandya"
  print("my favourite cricket player is ",h)

cricket()
print(h) 

# EX4:-

a="sharukh"

def actor():
  global a
  a="salman khan"
  print("my favourite actor is ",a)

actor()
print(a)  

# EX:-5

b="atomic habbit"

def book():
  global b
  b="the power of subconsious Mind"
  print("my favourite book is ",b)


book()
print(b)  