import unittest
from unittest.mock import patch
import json

from my_package.requests_get_module import get_current_weather


class TestMyBigModuleMethods(unittest.TestCase):

    @unittest.skip(reason='Instead of using requests.get we will mock it.')
    def test_requests_get(self):
        response = get_current_weather()
        self.assertEqual(
            response['message'],
            'Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.',
            'get_current_weather has returned incorrect result.'
        )

    def test_get_current_weather(self):
        with open('my_package/example_of_api_response.json', 'r') as file:
            json_response = json.loads(file.read())

        with patch('requests.get') as mock:
            mock.return_value.ok = True
            # The method json will return the dictionary that we have read from example_of_api_response.json
            mock.return_value.json.return_value = json_response
            result = get_current_weather()

        self.assertEqual(result['temp'], 274.31, 'get_current_weather has returned incorrect result.')


if __name__ == '__main__':
    unittest.main()
