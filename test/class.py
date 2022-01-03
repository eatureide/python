import unittest


class AnonymouseSurvery:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('survery results')
        for response in self.responses:
            print(f'- {response}')


class TestAnonymouseSurvey(unittest.TestCase):

    def setUp(self):
        question = 'what language did you first learn to speak?'
        self.my_survery = AnonymouseSurvery(question)
        self.responses = ['english', 'spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survery.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survery.responses)

    def test_store_three_responses(self):

        for response in self.responses:
            self.my_survery.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survery.responses)


unittest.main()
