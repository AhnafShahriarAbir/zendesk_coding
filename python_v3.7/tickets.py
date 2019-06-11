import os
import time
import sys
# imports datetime to reformat the created data received from json
from datetime import datetime
from get_json import GetJSON
getJson = GetJSON()


class Ticket():
    def title(self):
        print("Ticket Id", 2 * " ", "Subject",
              41 * " ", "Created at", 10 * " ", "Assigned by")
        print(100 * "_")
        print("\n")

    # This method asks for ticket id first, validates the ticket id,
    # calls "get_one_ticket_from_url" from GetJSON class
    # and displays the ticket with that inputted ticket id.

    def get_ticket(self):
        # gets all the tickets to get the count of tickets
        data = getJson.get_data_from_url()
        data_length = data['count']

        while True:
            # runs until a valid ticket number is entered
            while True:
                print("\nPlease Enter the Ticket id to get the ticket.\n ")
                ticket_id = input('Enter Ticket ID: ')
                try:
                    # tries to convert the input into int throws
                    # ValueError if can not convert
                    value = int(ticket_id)
                except ValueError:
                    print("\nPlease enter number only\n")
                    time.sleep(1)
                    continue
                # if the input lies within the range, then loop breaks
                if 1 <= value <= data_length:
                    break
                else:
                    print(
                        "\nInvalid range..You have only " + str(data_length) +
                        " Tickets...\n")
                    time.sleep(1)

            os.system('clear')

            # gets data of a single ticket with validated ticket id
            data = getJson.get_one_ticket_from_url(ticket_id)
            ticket = data['ticket']
            if ticket is not None:
                self.title()
                self.show_ticket(ticket)  # displays the ticket
            else:
                print("\nCould not retrieve the ticket!!! Please try again")
            
            print("\n" + 5 * "-", "Search again" + 5 * "-"+"\n")
            print("1. Yes (type 1 to search ticket again) ")
            print("2. No (type 2 to go to Home page) ")
            print("\nQuit (type q or Q to Quit) ")

            choice = input("\nEnter your choice: ")
            if choice == "1":
                os.system('clear')
                continue

            elif choice == "2":
                os.system('clear')
                print("Returning to Home Page.............")
                time.sleep(1)
                break
                
            elif choice == "q" or choice == "Q":
                print("\nThanks for visiting. :)\n")
                sys.exit()
            else:
                print(
                    """\nInvalid selection!!!! Returning to home page""")
                time.sleep(2)
                break

    # This method is used to get all tickets.
    # First,all the data is received as json format.
    # variables are set from the data received,
    # calls "print_tickets" until the user doesn't quit or t
    # here is no more data.
    def get_all_tickets(self):
        while True:
            data = getJson.get_data_from_url()
            array_length = len(data['tickets'])
            tickets = data['tickets']
            next_page = data['next_page']
            prev_page = data['previous_page']

            os.system('clear')

            print("\nPage: {}".format(getJson.params['page']))
            print(9*"-")
            self.title()
            # prints tickets with page from params
            self.print_tickets(tickets, getJson.params['page'])

            print("\n\nOPTIONS\n")
            print("1. View next Page (Enter 1 to view next page) ")
            print("2. View Previous Page (Enter 2 to view previous page) ")
            print("3. Return to Home Page (type 3 to go to Home page) ")
            print("\nQuit (type q or Q to Quit) ")

            choice = input("\nEnter your choice: ")
            if choice == "1":
                if next_page is None:
                    os.system('clear')
                    print('No more pages left')
                    time.sleep(1)
                    
                else:
                    os.system('clear')
                    print("loading.............")
                    getJson.params['page'] += 1

            elif choice == "2":
                if prev_page is None:
                    os.system('clear')
                    print('\nCan\'t go further!!!!!!!')
                    print('You are already in the first page.')
                    time.sleep(1)

                else:
                    os.system('clear')
                    print("loading.............")
                    getJson.params['page'] -= 1

            elif choice == "3":
                os.system('clear')
                print("Returning to Home Page.............")
                time.sleep(1)
                break
            elif choice == "q" or choice == "Q":
                print("\nThanks for visiting. :)\n")
                sys.exit()

            else:
                print(
                    "\nInvalid selection!!!! please enter \"1,2,3\" or \"q/Q\""
                        )
                time.sleep(2)

    # This method loops through all the tickets and displays
    # in individual page
    def print_tickets(self, tickets, page):
        page_count = page*getJson.TOTAL_PER_PAGE
        for ticket in tickets:
            self.show_ticket(ticket)
            page_count += 1
        return

    def show_ticket(self, ticket):
        ticket_id = ticket["id"]
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
