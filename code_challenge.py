# This is the main code to the code challenge
# used python3
# install pip3 install requests
# https://ahnaf.zendesk.com/api/v2/tickets/102.json -v -
# u abir3577189@gmail.com:15589633Ab

import os
import requests
import time
import json
from datetime import datetime


class CodingChallenge():
    def get_ticket(self):

        # reads the credentials from credentials.json file as read option
        with open("credentials.json", 'r') as f:

            # store values in credentials.json in a variable datastore
            datastore = json.load(f)

            # subdomain, email and password gets filled 
            # from values of credentials.json
            url = "https://"+datastore[
                "subdomain"]+".zendesk.com/api/v2/tickets/101.json"
            response = requests.get(url, auth=(
                datastore["email"], datastore["password"]))
        
        # runs if status code is 200 which means some data received from
        # the response with valid credentials
        if response.status_code == 200:
            print('Found ticket')
            data = json.loads(response.text)

            # gets id from data and convert the integer to string
            # for using in strings and asssigning to variables
            ticket_id = str(data['ticket']['id'])
            assinged_by = str(data['ticket']['assignee_id'])
            subject = data['ticket']['subject']

            # gets created_at from data json and formats into date format
            # and then converts into strings. ps. use of T and Z
            # is for satification of the format
            # received by data json
            created_at = str(datetime.strptime(
                data['ticket']['created_at'], '%Y-%m-%dT%H:%M:%SZ'))

            print("\n")
            print("Ticket Id", 2 * " ", "Subject",
                  32 * " ", "Created at", 10 * " ", "Assigned by")
            print("\n")
            
            string = "{:{fill}{align}{width}}"

            # passing format codes as arguments to format
            # the output easily readable
            print(string.format(
                ticket_id, fill='', align='<', width=13) + string.format(
                    subject, fill='', align='<', width=41) + string.format(
                    created_at, fill='', align='<', width=22) + string.format(
                    assinged_by, fill='', align='<', width=14))

        elif response.status_code == 404:
            print('No Result found. Please Try Again!!!')
    
    def get_all_tickets(self):
    
        # reads the credentials from credentials.json file as read option
        with open("credentials.json", 'r') as f:

            # store values in credentials.json in a variable datastore
            datastore = json.load(f)

            # subdomain, email and password gets filled 
            # from values of credentials.json
            url = "https://"+datastore[
                "subdomain"]+".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, auth=(
                datastore["email"], datastore["password"]))
        
        # runs if status code is 200 which means some data received from
        # the response with valid credentials

        if response.status_code == 200:
            print('Found ticket')
            data = json.loads(response.text)

            print("\n")
            print("Ticket Id", 2 * " ", "Subject",
                  41 * " ", "Created at", 10 * " ", "Assigned by")
            print(100 * "_")
            print("\n")
                
            counter = 0
            array_length = len(data['tickets'])

            for tickets in data['tickets']:
                # gets id from data and convert the integer to string
                # for using in strings and asssigning to variables
                ticket_id = str(tickets['id'])
                assinged_by = str(tickets['assignee_id'])
                subject = tickets['subject']

                # gets created_at from data json and formats into date format
                # and then converts into strings. ps. use of T and Z
                # is for satification of the format
                # received by data json
                created_at = str(datetime.strptime(
                    tickets['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
                string = "{:{fill}{align}{width}}"
      
                # passing format codes as arguments to format
                # the output easily readable
                print(string.format(
                    ticket_id, fill='', align='<', width=13) + string.format(
                        subject, fill='', align='<', width=50) + string.format(
                        created_at, fill='', align='<', width=22) +
                        string.format(
                        assinged_by, fill='', align='<', width=14))
               
        elif response.status_code == 404:
            print('No Result found. Please Try Again!!!')
           
    def display_menu(self):
        # This is the main display menu
        print("")
        print(30 * " ", "Welcome to Mobile Ticket viewer", 30 * " ")
        print("Please select an option from below:\n")
        print("1. List all the tickets ")
        print("2. List a single ticket ")
        print("Quit (Enter q or Q to Quit ) ")
     
    def menu(self):
        # clears out the screen everytime method menu is called
        os.system('cls||clear')
        
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.get_all_tickets()

            elif choice == "2":
                self.get_ticket()

            elif choice == "q" or choice == "Q":
                print("\nThanks for visiting. :)\n")
                break

            else:
                print("""\nInvalid selection!!!! please enter number 1, 2 or enter q or Q to Quit""")
                time.sleep(2)
                

if __name__ == '__main__':
    a = CodingChallenge()
    a.menu()

