import calculater
print(calculater.add(10,10))
print(calculater.substrct(800,50))
print(calculater.multiply(10,10))

import math

print(math.sqrt(64))
print(math.pi)
print(math.ceil(4.2))
print(math.floor(4.8))

import random
print(random.randint(1000,10000))

import datetime
print(datetime.datetime.now())

from collections import Counter

number =[1,1,2,2,2,3]
print(Counter(number))

from pathlib import Path

file= Path("text.txt")
print(file.exists)

import os
print(os.getcwd())

import sys
print(sys.version)