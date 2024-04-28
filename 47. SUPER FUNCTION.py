# super() = Function used to give access to methods in a parent class
# returns a temporary object of a parent class when used

# super class
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)
    # super method instead of
    # def __init__(self, length, width):
    #     self.length = length
    #     self.width = width
    # taking advantage of the inheritance

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
