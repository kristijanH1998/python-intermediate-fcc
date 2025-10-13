mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist2[0]
print(item)
item2 = mylist2[-2]
print(item2)

for i in mylist2:
    print(i)

if "banana" in mylist2:
    print("yes")
else:
    print("no")

print(len(mylist2))
mylist2.append("lemon")
print(mylist2)
mylist2.insert(1, "blueberry")
print(mylist2)
item3 = mylist2.pop()
print(mylist2)
print(item3)
item4 = mylist2.remove("apple")
print(mylist2)
mylist2.clear()
print(mylist2)
mylist2 = [1,5,2,3,4,4]
mylist2.reverse()
print(mylist2)
mylist2.sort()
print(mylist2)
new_list = sorted(mylist2)
print(new_list)
new_list = [0] * 5
print(new_list)
new_list2 = [1, 2, 3, 4, 5]
new_list = new_list2 + new_list2
print(new_list)
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = new_list[::-2]
print(a)
list_org = ["banana", "cherry", "apple"]
# list_cpy = list_org
list_cpy = list_org.copy()
list_cpy.append("lemon")
print(list_cpy)
print(list_org)
list_cpy2 = list(list_org)
print(list_cpy2)
list_cpy3 = list_org[:]
print(list_cpy3)
a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]
print(b)



