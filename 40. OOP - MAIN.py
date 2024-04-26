from car import Car

car_1 = Car("Toyota", "Corolla", 2015, "Red")
car_2 = Car("Ford", "Mustang", 2019, "Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

print()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()
