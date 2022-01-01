import unittest


def city_functions(city, country, population=5000):
    result = f'{city},{country}'
    return f'{result.title()} - population {population}'


class ResultTestClass(unittest.TestCase):
    def test_city_contry(self):
        format_city_contry = city_functions('shaoguan', 'china')
        self.assertEqual(format_city_contry,
                         'Shaoguan,China - population 5000')

    def test_city_contry_population(self):
        format_city_contry = city_functions('shaoguan', 'china', 8000)
        self.assertEqual(format_city_contry,
                         'Shaoguan,China - population 8000')


unittest.main()

# asserEqual(a,b)  核实 a == b
# asserNotEqual(a,b) 核实 a!== b
# asserTure(x) 核实x为true
# asserFalse(x) 核实x为false
# asserIn(item,list) 核实item在list中
# aseerNotIn(item,list) 核实item不在list中