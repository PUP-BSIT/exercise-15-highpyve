import os
import random

# Constants for menu choices
class MenuOption:
    EXIT_OPTION = 0
    NAME = 1
    AGE = 2
    COLOR = 3
    ADDRESS = 4
    BIRTHDAY = 5
    PERSON_SUMMARY = 6
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()

def random_motivation():
    quotes = [
        "Keep going! You're learning more every second.",
        "Every coder was once a beginner. Stay consistent.",
        "Always choose to be kind :')",
        "Progress, not perfection. One step at a time.",
        "You just learned something new. That's a win!",
        "Great things take time — just like great code.",
        "Never underestimate what you can do with one good idea.",
        "Practice makes progress. Keep at it!",
        "Debugging is like being a detective in your own code."
    ]
    print(f"\nQuote of the Moment:\n→ \"{random.choice(quotes)}\"")

class Person:
    def __init__(self, name, age, color, address, birthday):
        self.name = name
        self.age = age
        self.color = color
        self.address = address
        self.birthday = birthday

    def greet(self):
        clear_screen()
        print("===========================================================")
        print(f"Hello! My name is {self.name}. It's a pleasure to meet you.")
        print("===========================================================")
        random_motivation()
        buffer()

    def show_age(self):
        clear_screen()
        print("===========================================================")
        print(f"I am {self.age} years old.")
        print("===========================================================")
        random_motivation()
        buffer()

    def show_favorite_color(self):
        clear_screen()
        print("===========================================================")
        print(f"My favorite color is {self.color}.")
        print("===========================================================")
        random_motivation()
        buffer()

    def show_address(self):
        clear_screen()
        print("===========================================================")
        print(f"I currently live in {self.address}.")
        print("===========================================================")
        random_motivation()
        buffer()

    def show_birthday(self):
        clear_screen()
        print("===========================================================")
        print(f"I was born on {self.birthday}.")
        print("===========================================================")
        random_motivation()
        buffer()

    def display_summary(self):
        clear_screen()
        print("\n----- PERSONAL PROFILE SUMMARY -----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Favorite Color: {self.color}")
        print(f"Address: {self.address}")
        print(f"Birthday: {self.birthday}")
        print("------------------------------------")
        buffer()

    def display_menu(self):
        while True:
            clear_screen()
            print("=======================================================")
            print("             Welcome to Tolentino's Main Menu")
            print("               Get to know me better!")
            print("=======================================================")
            print("[1] - View My Name")
            print("[2] - View My Age")
            print("[3] - View My Favorite Color")
            print("[4] - View My Address")
            print("[5] - View My Birthday")
            print("[6] - View My Profile Summary")
            print("[0] - Back to HighPyve Main Menu")
            print("=======================================================")

            user_input = input("\nSelect an option: ").strip()

            try:
                choice = int(user_input)
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                buffer()
                continue
            
            # Exit loop if user selects 0
            if choice == MenuOption.EXIT_OPTION:
                print("\nThat was fun! I hope you got to know me better. "
                      "See you next time from Tolentino's menu!")
                buffer()
                return MenuOption.EXIT_OPTION
            
            if 1 <= choice <= 6:
                return choice
            else:
                print("\nInvalid option. Please enter a number from 0 to 6.")
                buffer()
        
    def process_choice(self, user_choice):
        match user_choice:
            case MenuOption.NAME:
                self.greet()
            case MenuOption.AGE:
                self.show_age()
            case MenuOption.COLOR:
                self.show_favorite_color()
            case MenuOption.ADDRESS:
                self.show_address()
            case MenuOption.BIRTHDAY:
                self.show_birthday()
            case MenuOption.PERSON_SUMMARY:
                self.display_summary()

    def menu(self):
        clear_screen()
        user_choice = None
        while user_choice != MenuOption.EXIT_OPTION:
            user_choice = self.display_menu()
            self.process_choice(user_choice)