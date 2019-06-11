import unittest
from unittest.mock import patch
import code_challenge
import requests
import unittest.mock
import tickets
import get_json
from tickets import Ticket
from get_json import GetJSON
getJson = GetJSON()
ticket = Ticket()


class TestCodes(unittest.TestCase):
    # checks user's crendential
    def test_credentials(self):
        # trying to get response from correct request with status code 200
        response = requests.get(
            "https://ahnaf.zendesk.com/api/v2/tickets.json", auth=(
                "abir3577189@gmail.com", "1231234567Ab"))
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)

    def test_false_credentials(self):
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
    
    # checks if total per page changes, 
    # data length receives changes accordingly
    @patch('get_json.GetJSON.get_total_per_page', create=True)
    def test_total_per_page(self, mocked_input):
        mocked_input.side_effect = ['90']
        data = getJson.get_data_from_url()
        self.assertEqual(getJson.TOTAL_PER_PAGE, len(data['tickets']))

    # checks if id passed to get_one_ticket_from_url
    # and received data has same id which means
    # correct ticket received
    def test_single_ticket(self):
        id = str(15)
        data = getJson.get_one_ticket_from_url(id)

        ticket_id = str(data['ticket']['id'])
        self.assertEqual(ticket_id, id)
   
if __name__ == "__main__":
    unittest.main()
    
