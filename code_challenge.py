# This is the main code to the code challenge
import os


class CodingChallenge():
    def display_menu(self):
        # clears out the screen everytime method display_menu is called
        os.system('cls||clear')

        print(30 * "-", "Welcome to Mobile Ticket viewer", 30 * "-")
        print("Please select an option from below:\n")
        print("1. List all the tickets ")
        print("2. List a single ticket ")
        print("Quit (Enter q or Q to Quit ) ")


def main():
    a = CodingChallenge()
    a.display_menu()

if __name__ == '__main__':
    main()

