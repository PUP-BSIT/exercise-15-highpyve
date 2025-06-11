import os

EXIT_OPTION = 0

# Constants for skin types
SKIN_TYPE_OILY = "Oily"
SKIN_TYPE_DRY = "Dry"
SKIN_TYPE_COMBINATION = "Combination"
SKIN_TYPE_NORMAL = "Normal"

VALID_SKIN_TYPES = (SKIN_TYPE_OILY, SKIN_TYPE_DRY, SKIN_TYPE_COMBINATION, 
                    SKIN_TYPE_NORMAL)

# Constants for beauty menu options
class MenuOption:
    DESCRIBE_SKIN = 1
    RECOMMEND_ROUTINE = 2
    SHOW_ACTIVITIES = 3
    DISPLAY_SUMMARY = 4
    UPDATE_SKIN_TYPE = 5
    SET_FAV_PRODUCT = 6

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()

class BeautyProfile:
    def __init__(self, name, skin_type, favorite_product):
        self.name = name
        self.skin_type = skin_type
        self.favorite_product = favorite_product

    def describe_skin(self):
        clear_screen()
        print(f"\n{self.name.title()} has {self.skin_type.lower()} skin.")
        buffer()

    def recommend_routine(self):
        clear_screen()
        skin_type = self.skin_type

        if skin_type == SKIN_TYPE_OILY:
            print("Routine for oily skin: \n- Gel cleanser, " 
                  "alcohol-free toner, and oil-free moisturizer")
        elif skin_type == SKIN_TYPE_DRY:
            print("Routine for dry skin: \n- Cream cleanser, hydrating toner,"
                  " and rich moisturizer")
        elif skin_type == SKIN_TYPE_COMBINATION:
            print("Routine for combination skin: \n- Balanced cleanser, "
                  "lightweight moisturizer, and targeted serums")
        elif skin_type == SKIN_TYPE_NORMAL:
            print("Routine for normal skin: \n- Gentle cleanser, " 
                  "light moisturizer, and daily sunscreen")
        buffer()

    def show_self_care_activities(self):
        clear_screen()
        print("\nHere are some self-care activities you might enjoy:")
        print("\n- Taking a relaxing bath"
              "\n- Reading a book"
              "\n- Journaling your thoughts"
              "\n- Listening to calming music"
              "\n- Watching your favorite movie or series"
              "\n- Decluttering or organizing a space")
        buffer()

    def update_skin_type(self):
        clear_screen()
        new_skin_type = input("\nEnter your new skin type (oily, dry, "
                              "combination, or normal): ").strip().title()
        if not new_skin_type:
            print("Invalid input. You didn't enter anything.")
        elif new_skin_type not in VALID_SKIN_TYPES:
            print("Invalid skin type. Choose from oily, dry, "
                  "combination, or normal.")
        else:
            self.skin_type = new_skin_type
            print(f"Skin type updated to: {self.skin_type}")
        buffer()

    def set_new_favorite_product(self):
        clear_screen()
        new_product = input("\nEnter new favorite beauty product: ").strip()
        if not new_product:
            print("Invalid input. You didn't enter anything.")
        else:
            self.favorite_product = new_product.title()
            print(f"New favorite product set to: {self.favorite_product}")
        buffer()

    def display_summary(self):
        clear_screen()
        print("\n+----- BEAUTY PROFILE SUMMARY -----+")
        print(f"Name: {self.name.title()}")
        print(f"Skin Type: {self.skin_type}")
        print(f"Favorite Product: {self.favorite_product.title()}")
        print("+----------------------------------+")
        buffer()

    def display_menu(self):
        while True:
            print("\n" + "+" + "-"*38 + "+")
            print("|{:^38}|".format(" BEAUTY MENU "))
            print("+" + "-"*38 + "+")
            print("| 1 | Describe Skin                    |")
            print("| 2 | Recommend Routine                |")
            print("| 3 | Self-Care Activities             |")
            print("| 4 | Beauty Profile Summary           |")
            print("| 5 | Update Skin Type                 |")
            print("| 6 | Set Favorite Product             |")
            print("| 0 | Back to Main Menu                |")
            print("+" + "-"*38 + "+")
            
            user_input = input("\nSelect an option: ").strip()

            try:
                choice = int(user_input)
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                buffer()
                continue
            
            # Exit loop if user selects 0
            if choice == EXIT_OPTION:
                print(f"\nExiting {self.name.title()}'s Beauty Menu. "
                      "See you soon!")
                buffer()
                return EXIT_OPTION
            
            if (MenuOption.DESCRIBE_SKIN <= choice 
                    <= MenuOption.SET_FAV_PRODUCT):
                return choice
            else:
                print("\nInvalid option. Please enter a number from 0 to 6.")
                buffer()

    def process_choice(self, user_choice):
        match user_choice:
            case MenuOption.DESCRIBE_SKIN:
                self.describe_skin()
            case MenuOption.RECOMMEND_ROUTINE:
                self.recommend_routine()
            case MenuOption.SHOW_ACTIVITIES:
                self.show_self_care_activities()
            case MenuOption.DISPLAY_SUMMARY:
                self.display_summary()
            case MenuOption.UPDATE_SKIN_TYPE:
                self.update_skin_type()
            case MenuOption.SET_FAV_PRODUCT:
                self.set_new_favorite_product()

    def menu(self):
        clear_screen()
        user_choice = None
        while user_choice != EXIT_OPTION:
            user_choice = self.display_menu()
            self.process_choice(user_choice)
