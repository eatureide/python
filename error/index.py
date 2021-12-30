# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('no')

# print('give me two numbers and i will divide them')
# print('enter q to quit')

# while True:
#     first_number = input('first number:')
#     if first_number == 'q':
#         break
#     second_number = input('second number:')
#     if second_number == 'q':
#         break

#     try:
#       answer = int(first_number) / int(second_number)
#     except:
#       print('you cant divide by 0')
#     else:
#       print(answer)


# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             content = f.read()
#     except FileNotFoundError:
#         # print(f'sorry the {filename} not found')
#         pass
#     else:
#         words = content.split()
#         print(f'{len(words)} words')


# filenames = ['alice.txt', 'siddhartha.txt',
#              'moby_dick.txt', 'little_women.txt']

# for filename in filenames:
#     count_words(filename)


# def add():
#     while True:
#         first_num = input('input first number')
#         if first_num == 'q':
#             break
#         last_num = input('input last num')
#         if last_num == 'q':
#             break

#         try:
#             result = int(first_num) + int(last_num)
#             print(result)
#         except ValueError:
#             print('error value')


# add()

# text_data = ['learning_python.txt', 'pi_digits.txt', 'moby_women.txt']

# for file in text_data:
#     try:
#         with open(file) as file_object:
#             content = file_object.read()
#             print(content)
#     except:
#         pass
# print('not found')

# r 只读方式打开文件，默认
# w 打开一个文件用于写入，如果文件不存在，则创建文件
# a 打开文件用于追加，文件存在则写入文件末尾，不存在则创建文件

# with open('little_women.txt') as file_object:
#     content = file_object.read().lower()

#     print(content.count('row'))

# import json
# # numbers = [i for i in range(10)]

# # filename = 'numbers.json'
# # with open(filename) as f:
# #     # json.dump(numbers, f)
# #     print(json.load(f))
# filename = 'username.json'
# username = input('input your name:')
# with open(filename, 'w') as f:
#     json.dump(username, f)

# with open(filename) as f:
#     print(json.load(f))
