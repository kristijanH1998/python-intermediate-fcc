# # * * * * *
# result = 5 * 7
# print(result)
# result = 2 ** 4
# print(result)
# zeros = [0] * 10
# print(zeros)
# zeros_ones = [0, 1] * 10
# zeros_ones_tup = (0, 1) * 10
# strings = "AB" * 10
# print(zeros_ones)
# print(zeros_ones_tup)
# print(strings)

# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])

# foo(1, 2, 3, 4, 5, six=6, seven=7)

# def foo(a, b, *, c):
#     print(a, b, c)
    
# foo(1, 2, c=3)
# # foo(1, 2, 3, 4)

# def foo2(a, b, c):
#     print(a, b, c)

# my_list = [0, 1, 2]
# foo2(*my_list)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# foo2(**my_dict)

# numbers = [1, 2, 3, 4, 5, 6]
# numbers_tup = (1, 2, 3, 4, 5, 6)
# *beginning, last = numbers
# print(beginning)
# print(last)
# first, *remaining = numbers_tup
# print(first)
# print(remaining)
# first, *middle, last = numbers
# print(first)
# print(middle)
# print(last)
# print(type(middle))
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)



