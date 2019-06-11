#!/usr/bin/env python3

# install pip3 install requests


from tickets import Ticket
import os
import time


# This is the main code to the code challenge
# Contains:
class CodingChallenge():
    def display_menu(self):
        # This is the main display menu
        # clears out the screen everytime method is called
        os.system('clear')
        print("")
        print(30 * " ", "Welcome to Mobile Ticket viewer", 30 * " ")
        print("Please select an option from below:\n")
        print("1. List all the tickets ")
        print("2. List a single ticket ")
        print("Quit (Enter q or Q to Quit ) \n")

    def menu(self):
        # clears out the screen everytime method menu is called
        os.system('clear')

        while True:
            # displays the main menu in the console
            self.display_menu()
            choice = input("Enter your choice(1,2,3 or q/Q): ")
            if choice == "1":
                os.system('clear')

                # calls get_all_tickets from tickets.py file to receive all tickets
                tickets.get_all_tickets()

            elif choice == "2":
                os.system('clear')

                # calls get_ticket from tickets.py file to get a single ticket
                tickets.get_ticket()

            elif choice == "q" or choice == "Q":
                print("\nThanks for visiting. :)\n")
                # Quits the main console-based menu
                break

            else:
                print(
                    """\nInvalid selection!!!! please enter number 1, 2 or enter q or Q to Quit""")
                time.sleep(3)
                os.system('clear')


if __name__ == '__main__':
    tickets = Ticket()
    a = CodingChallenge()
    a.menu()
