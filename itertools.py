from itertools import product
a = [1, 2]
b = [3]
prod = product(a, b)
print(prod)
print(list(prod))
prod2 = product(a, b, repeat=3)
print(list(prod2))

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(perm)
print(list(perm))
perm2 = permutations(a, 2)
print(list(perm2))
perm3 = permutations(a, 1)
print(list(perm3))

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(comb)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate
a = [1, 2, 3, 4, 2]
acc = accumulate(a)
print(acc)
print(list(acc))

import operator
acc2 = accumulate(a, func=operator.mul)
print(list(acc2))
acc3 = accumulate(a, func=max)
print(list(acc3))
# print([i for i in acc3])

from itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key,value in group_obj:
    print(key, list(value))

def equal_to_3(x):
    return x == 3

group_obj2 = groupby(a, key=lambda x: x==3)
for key,val in group_obj2:
    print(key, list(val))

persons = [{'name': 'Tim', 'age': 25},
        {'name': 'Dan', 'age': 25},
        {'name': 'Lisa', 'age': 27},
        {'name': 'Claire', 'age': 28}]

group_persons = groupby(persons, key=lambda pers: pers['age']==25)
for key,val in group_persons:
    print(key, list(val))

group_by_age = groupby(persons, key=lambda x: x['age'])
for key,val in group_by_age:
    print(key, list(val))

from itertools import count, cycle, repeat

for i in count(5):
    print(i)
    if(i == 15):
        break

a = [1, 2, 3]
cnt = 0
for i in cycle(a):
    print(i)
    cnt += 1
    if(cnt == 5):
        break

for i in repeat(1, 4):
    print(i)