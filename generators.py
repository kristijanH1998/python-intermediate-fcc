#left off: 3:35

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3
#     yield 1

# g = mygenerator()
# print(g)
# for i in g:
#     print(i)

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

# g = mygenerator()
# # print(sum(g))
# print(sorted(g))
# print(g)

# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)
# value = next(cd)
# print(value)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# mylist = firstn(10)
# print(mylist)
# print(sum(mylist))
# print(sum(firstn_generator(10)))

import sys

# print(sys.getsizeof(firstn(1000)))
# print(sys.getsizeof(firstn_generator(1000)))

# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# fib = fibonacci(30)
# for i in fib:
#     print(i)

mygenerator2 = (i for i in range(100) if i % 2 == 0)
# for i in mygenerator2:
#     print(i)

mylist2 = [i for i in range(100) if i % 2 == 0]
print(mylist2)

print(list(mygenerator2))

mygenerator3 = (i for i in range(5))
print(list(mygenerator3))

print(sys.getsizeof(mygenerator2))
print(sys.getsizeof(mylist2))