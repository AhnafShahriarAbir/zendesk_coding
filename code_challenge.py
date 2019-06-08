# This is the main code to the code challenge
# used python3
# install pip3 install requests
# https://ahnaf.zendesk.com/api/v2/tickets/102.json -v -
# u abir3577189@gmail.com:15589633Ab

from tickets import Ticket
import os
import time


class CodingChallenge():
    def display_menu(self):
        # This is the main display menu
        # clears out the screen everytime method is called
        os.system('cls||clear')
        print("")
        print(30 * " ", "Welcome to Mobile Ticket viewer", 30 * " ")
        print("Please select an option from below:\n")
        print("1. List all the tickets ")
        print("2. List a single ticket ")
        print("Quit (Enter q or Q to Quit ) \n")

    def menu(self):
        # clears out the screen everytime method menu is called
        os.system('cls||clear')

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                # clears out the screen everytime method is called
                os.system('cls||clear')

                # calls get_all_tickets from tickets.py file
                tickets.get_all_tickets()

            elif choice == "2":
                # clears out the screen everytime method is called
                os.system('cls||clear')

                # calls get_ticket from tickets.py file
                tickets.get_ticket()

            elif choice == "q" or choice == "Q":
                print("\nThanks for visiting. :)\n")
                break

            else:
                print(
                    """\nInvalid selection!!!! please enter number 1, 2 or enter q or Q to Quit""")
                time.sleep(3)
                # clears out the screen everytime method is called
                os.system('cls||clear')


if __name__ == '__main__':
    tickets = Ticket()
    a = CodingChallenge()
    a.menu()
