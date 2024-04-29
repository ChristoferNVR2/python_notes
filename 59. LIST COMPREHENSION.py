# list comprehension = a way to create a list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]

squares = []  # create an empty list
for i in range(1, 11):  # create a for loop
    squares.append(i**2)  # define what each loop iteration should do
print(squares)

squares = [i**2 for i in range(1, 11)]  # list comprehension
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students = [i for i in students if i >= 60]
print(passed_students)

passed_students = [i if i >= 60 else 'Failed' for i in students]
print(passed_students)
