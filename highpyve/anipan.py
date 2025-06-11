import os

EXIT_OPTION = 0
UNSET_OPTION = ""

# Constants for cat menu options
class CatMenuOption:
    DETAILS = 1
    HOBBIES = 2
    SIBLINGS = 3
    FAVORITE_FOOD = 4
    FRIENDS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()

class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def display_details(self):
        clear_screen()
        print(f"Hello! My name is {self.name}!")
        print(f"I am {self.age} years old, and my breed is {self.breed}!")
        buffer()

    def display_hobbies(self):
        clear_screen()
        print("My hobbies are: \n")
        print("- Sleeping on the couch")
        print("- Scratching my owner's tires")
        print("- Jumping through our window")
        print("- Cuddling with my owner")
        buffer()

    def display_siblings(self):
        clear_screen()
        print("I have siblings named Snow and Una. They are also Puspins!")
        buffer()

    def display_favorite_food(self):
        clear_screen()
        print("My favorite food is tuna, but it really depends on my mood.")
        buffer()

    def display_friends(self):
        clear_screen()
        print("I also have dog friends! They are Whiskey, Bella, and Happy!")
        buffer()

    def display_menu(self):
        while True:
            print(f"\n{self.name}'s Menu:")
            print(f"[{CatMenuOption.DETAILS}] - {self.name}'s Details")
            print(f"[{CatMenuOption.HOBBIES}] - {self.name}'s Hobbies")
            print(f"[{CatMenuOption.SIBLINGS}] - {self.name}'s Siblings")
            print(f"[{CatMenuOption.FAVORITE_FOOD}] - "
                  f"{self.name}'s Favorite Food")
            print(f"[{CatMenuOption.FRIENDS}] - {self.name}'s Dog Friends")
            print(f"[{EXIT_OPTION}] - Exit")
            
            user_input = input("\nEnter your choice: ").strip()

            try:
                choice = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")
                buffer()
                continue
            
            # Exit loop if user selects 0
            if choice == EXIT_OPTION:
                print(f"\nExiting {self.name}'s Menu. Goodbye!")
                buffer()
                return EXIT_OPTION
            
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid option. Please enter a number from 0 to 5.")
                buffer()

    def process_choice(self, user_choice):
        match user_choice:
            case CatMenuOption.DETAILS:
                self.display_details()
            case CatMenuOption.HOBBIES:
                self.display_hobbies()
            case CatMenuOption.SIBLINGS:
                self.display_siblings()
            case CatMenuOption.FAVORITE_FOOD:
                self.display_favorite_food()
            case CatMenuOption.FRIENDS:
                self.display_friends()

    def menu(self):
        clear_screen()
        user_choice = UNSET_OPTION
        while user_choice != EXIT_OPTION:
            user_choice = self.display_menu()
            self.process_choice(user_choice)