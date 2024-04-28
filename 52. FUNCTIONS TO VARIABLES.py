def hello():
    print("Hello")


hi = hello  # hi is now an alias for hello
# they have the same memory address
hello()
hi()

say = print
say("I can't believe this works!")
