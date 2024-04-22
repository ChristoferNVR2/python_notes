# str.format() = optional method that gives users more control when displaying output

animal = 'cow'
item = 'moon'

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format('cow', 'moon'))
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))  # positional argument

# if we don't want to use positional arguments, we can use keyword arguments
print("The {animal} jumped over the {item}".format(animal='cow', item='moon'))

text = "The {} jumped over the {}"
print(text.format(animal, item))


name = "Chris"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))  # padding
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left align
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # right align
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # center align

pi = 3.14159
number = 1000

print("The number pi is {:.2f}".format(pi))  # 2 decimal places
print("The number is {:,}".format(number))  # comma separator
print("The number is {:b}".format(number))  # binary
print("The number is {:o}".format(number))  # octal
print("The number is {:x}".format(number))  # hexadecimal
print("The number is {:e}".format(number))  # scientific notation
