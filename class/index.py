# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it')

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('you cant roll back an odometer!')

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# class Battery:
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f'this car has a {self.battery_size}-kwh battery')


# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

# class Admin:
#     def __init__(self, user_name, privileges):
#         self.user_name = user_name
#         self.privileges = Privileges(privileges)


# class Privileges:
#     def __init__(self, privileges):
#         self.privileges = privileges

#     def show_privileges(self):
#         print(f'privileges is {self.privileges}')


# user = Admin('brando', 'can do any')
# user.privileges.show_privileges()

# from car import Car
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# from random import randint, choice
# players = ['charles', 'eli', 'michael', 'florence']

# print(
#     choice(players)
# )


# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         print(randint(1, self.sides))

#     def loop_die(self, count):
#         turn = 1
#         while True:
#             turn += 1
#             self.roll_die()
#             if turn >= count:
#                 break


# six_roll = Die()
# six_roll.roll_die()

# ten_roll = Die(10)
# # ten_roll.roll_die()
# ten_roll.loop_die(20)

from random import choice, randint
import sys

sys.setrecursionlimit(3000)


class Ticket:
    def __init__(self):
        self.int_str = ['a',  'd',  '2', '3', '4']
        self.result = 'd333'
        self.count = 0

    def loop(self):
        test = ''

        while True:
            test += choice(self.int_str)

            if len(test) == 4:
                break

        if test != self.result:
            self.count += 1
            self.loop()

        if test == self.result:
            print(f'loop count: {self.count}')
            print(f'result: {test}')


begin = Ticket()
begin.loop()
