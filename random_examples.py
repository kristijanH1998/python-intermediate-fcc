# left off: 2:59
import random

a = random.random()
print(a)
b = random.uniform(1,10)
print(b)
c = random.randint(1, 10)
print(c)
d = random.randrange(1, 10)
print(d)
e = random.normalvariate(0, 1)
print(e)

mylist = list("ABCDEFGH")
print(mylist)
a = random.choice(mylist)
print(a)
b = random.sample(mylist, 3)
print(b)
c = random.choices(mylist, k=3)
print(c)
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))

import secrets

a = secrets.randbelow(10)
print(a)
b = secrets.randbits(10)
print(b)
mylist = list("ABCDEFGH")
c = secrets.choice(mylist)
print(c)

import numpy as np

a = np.random.rand(3)
print(a)
a = np.random.rand(3, 3)
print(a)
b = np.random.randint(0, 10, 3)
print(b)
c = np.random.randint(0, 10, (3,4))
print(c)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)
# for tri in arr:
#     np.random.shuffle(tri)
# print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))

