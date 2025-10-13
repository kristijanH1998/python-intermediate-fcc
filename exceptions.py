# a = 5 + '10'
# import somemodule 
# a = 5
# b = c
# f = open('somefile.txt')
a = [1, 2, 3]
# a.remove(1)
# print(a)
# a.remove(4)
# a[4]
# print(a)
my_dict = {'name': 'Max'}
# my_dict['age']
my_dict['name']
x = -5
x = 5
# if x < 0:
#     raise Exception('x should be positive')

# assert (x <= 0), 'x is not negative'
# try:
#     a = 5 / 0
# except:
#     print('an error happened')

# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)

# try:
#     a = 5 / 0
#     b = a + '10'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

# try:
#     f = open('sth.txt')
# except Exception as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)

# try:
#     a = 5 / 0
#     b = a + 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up')

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
# test_value(200)

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
    
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small:', x)
# test_value(200)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)