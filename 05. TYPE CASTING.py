# Type casting = converting one data type to another

x = 1  # int
y = 2.0  # float
z = "3"  # string

x = float(x)
y = int(y)

print(x)
print(y)  # or only print(int(y))
print(z*3)  # as a string it will print 3 three times
print(int(z)*3)  # as an integer it will print 3 three times
# we also can z = int(z) and then print(z*3)

print("x is " + str(x))
print("y is " + str(y))
# we need to use str() to convert int or float to string to concatenate with another string
