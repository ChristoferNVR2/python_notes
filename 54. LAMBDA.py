# lambda functions = function written in one line using lambda keyword
# accepts any number of arguments, but only one expression
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lambda parameters: expression

# def double(x):
#     return x * 2
#
#
# print(double(5))

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + ' ' + last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5, 6))
print(add(5, 6, 7))
print(full_name('Chris', 'Vega'))
print(age_check(18))

# Notice that pycharm give us a warning that we can replace lambda with a function
# specifically "PEP 8: E731 do not assign a lambda expression, use a def"
# This is a code style recommendation by PEP 8 that provide us recommendations
# on how to write readable and consistent python code
# In this specific case of warning E731, it suggests that we do not assign a lambda
# expression to a variable and instead use a def to define a function (def) if the
# function is complex enough to require a name, or simply use the lambda expression
# directly where it is needed
# for example
# instead of
# double = lambda x: x * 2
# use
# def double(x):
#     return x * 2
# or
# print((lambda x: x * 2)(5))
