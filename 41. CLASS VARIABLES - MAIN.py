from car import Car

car_1 = Car("Toyota", "Corolla", 2015, "Red")
car_2 = Car("Ford", "Mustang", 2019, "Blue")

Car.wheels = 5
# The class variable wheels is shared by all instances of the Car class.
# The class variable is independent of the object and is shared by all objects of the class.

print(car_1.wheels)
print(car_2.wheels)
