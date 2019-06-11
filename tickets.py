import os
import requests
import time
import json
import sys
from datetime import datetime
TOTAL_PAGE = 25
params = {"per_page": TOTAL_PAGE, "page": 1}


class Ticket():
    def get_data_from_url(self):
        # reads the credentials from credentials.json file as read option
        with open("credentials.json", 'r') as f:
            # store values in credentials.json in a variable datastore
            datastore = json.load(f)

            # subdomain, email and password gets filled
            # from values of credentials.json
            url = "https://"+datastore[
                "subdomain"]+".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, params=params, auth=(
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
            time.sleep(4)
    
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

    def title(self):
        # clears out the screen everytime method menu is called
        os.system('clear')
        print("Ticket Id", 2 * " ", "Subject",
              41 * " ", "Created at", 10 * " ", "Assigned by")
        print(100 * "_")
        print("\n")

    # This method asks for ticket id first, validates the ticket id,
    # looks through the data
    # in tickets.json and displays the ticket with
    # that inputted ticket id.
    def get_ticket(self):
        while True:

            # runs until a valid ticket number is entered
            while True:
                print("Please Enter the Ticket id to get the ticket.\n ")
                ticket_id = input('Enter Ticket ID: ')
                try:
                    # tries to convert the input into int throws
                    # ValueError if can not convert
                    value = int(ticket_id)
                except ValueError:
                    print("\nPlease enter number only\n")
                    time.sleep(2)
                    continue
                # if the input lies within the range, then loop breaks
                # if 1 <= value <= array_length:
                #     break
                # else:
                #     print(
                #         "\nInvalid range..You have only " + " Tickets...\n")
                #     time.sleep(2)
                else:
                    break
            ticket = self.get_one_ticket_from_url(ticket_id)
            if ticket is not None:
                for t in ticket:
                    print(t)
                    # self.title()
                    # self.show_ticket(ticket)
            else:
                print("Could not retrieve the ticket!!! Please try again")
            
            print("\n" + 5 * "-", "Search again" + 5 * "-"+"\n")
            print("1. Yes (type y to search ticket again) ")
            print("2. No (type n to go to Home page) ")
            print("3. Quit (type q or Q to Quit) ")
            choice = input("Enter your choice: ")
            if choice == "y":
                # clears out the screen everytime method menu is called
                os.system('clear')
                continue

            elif choice == "n":
                break
            elif choice == "q" or choice == "Q":
                print("\nThanks for visiting. :)\n")
                sys.exit()
            else:
                print(
                    """\nInvalid selection!!!! Returning to home page""")
                time.sleep(2)
                break

    def get_all_tickets(self):
       
        # if array_length > 25:
        #     for ticket in tickets:
        #         self.show_pages(tickets, counter, counter+25)
        while True:
            data = self.get_data_from_url()
            array_length = len(data['tickets'])
            tickets = data['tickets']
            next_page = data['next_page']

            # clears out the screen everytime method menu is called
            os.system('clear')

            print(5*"-", "\nPage: {}".format(params['page']))
            print(9*"-")
            self.title()
            self.print_tickets(tickets, params['page'])

            print("\nView next Page\n")
            print("1. Yes (type y to view next page) ")
            print("2. No (type n to go to Home page) ")
            choice = input("Enter your choice: ")
            if choice == "y":
                if next_page is None:
                    os.system('clear')
                    print('No more pages left')
                    time.sleep(1)
                    
                else:
                    os.system('clear')
                    print("loading.............")
                    params['page'] += 1
                    
            elif choice == "n":
                os.system('clear')
                print("Returning to Home Page.............")
                time.sleep(1)
                break
            else:
                print(
                    "\nInvalid selection!!!! please enter \"y\" or \"n\" ")
                time.sleep(2)

    def print_tickets(self, tickets, page):
        start = page*TOTAL_PAGE - 24

        for ticket in tickets:
            self.show_ticket(ticket)
            start += 1
        return

    def get_id_from_user(self, id):
        data = self.get_data_from_url()
        tickets = data['tickets']
        for ticket in tickets:
            if id == ticket['id']:
                return ticket

    def show_ticket(self, ticket):
        ticket_id = ticket['ticket']["id"]
        assinged_by = str(ticket['ticket']['assignee_id'])
        subject = ticket['ticket']['subject']

        # gets created_at from data json and formats into date format
        # and then converts into strings. ps. use of T and Z
        # is for satification of the format
        # received by data json
        created_at = str(datetime.strptime(
            ticket['ticket']['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
        string = "{:{fill}{align}{width}}"

        # passing format codes as arguments to format
        # the output easily readable
        print(string.format(
            ticket_id, fill='', align='<', width=13) + string.format(
            subject, fill='', align='<', width=50) + string.format(
            created_at, fill='', align='<', width=22) +
            string.format(
            assinged_by, fill='', align='<', width=14))
