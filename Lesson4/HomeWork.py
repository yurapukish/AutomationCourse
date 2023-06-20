"""
Homework 3.

We have four values w,x,y,z
write if-elif-else statement that will search minimum value and print
smth aka "'y' is minimum value'

"""
x, y, z, w = 100, 0, 32, 123

if x <= y and x <= z and x <= w:
    print("'x' is minimum value")
elif y <= x and y <= z and y <= w:
    print("'y' is minimum value")
elif z <= x and z <= y and z <= w:
    print("'z' is minimum value")
else:
    print("'w' is minimum value")
