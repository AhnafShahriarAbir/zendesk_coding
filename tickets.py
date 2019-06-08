import os
import requests
import time
import json
from datetime import datetime


class Ticket():
    data = ""

    def get_data_from_url(self):
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
            data = json.loads(response.text)

        elif response.status_code == 404:
            print("\nRequest failed. Please check and try Again!!!\n")
            time.sleep(2)
            data = None

        # returns data with json output or None which will be used
        # in get_ticket method
        return data

    # This method asks for ticket id first, validates the ticket id,
    # looks through the data
    # in tickets.json and displays the ticket with
    # that inputted ticket id.
    def get_ticket(self):
        data = self.get_data_from_url()
        if data is not None:
            tickets = data['tickets']

            # gets the total number of tickets
            array_length = len(tickets)
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
                    if 1 <= value <= array_length:
                        break
                    else:
                        print(
                            "\nInvalid range..You have only " + str(
                                array_length) + " Tickets...\n")
                        time.sleep(2)

                for ticket in tickets:
                    if ticket_id == str(ticket['id']):
                        os.system('cls||clear')
                        print("\n")
                        print("Ticket Id", 2 * " ", "Subject",
                              41 * " ", "Created at", 10 * " ", "Assigned by")
                        print(100 * "_")
                        print("\n")
                        # clears out the screen everytime method menu is called
                        self.show_ticket(ticket)
                        break

                print("\n" + 5 * "-", "Search again" + 5 * "-"+"\n")
                print("1. Yes (type y to search ticket again) ")
                print("2. No (type n to go to Home page) ")
                choice = input("Enter your choice: ")
                if choice == "y":
                    # clears out the screen everytime method menu is called
                    os.system('cls||clear')
                    continue

                elif choice == "n":
                    break
                else:
                    print(
                        """\nInvalid selection!!!! Returning to home page""")
                    time.sleep(2)
                    break

    def get_all_tickets(self):
        pass
        # self.show_tickets(data)

    def show_ticket(self, ticket):
        ticket_id = str(ticket['id'])
        assinged_by = str(ticket['assignee_id'])
        subject = ticket['subject']

        # gets created_at from data json and formats into date format
        # and then converts into strings. ps. use of T and Z
        # is for satification of the format
        # received by data json
        created_at = str(datetime.strptime(
            ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
        string = "{:{fill}{align}{width}}"

        # passing format codes as arguments to format
        # the output easily readable
        print(string.format(
            ticket_id, fill='', align='<', width=13) + string.format(
            subject, fill='', align='<', width=50) + string.format(
            created_at, fill='', align='<', width=22) +
            string.format(
            assinged_by, fill='', align='<', width=14))

    def show_tickets(self, data):
        array_length = len(data['tickets'])
        counter = 1
        tickets = data['tickets']
        # if array_length > 25:
        #     for ticket in tickets:
        #         self.show_pages(tickets, counter, counter+25)

        while counter < array_length:

            print("\n")
            print("Ticket Id", 2 * " ", "Subject",
                  41 * " ", "Created at", 10 * " ", "Assigned by")
            print(100 * "_")
            print("\n")
            max = counter+24

            counter = self.show_pages(tickets, counter, max)
            counter += 1

            print("\nView next Page\n")
            print("1. Yes (type y to view next page) ")
            print("2. No (type n to go to Home page) ")
            choice = input("Enter your choice: ")
            if choice == "y":
                # clears out the screen everytime method menu is called
                os.system('cls||clear')
                continue

            elif choice == "n":
                break
            else:
                print(
                    """\nInvalid selection!!!! please enter y or n""")
        print("Played All tickets. Returned to home page")

    def show_pages(self, tickets, counter, max):
        for ticket in tickets:
            for counter in range(counter, max+1, 1):
                # gets id from data and convert the integer to string
                # for using in strings and asssigning to variables
                self.show_ticket(ticket)
                print("Counter: " + str(counter))
        return counter
