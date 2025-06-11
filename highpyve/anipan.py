import os

# Constants for cat menu choices
class CatMenuOptions:
    EXIT = 0
    DETAILS = 1
    HOBBIES = 2
    SIBLINGS = 3
    FAVORITE_FOOD = 4
    FRIENDS = 5

def clear_screen():
    os.system('cls')

def buffer():
    input("\nPress enter to continue...")
    clear_screen()

class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def display_cat_details(self):
        clear_screen()
        print(f"Hello! My name is {self.name}!")
        print(f"I am {self.age} years old, and my breed is {self.breed}!")
        buffer()

    def display_cat_hobbies(self):
        clear_screen()
        print(f"My hobbies are: \n")
        print(f"[1] - Sleeping on the couch.")
        print(f"[2] - Scratching my owner's tires.")
        print(f"[3] - Jumping through our window.")
        print(f"[4] - Cuddling with my owner.")
        buffer()

    def display_cat_siblings(self):
        clear_screen()
        print("I have siblings named Snow and Una. They are also Puspins!")
        buffer()

    def display_cat_favorite_food(self):
        clear_screen()
        print("My favorite food is tuna, but it really depends on my mood.")
        buffer()

    def display_cat_friends(self):
        clear_screen()
        print("I also have dog friends! They are Whiskey, Bella, and Happy!")
        buffer()

    def menu(self):
        while True:
            clear_screen()
            print(f"Welcome to {self.name}'s Menu! \n")
            print(f"[{CatMenuOptions.DETAILS}] - {self.name}'s Details")
            print(f"[{CatMenuOptions.HOBBIES}] - {self.name}'s Hobbies")
            print(f"[{CatMenuOptions.SIBLINGS}] - {self.name}'s Siblings")
            print(f"[{CatMenuOptions.FAVORITE_FOOD}] - "
                  f"{self.name}'s Favorite Food")
            print(f"[{CatMenuOptions.FRIENDS}] - {self.name}'s Dog Friends")
            print(f"[{CatMenuOptions.EXIT}] - Exit")

            choice = input("\nEnter your choice: ")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid option. Please enter a number.")
                buffer()
                continue
            
            # Exit loop if user selects 0
            if choice == CatMenuOptions.EXIT:
                clear_screen()
                print("Thank you. Goodbye!")
                break

            match choice:
                case CatMenuOptions.DETAILS:
                    self.display_cat_details()
                case CatMenuOptions.HOBBIES:
                    self.display_cat_hobbies()
                case CatMenuOptions.SIBLINGS:
                    self.display_cat_siblings()
                case CatMenuOptions.FAVORITE_FOOD:
                    self.display_cat_favorite_food()
                case CatMenuOptions.FRIENDS:
                    self.display_cat_friends()
                case _:
                    print("Invalid option. Please select from 1 to 5.")
                    buffer()
