my_string = "Hello World"
print(my_string)
my_string_multi = """sdds \
dsds
dsd
sd"""
print(my_string_multi)
my_string = "Hello world"
char = my_string[-2]
print(char)
substring = my_string[1:5]
print(substring)
substring = my_string[::2]
print(substring)
substring = my_string[::-1]
print(substring)
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
for i in greeting:
    print(i)
if 'ell' in greeting:
    print("Yes")
else:
    print("No")
my_string = '   Hello World     '
print(my_string)
my_string = my_string.strip()
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('He'))
print(my_string.endswith("worl"))
print(my_string.find('o'))
print(my_string.find('lo'))
print(my_string.count('o'))
print(my_string.replace('World', 'Universe'))
print(my_string)
my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)
# my_list = my_string.split("o")
# print(my_list)
new_string = ''.join(my_list)
print(new_string)
my_list = ['a'] * 5
# print(my_list)
# my_string = ''

# print(my_string)
# my_string = ' '.join(my_list)
# print(my_string)
from timeit import default_timer as timer
start = timer()
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)
var = 4
my_string = "the variable is %d" % var
print(my_string)
var = 4.5533322
my_string = "the variable is %.2f" % var
print(my_string)
my_string = "the variable is {:.2f} and {}".format(var, var)
print(my_string)
my_string = f"the variable is {var} and {var * 2}"
print(my_string)



