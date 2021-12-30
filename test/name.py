import unittest
from name_function import get_formatted_name

# print('enter q tp quit')
# while True:
#     first = input('input first name:')
#     if first == 'q':
#         break
#     last = input('input last name:')
#     if last == 'q':
#         break

#     formatted_name = get_formatted_name(first, last)
#     print(f'formatted:{formatted_name}')


class NameTestClass(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
