name = input("What is your name?: ")
age = int(input("How old are you?: "))  # we need to convert the input to an integer
height = float(input("How tall are you?: "))

age = age + 1

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + " cm tall")
# we also need to convert the age to a string to concatenate it with the other strings
