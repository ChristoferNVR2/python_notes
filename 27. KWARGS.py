# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying number of keyword arguments

def hello(**kwargs):
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')


hello(tittle='Mr.', first='Chris', middle='Nicolás', last='Vega')
