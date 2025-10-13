mytuple = ("Max", 28, "Boston")
print(mytuple)
print(type(mytuple))
mytuple2 = tuple(["Max", 28, "Boston"])
print(mytuple2)
item = mytuple[0]
print(item)
item2 = mytuple[-1]
print(item2)
# mytuple[0] = "Tim"
for i in mytuple:
    print(i)
if "Max" in mytuple:
    print("yes")
else:
    print("no")
my_tuple = ('a', 'b', 'c', 'd', 'e')
print(len(my_tuple))
print(my_tuple.count('b'))
print(my_tuple.index('b'))
my_list = list(my_tuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
print(type(b))
c = b[::1]
print(c)
print(a[::-1])
my_tuple3 = "Max", 28, "Boston"
name, age, city = my_tuple3
print(name)
print(age)
print(city)
my_tuple4 = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple4
print(i1)
print(i3)
print(i2)
print(type(i2))

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
import timeit
print(timeit.timeit(stmt="[0, 1, 2]", number = 100000))
print(timeit.timeit(stmt="(0, 1, 2)", number = 100000))




