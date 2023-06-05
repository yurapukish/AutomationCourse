from sys import getsizeof

s = None
print(id(s))
a = None
print(getsizeof(a))
a = ''
print(getsizeof(a))