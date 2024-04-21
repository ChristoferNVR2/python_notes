# tuple = immutable list

student = ("Chris", 18, "male")

print(student.count("Chris"))
print(student.index("male"))

for x in student:
    print(x)

if "Chris" in student:
    print("Chris is here")
