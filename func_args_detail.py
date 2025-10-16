# def print_name(name):
#     print(name)

# print_name('Kristijan')

# def foo(a, b, c, d=4):
#     print(a, b, c, d)

# foo(1, 2, 3)
# foo(a=1, b=2, c=3)
# foo(c=3, a=1, b=2)

# foo(1, b=2, c=3)
# foo(1, 2, 3, 6)

# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])
#     # for key in kwargs:
#     #     print(key)
    
# # foo(1, 2)
# foo(1, 2, 3, 4, 5, six=6, seven=7)
# foo(1, 2, 3, 4)

# def foo2(a, b, *, c, d):
#     print(a, b, c, d)

# foo(1, 2, c=3, d=4)

# def foo3(*args, last):
#     # print(c, d)
#     for arg in args:
#         print(arg)
#     print(last)

# foo3(1, 2, 3, last=4)

# def foo4(a, b, c):
#     print(a, b, c)

# my_list = [0, 1, 2]
# my_tuple = (0, 1, 2)
# foo4(*my_list)
# foo4(*my_tuple)
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# foo4(**my_dict)

# def foo5():
#     global number
#     x = number
#     number = 3
#     print('number inside function:', x)

# number = 0
# foo5()
# print(number)

def foo(a_list):
    # a_list = [200, 300, 400]
    # a_list.append(4)
    # a_list[0] = -100
    # a_list += [200, 300, 400]
    a_list = a_list + [200, 300, 400]

my_list=[1, 2, 3]
foo(my_list)
print(my_list)