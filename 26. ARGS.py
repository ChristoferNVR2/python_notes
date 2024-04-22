# *args = parameter that will pack all the arguments in a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args):
    sum_ = 0
    # if we want to modify the first element of the tuple
    # we need to convert it to a list
    args = list(args)  # convert tuple to list
    args[0] = 0  # set the first element to 0
    for i in args:
        sum_ += i
    return sum_


print(add(1, 2, 3, 4, 5, 6))
