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

filename = 'alice.txt'


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        # print(f'sorry the {filename} not found')
        pass
    else:
        words = content.split()
        print(f'{len(words)} words')


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)
