myset = {1, 2, 3, 2}
print(myset)
myset2 = set([1, 2, 3])
print(myset2)
myset3 = set("Hello")
print(myset3)
print(type(myset3))
myset3 = set()
print(myset3)
myset3.add(1)
myset3.add(2)
myset3.add(3)
print(myset3)
myset3.remove(2)
print(myset3)
myset3.discard(3)
print(myset3)
myset3.clear()
print(myset3)
myset3.add(8)
print(myset3)
print(myset3.pop())
print(myset3)
for i in range(1, 5):
    myset3.add(i)
for i in myset3:
    print(i)
if 1 in myset3:
    print("Yes")
if 4 in myset3:
    print("Yes")
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i) 
i = odds.intersection(primes)
print(i)
i = evens.intersection(primes)
print(i)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# diff = setA.difference(setB)
# print(diff)
# diff2 = setB.difference(setA)
# print(diff2)
# diff3 = setB.symmetric_difference(setA)
# diff4 = setA.symmetric_difference(setB)
# print(diff3)
# print(diff4)
# setA.update(setB)
# print(setA)
# setA.intersection_update(setB)
# print(setA)
# setA.difference_update(setB)
# print(setA)
setA.symmetric_difference_update(setB)
print(setA)
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.issubset(setB))
print(setB.issubset(setA))
print(setB.issuperset(setA))
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))
# setB = setA
# setB.add(7)
# print(setB)
# print(setA)
setB = setA.copy()
setB.add(34)
print(setA)
print(setB)
a = frozenset([1, 2, 3, 4])
print(a)
print(type(a))
# a.add(2)
a.remove(1)






