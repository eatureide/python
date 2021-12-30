import json


# def get_stored_username():
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username


# def get_new_username():
#     username = input('what is your name?')
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username


# def greet_user():
#     username = get_stored_username()
#     if username:
#         print(f'welcome back {username}')
#     else:
#         username = get_new_username()
#         print(f'we well remember {username}')


# greet_user()

# r 只读方式打开文件，默认
# w 打开一个文件用于写入，如果文件不存在，则创建文件
# a 打开文件用于追加，文件存在则写入文件末尾，不存在则创建文件


# def fav_number():
#     number = input('what is your fav number?')
#     file_name = 'fav_number.json'
#     with open(file_name, 'w') as f:
#         json.dump(number, f)


# fav_number()

# def load_fav_number():
#     file_name = 'fav_number.json'
#     try:
#         with open(file_name) as f:
#             content = f.read()
#     except FileNotFoundError:
#         print('no file')
#     else:
#         print(content)


# load_fav_number()