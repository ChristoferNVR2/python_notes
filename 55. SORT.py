# sort() method = used with lists
# sorted() function = used with iterables

students_list = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students_list.sort()
# we can also use the parameter reverse=True to sort in reverse order
# students.sort(reverse=True)

for i in students_list:
    print(i)

students_tuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")

# students_.sort()
# we cannot use the sort() function with tuples

sorted_students = sorted(students_tuple)

# we are printing the tuple (not necessary sorted)
for i in students_tuple:
    print(i)

# we are printing the sorted tuple (actually is a list)
for i in sorted_students:
    print(i)

students_matrix = [("Squidward", "F", 60),
                   ("Sandy", "A", 33),
                   ("Patrick", "D", 36),
                   ("Spongebob", "B", 20),
                   ("Mr. Krabs", "C", 78)]

# we are sorting the matrix by the first element of each tuple
students_matrix.sort()

for i in students_matrix:
    print(i)

# we are sorting the matrix by the second element of each tuple
grade = lambda grades: grades[1]
students_matrix.sort(key=grade)

for i in students_matrix:
    print(i)

# we are sorting the matrix by the third element of each tuple
age = lambda ages: ages[2]
students_matrix.sort(key=age)

for i in students_matrix:
    print(i)

students_tuple_of_tuples = (("Squidward", "F", 60),
                            ("Sandy", "A", 33),
                            ("Patrick", "D", 36),
                            ("Spongebob", "B", 20),
                            ("Mr. Krabs", "C", 78))

age = lambda ages: ages[2]
sorted_students_ = sorted(students_tuple_of_tuples, key=age)

for i in sorted_students_:
    print(i)
