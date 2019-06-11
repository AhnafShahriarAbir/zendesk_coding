import json
import requests
import os
import time


class GetJSON():
    # Initialises with total_per_page and params
    # changing total_per_page will changes the output of tickets
    # shown in per page
    def __init__(self):
        self.TOTAL_PER_PAGE = 25
        self.params = {"per_page": self.TOTAL_PER_PAGE, "page": 1}
    
    def get_total_per_page(self):
        return self.TOTAL_PER_PAGE

    def get_params(self):
        return self.params
        
    def get_data_from_url(self):
        # reads the credentials from credentials.json file as read option
        with open("credentials.json", 'r') as f:
            # store values in credentials.json in a variable datastore
            datastore = json.load(f)

            # subdomain, email and password gets filled
            # from values of credentials.json
            url = "https://"+datastore[
                "subdomain"]+".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, params=self.params, auth=(
                datastore["email"], datastore["password"]))
            data = self.check_response(response)
        return data

    def get_one_ticket_from_url(self, id):
        # reads the credentials from credentials.json file as read option
        with open("credentials.json", 'r') as f:
            # store values in credentials.json in a variable datastore
            datastore = json.load(f)

            # subdomain, email and password gets filled
            # from values of credentials.json
            url = "https://"+datastore[
                "subdomain"]+".zendesk.com/api/v2/tickets/"+id+".json"
            response = requests.get(url, auth=(
                datastore["email"], datastore["password"]))
            data = self.check_response(response)
        return data

    def check_response(self, response):
        # runs if status code is 200 which means some data received from
        # the response with valid credentials
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            print("\nRequest failed. Please check and try Again!!!\n")
            time.sleep(2)
