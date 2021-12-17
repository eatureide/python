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


favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python'}

# if 'erin' not in favorite_languages.keys():
#     print('erin,please take our poll')

# for name in sorted(favorite_languages.keys()):
#     print(name)

# values = favorite_languages.values()
# print(set(values))

for human, value in favorite_languages.items():
    print(f'{human} favorite language:')
    print(f'{value}\n')

if 'eature' not in favorite_languages.keys():
    print('hi eatrue please join us pill')
