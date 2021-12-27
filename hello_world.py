# array = ['typescript', 'javascript', 'nodejs']
# msg = f'her name is {array[1]}'
# print(msg)
# print(f'hi {array[0]}')
# array.append('script')
# print(array)

# array.insert(1, 'haha')
# print(array)

# del array[1]
# pop_item = array.pop()
# print(pop_item)

# array.remove('mike1')
# print(array)

# print(f'{array[1]} pigeon')
# array.remove('javascript')
# array.append('python')
# print(array)
# array.insert(0, 'java')
# array.insert(1, 'c++')
# array.append('go')
# print(array)

# print(f'only {array[1]}&{array[3]}')
# print(f'fuck off{array.pop()}')
# print(f'fuck off{array.pop()}')
# print(f'{array} have a good night')

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# print(cars)
# print(sorted(cars))
# cars.reverse()
# print(cars)

# cities = ['shaoguan', 'guangzhou', 'wengyuan', 'xianggang', 'taiwan']
# print(sorted(cities))
# print(cities)
# sorted(cities)
# cities.reverse()
# print(cities)
# cities.sort()
# print(cities)
# cities.sort(reverse=True)
# print(len(cities))
# for item in cities:
# print(item)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick!')
#     print(f'i cant wait to see your next trick {magician.title()}. \n')

#     print('thank you everyone that was a great magic show!')

# pizzas = ['pepperoni', 'chicken', 'beef']
# for pizza in pizzas:
#     print(f'i like {pizza} pizza')

# print('i really love pizza')


# animals = ['cat', 'dog', 'pig']
# for animal in animals:
#     print(f'a {animal} would like a great prt')

# print('these animals would a great pet')

# for value in range(5):
#     print(value)

# numbers = list(range(1, 11))
# squares = []

# for value in numbers:
#     squares.append(value ** 2)

# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# numbers = list(range(21))
# for number in numbers:
#     print(number)

# bigNumbers = list(range(1_000_000))
# print(min(bigNumbers))
# print(max(bigNumbers))
# print(sum(bigNumbers))
# print(list(range(1, 21, 3)))
# numbers = list(range(3, 31, 3))
# for number in numbers:
#     print(number)

# numberSquare = [value ** 2 for value in range(11)]
# for number in numberSquare:
#     print(number)
# print(numberSquare)

# numberList = list(range(10))
# squares = []
# for number in numberList:
#     squares.append(number ** 2)
# print(squares)

# players = ['charles', 'martina', 'micheal', 'eli']
# for player in players[:3]:
#     print(player)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print(my_foods)
# print(friend_foods)

# foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'humberger']
# print(foods[:3])

# print(foods[1:-1])

# print(foods[-3:])
# originFoods = foods[:]
# otherFoods = foods[:]
# originFoods.append('apple')
# otherFoods.append('peach')

# print(originFoods)
# print(otherFoods)

# for originFood in originFoods:
#     print(f'my favorite foods are:{originFood}')

# for otherFood in otherFoods:
#     print(f'other favorite foods are:{originFood}')

# dismensions = (20, 50)
# dismensions[0] = 5
# print(dismensions)
# foods = ('pizza', 'falafel', 'carrot cake', 'ice cream', 'humberger')
# for food in foods:
#     print(food)

# foods = ('other')

# print(foods)

# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# age_0 = 22
# age_1 = 18
# # # print(age_0 >= 21 and age_1 >= 21)
# # print(age_0 >= 21 and age_1 <= 21)

# print(age_0 >= 21 or age_1 <= 21)


# requested_toppings = ['mushroom', 'onions', 'pineapple']
# print('onions' in requested_toppings)

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(f'{user.title()}, you can submit')


# car = 'subaru'
# print(car == 'subaru')
# print(car == 'audi')

# age_0 = 1
# age_1 = 2

# print(age_0 >= 0 or age_1 >= 1)
# print(age_0 >= 0 and age_1 >= 1)


# cars = ['a', 'b', 'c']
# if 'd' not in cars:
#     print('d not in cars')

# car = 'test'
# if car:
#     print('car')

# age = 12

# if age < 4:
#     print('free')
# elif age < 18:
#     print('cost $25')
# else:
#     print('cost $40')

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print('adding mushrooms')
# if 'pepperoni' in requested_toppings:
#     print('adding pepperoni')
# if 'extra cheese' in requested_toppings:
#     print('adding extra cheese')

# print('\n finished  marking your pizza')

# alien_color = 'yellow'
# if alien_color == 'green':
#     print('5 point')
# elif alien_color == 'red':
#     print('10 point')
# else:
#     print('15 point')

# age = 2
# if age >= 2 and age <= 4:
#     print('baby')
# elif age >= 4 and age <= 13:
#     print('child')
# elif age >= 13 and age <= 20:
#     print('yong')
# else:
#     print('old')


# requested_toppings = ['a', 'b', 'c']

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'adding {requested_topping}')
#     print('finish')
# else:
#     print('are you want a plain pizza?')
# available_toppings = ['mushrooms', 'olives',
#                       'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'adding {requested_topping}')
#     else:
#         print(f'sorry we don t have {requested_topping}')

# print('finish')

# customer_toppings = ['c', 'f']
# shop_toppings = ['a', 'b', 'c', 'd', 'e']

# for customer_topping in customer_toppings:
#     if customer_topping in shop_toppings:
#         print(f'you can adding {customer_topping}')
#     else:
#         print(f'no {customer_topping}')

# current_users = ['john', 'jojo', 'DIO', 'puqi', 'taro']
# current_users_upper = []
# for current_user in current_users:
#     current_users_upper.append(current_user.upper())

# new_users = ['tony', 'allen', 'death', 'dio', 'taro']
# print(current_users_upper)
# for new_user in new_users:
#     if new_user in current_users or new_user.upper() in current_users_upper:
#         print(f'the name {new_user} used.')
#     else:
#         print('you cna use the name')

#  [value ** 2 for value in range(1, 11)]
# numbers = [value for value in range(0, 10)]

# for number in numbers:
#     if number == 1:
#         print('1st')
#     elif number == 2:
#         print('2nd')
#     elif number == 3:
#         print('3rd')
#     else:
#         print(f'{number}th')


# alien_0 = {
#     'color': 'green',
#     'point': 5
# }
# # print(alien_0)
# # alien_0['x_position'] = 0
# # alien_0['y_position'] = 25

# alien_0['color'] = 'yellow'
# print(alien_0)


# alien_0 = {
#     'x_position': 0,
#     'y_position': 25,
#     'speed': 'medium'
# }

# print(f"original postion:{alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(alien_0)

# alien_0 = {
#     'color': 'green',
#     'positions': 5
# }

# del alien_0['positions']
# print(alien_0)

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# language = favorite_language['sarah'].title()
# print(f'sarah favorite language is {language}')

# alien_0 = {
#     'color': 'red'
# }
# print(alien_0.get('points'))

# human = {
#     'first_name': 'e',
#     'last_name': 'ature',
#     'age': 26,
#     'city': 'guangzhou'
# }
# # for h in human:
# #     print(human[h])
# # for key, value in human.items():
# #     print(key)
# #     print(value)

# print(human.keys())

# fav_languages = {
#     'phil': 'c',
#     'sarah': 'javascirpt'
# }
# friends = ['phil', 'sarah']
# for name in fav_languages.keys():
#     print(f'hi {name.title()}')
#     if name in friends:
#         language = fav_languages[name].title()
#         print(f'\t{name.title()},i see you love {language}')


# favorite_languages = {'jen': 'python', 'sarah': 'c',
#                       'edward': 'ruby', 'phil': 'python'}

# if 'erin' not in favorite_languages.keys():
#     print('erin,please take our poll')

# for name in sorted(favorite_languages.keys()):
#     print(name)

# values = favorite_languages.values()
# print(set(values))

# for human, value in favorite_languages.items():
#     print(f'{human} favorite language:')
#     print(f'{value}\n')

# if 'eature' not in favorite_languages.keys():
#     print('hi eatrue please join us pill')

# alien_0 = {'color': 'green', 'point': '5'}
# alien_1 = {'color': 'yellow', 'point': '10'}
# alien_2 = {'color': 'red', 'point': '15'}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['point'] = 10

# print(aliens[:10])

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }

# print(f"you ordered a { pizza['crust'] } -curst pizza"
#     "with you followping toppings")

# for topping in pizza['toppings']:
#     print(topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }

# for name, languages in favorite_languages.items():
#     print(f'\n{name.title()} s favorite languages are:')
#     for language in languages:
#         print(f'\t{language.title()}')

# for name in favorite_languages:
#     print(f'\n{name.title()} favorite languages are')
#     for language in favorite_languages[name]:
#         print(f'\t{language.title()}')

# users = {
#     'einstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'perinceton'
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#     }
# }

# for username, user_info in users.items():
#     print(f'\nUsername:{username}')
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f'\tfull name:{full_name}')
#     print(f'\tlocation :{location}')

# message = input('tell me something, and i will repeat it back to you:')
# print(message)

# name = input('please enter your name:')
# print(f'\nHello,{name}!')

# age = input('how old are you?')
# print(int(age) >= 18)

# height = input('hot tall are you in inches?')
# height = int(height)

# if height >= 48:
#     print('you are tall enough to ride')
# else:
#     print('you be able to ride')

# current_number = 1
# while current_number < 5:
#     print(current_number)
#     current_number += 1

# prompt = 'tell me something and i will repeat it back to you'
# prompt += "\nenter 'quit' to end the program:"

# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f'i d love to go to {city.title()}!')

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# quit = ''
# while True:
#     quit = input('input your topping then will be return tour msg:')
#     if quit == 'quit':
#         break
#     print(quit)


# age = ''
# quit = ''
# while True:
#     age = int(input('your age:'))
#     if age < 3:
#         print('free')
#     elif age >= 3 and age <= 12:
#         print('10$')
#     elif age >= 12:
#         print('15$')
#     if quit == 'quit':
#         break

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f'verifying user:{current_user.title()}')
#     confirmed_users.append(current_user)

# print(unconfirmed_users)
# print(confirmed_users)

# pets = ['dog','cat','dog','cat']
# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# responses = {}

# polling_active = True

# while polling_active:
#     name = input('\n what is your name?')
#     response = input('which mountain would you like climb someday?')

#     responses[name] = response

#     repeat = input('other one?')
#     if repeat == 'no':
#         polling_active = False

# print(responses)

# sandwitch = {}
# start = True

# while start:
#     name = input('input sandwitch name:')
#     topping = input('input topping:')

#     sandwitch[name] = topping

#     repeat = input('other one?')
#     if repeat == 'no':
#         start = False

# print(sandwitch)

# def greet_user(username):
#     print(username)

# greet_user('hi')

# def describe_pet(animal_type, pet_name = 'dog'):
#     print(f'i have a {animal_type}')
#     print(f"my {animal_type}'s name is {pet_name.title()}")

# describe_pet(animal_type='hamster')


# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'

#     return full_name.title()


# print(get_formatted_name(first_name='dio', last_name='brando', middle_name='s'))


# def build_person(first_name, last_name):
#     return {
#         'first': first_name,
#         'last': last_name
#     }


# print(build_person('dio', 'brando'))

# def build_person(first_name, last_name, age=None):
#     person = {
#         'first': first_name,
#         'last': last_name
#     }
#     if age:
#         person['age'] = age

#     return person


# person = build_person(first_name='jimi', last_name='hendrix', age=27)
# print(person)


# def make_album(singer_name, music_name):
#     return {
#         'singer': singer_name,
#         'music': music_name
#     }


# while True:
#     singer = input('singer name:')
#     if singer == 'q':
#         break
#     music = input('music name:')
#     if music == 'q':
#         break

#     print(make_album(singer_name=singer, music_name=music))

# name_list = ['dio', 'jojo', 'popo']

# def say_heelo(list):
#     for item in list:
#         print(f'hello {item.title()}')

# say_heelo(name_list)

# list_1 = ['dio', 'jojo', 'rabdo', 'johne']
# list_2 = []


# def transfer_list(list, result):
#     while list:
#         result.append(list.pop())
#     return result


# print(transfer_list(list_1[:], list_2))

# def make_pizza(size, *toppings):
#     print(size)
#     print(toppings)


# make_pizza('a', 'b', 'c')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile(
#     'albert', 'einstein', location='priceton', field='physics')
# print(user_profile)

# def sanwich(*topping):
#     print(topping)


# sanwich('beaf', 'chicken', 'fish')

# def user_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# print(user_profile('dio', 'brando', location='usa'))
# from pizza import make_pizza


# from pizza import make_pizza as mp
# mp('16', 'beaf', 'tomato')

# from pizza import make_pizza
# make_pizza('16', 'beaf')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f'{self.name} is now setting')

#     def roll_over(self):
#         print(f'{self.name} roll over!')


# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)

# your_dog.sit()
# my_dog.sit()


# class Restaurant:
#     def __init__(self, restaunt_name, cuisine_type):
#         self.resetanunt_name = restaunt_name
#         self.cusine_type = cuisine_type

#     def describe_restanut(self):
#         print(self.resetanunt_name, self.cusine_type)

#     def besiness_time(self):
#         print(f'{self.resetanunt_name} opening')


# my_resetuant = Restaurant('kfc', 'jumk')

# my_resetuant.describe_restanut()
# my_resetuant.besiness_time()

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name

#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it')

#     def update_odometer(self, mileage):
#         # if mileage>=self.odometer_reading:
#         #     self.odometer_reading = mileage
#         # else:
#         #     print('you cant roll back an odometer!')
#         print()

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# # my_new_car.update_odometer(23)
# # my_new_car.update_odometer(20)
# my_new_car.increment_odometer(23_500)
# my_new_car.read_odometer()

# class Restuant:
#     def __init__(self, restuant_name, restuant_type):
#         self.name = restuant_name
#         self.type = restuant_type
#         self.count = 0

#     def restuant_info(self):
#         print(f'{self.name} {self.type} {self.count}')

#     def set_number_served(self, count):
#         self.count = count

#     def increment_number_served(self, count):
#         self.count += count


# # my_restuant = Restuant('kfc', 'jumk')
# # my_restuant.set_number_served(10)
# # my_restuant.increment_number_served(400)
# # my_restuant.restuant_info()


# class RestuantExtend(Restuant):
#     def __init__(self, restuant_name, restuant_type):
#         super().__init__(restuant_name, restuant_type)


# check = RestuantExtend('kfc', 'jumk')
# check.restuant_info()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cant roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f'this car has a {self.battery_size}-kwh battery')


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()