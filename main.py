import os
from highpyve.anipan import Cat
from highpyve.tolentino import Person
from highpyve.ocariza import BeautyProfile
from highpyve.bartolome import FavoriteMusicalLyrics

# Constants for menu choices
class MenuOptions:
    EXIT = 0
    ANIPAN = 1
    TOLENTINO = 2
    BARTOLOME = 3
    OCARIZA = 4

def clear_screen():
    os.system('cls')

def buffer():
    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print("==========================================")
        print("          Welcome to HighPyve!         ")
        print("==========================================")
        print("Select a developer module to continue:\n")
        print(f"[{MenuOptions.ANIPAN}] Kristoffer Anipan")
        print(f"[{MenuOptions.TOLENTINO}] Ma. Rose Tolentino")
        print(f"[{MenuOptions.BARTOLOME}] Mikaela Joy Bartolome")
        print(f"[{MenuOptions.OCARIZA}] Jaira Isabel Ocariza")
        print(f"[{MenuOptions.EXIT}] Exit\n")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.")
            buffer()
            continue

        # Exit loop if user selects 0    
        if user_choice == MenuOptions.EXIT:
            clear_screen()
            print("Thank you for using HighPyve Main Menu! Exiting...")
            break

        match user_choice:
            case MenuOptions.ANIPAN:
                my_cat = Cat("Gracia", 8, "Puspin")
                my_cat.menu()
            case MenuOptions.TOLENTINO:
                my_profile = Person("Rose", 20, "Purple", 
                            "South Signal Taguig City", "July 15, 2004")
                my_profile.menu()
            case MenuOptions.BARTOLOME:
                favorite_musical = FavoriteMusicalLyrics()
                favorite_musical.menu()
            case MenuOptions.OCARIZA:
                profile = BeautyProfile("Jaira", "Normal", "Sunscreen")
                profile.menu()
            case _:
                print("\nInvalid choice! Please select a number from 1 to 4.")
                buffer()

main()