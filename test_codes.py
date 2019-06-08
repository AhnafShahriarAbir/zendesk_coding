import unittest
from unittest.mock import patch
import code_challenge
import requests
import unittest.mock
import tickets
from tickets import Ticket


class TestCodes(unittest.TestCase):
   
    def test_credentials(self):
        # trying to get response from correct request with status code 200
        response = requests.get(
            "https://ahnaf.zendesk.com/api/v2/tickets.json", auth=(
                "abir3577189@gmail.com", "1231234567Ab"))
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)

        # Changing password or anything on the url will result 401 or 400
        response = requests.get(
            "https://ahnaf.zendesk.com/api/v2/tickets.json", auth=(
                "abir35771@gmail.com", "Random Password"))
        self.assertEqual(response.status_code, 401 or 400)

    # raises value error on input when strings are passed
    @patch('tickets.input', create=True)
    def test_check_input(self, mocked_input):
        mocked_input.side_effect = ['ff']
        tickets.Ticket.get_ticket
        self.assertRaises(ValueError)

    # prints invalid range when invalid ticket id is passed
    @patch('tickets.input', create=True)
    def test_check_input(self, mocked_input):
        mocked_input.side_effect = [250]
        tickets.Ticket.get_ticket
        self.assertTrue("\nInvalid range..You have only ")
    
    # prints exit message when 3 is entered in main menu
    @patch('code_challenge.input', create=True)
    def test_main_menu(self, mocked_input):
        mocked_input.side_effect = [3]
        code_challenge.CodingChallenge.menu
        self.assertTrue("\nThanks for visiting. :)\n")
 
if __name__ == "__main__":
    unittest.main()
    
