import os

EXIT_OPTION = 0

# Constant for Main Menu
class MenuOptions:
    WICKED = 1
    HAMILTON = 2
    EPIC = 3
    CHARACTERS = 4
    RATINGS = 5
    EXIT = 0

# Constant for Titles
class MusicalTitles:
    WICKED = "Wicked"
    HAMILTON = "Hamilton"
    EPIC = "Epic: The Musical"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()

class FavoriteMusicalLyrics:
    #Disctionary of Mikaela's favorite lyrics
    MUSICAL_LYRICS = {
        MusicalTitles.WICKED: [
            ('"Are people born wicked? Or do they have wickedness '
             'thrust upon them?" '
             '— No One Mourns the Wicked, Ariana Grande'),
            ('"Life\'s more painless, for the brainless" '
             '— Dancing Through Life, Jonathan Bailey'),
            ('"Everyone deserves the chance to fly" '
             '— A Sentimental Man, Jeff Goldblum'),
            ('"Like a comet pulled for orbit, as it passes the sun" '
             '— For Good, Kristin Chenoweth'),
            ('"No good deed goes unpunished, no act of charity '
             'goes unresented" '
             '— No Good Deed, Idina Menzel')
        ],
        MusicalTitles.HAMILTON: [
            ('"Death doesn\'t discriminate, between the sinners '
             'and the saints"  '
             '— Wait for It, Leslie Odom Jr.'),
            ('"You have no control, who lives, who dies, '
             'who tells your story"  '
             '— History Has Its Eyes On You, Christopher Jackson'),
            ('"What is a legacy? It\'s planting seeds in a '
             'garden you never get to see" '
             '— The World Was Wide Enough, Lin-Manuel Miranda'),
            ('"A civic lesson from a slaver, hey neighbor. '
             'Your debts are paid \'cause you don\'t pay labour" '
             '— Cabinet Battle #1, Lin-Manuel Miranda'),
            ('"There are moments when you\'re in so deep. '
            'It seems easier to just swim down" '
             '— It\'s Quiet Uptown, Phillipa Soo')
        ],
        MusicalTitles.EPIC: [
            ('"I will fall in love in love with you over and over again" '
             '— Would You Fall in Love With Me Again?, Penelope'),
            ('"This life is amazing when you greet it with open arms" '
             '— Open Arms, Polites'),
            ('"I have no respect for bullies, those who impose their will" '
             '— Warrior of the Mind, Athena'),
            ('"The line between naïveté and hopefulness is '
            'almost invisible" '
             '— Ruthlessness, Poseidon'),
            ('"You\'re the worst kind of good \'cause you\'re '
            'not even great" '
             '— Ruthlessness, Poseidon') 
        ]
    }

    #Disctionary of the characters in the 3 Musicals
    MAIN_CHARACTERS = {
        MusicalTitles.WICKED: [
            "Cynthia Erivo & Idina Menzel as Elphaba",
            "Ariana Grande & Kristin Chenoweth as Glinda",
            "Jonathan Bailey as Fiyero",
            "Jeff Goldblum as The Wizard",
            "Michelle Yeoh as Madame Morrible",
        ],
        MusicalTitles.HAMILTON: [
            "Lin-Manuel Miranda as Alexander Hamilton",
            "Leslie Odom Jr. as Aaron Burr",
            "Phillipa Soo as Eliza Schuyler",
            "Renée Elise Goldsberry as Angelica Schuyler",
            "Christopher Jackson as George Washington",
        ],
        MusicalTitles.EPIC: [
            "Jorge Rivera-Herrans as Odysseus",
            "Teagan Earley as Athena",
            "Steven Rodriguez as Poseidon",
            "Anna Lea Casey as Penelope",
            "Steven Dookie as Polites",
            "Barbara Wangui as Calypso",
        ]
    }

    #Disctionary of personal ratings of the 3 Musicals
    MUSICAL_RATINGS = {
        MusicalTitles.WICKED: [
            ("First musical I watched in Cinema. I can't wait "
            "for the Wicked: For Good — 5/5⭐"),
        ],
        MusicalTitles.HAMILTON: [
            ("I've learned a lot of about American History. I wish"
            " there are more musicals about History— 5/5⭐"),
        ],
        MusicalTitles.EPIC: [
            ("Hidden gem! This is for greek mythology lover "
            "like me. — 5/5⭐"),
        ]
    }

    def __init__(self):
        self.favorite_musical_lyrics = self.MUSICAL_LYRICS
        self.characters = self.MAIN_CHARACTERS
        self.personal_ratings = self.MUSICAL_RATINGS

    def display_lyrics(self, musical):
        clear_screen()
        lyrics = self.favorite_musical_lyrics.get(musical)
        if lyrics:
            print(f"{musical} Lyrics:\n")
            for index, lyric in enumerate(lyrics, 1):
                print(f'{index}. {lyric}')
        buffer()

    def display_main_characters(self):
        clear_screen()
        print("Main Characters and their Actors\n")
        for musical, characters in self.characters.items():
            print(f"{musical}:")
            for name in characters:
                print(f"  - {name}")
            print()
        buffer()

    def display_musical_ratings(self):
        clear_screen()
        for musical, ratings in self.personal_ratings.items():
            print(f"{musical}:")
            if ratings:
                for index, rating in enumerate(ratings, 1):
                    print(f"{index}. {rating}\n")
        buffer()  

    def display_menu(self):
        clear_screen()
        while True:
            print("******************************************")
            print("\tMika's Favorite Musical")
            print("    Lyrics, Characters, and Ratings")
            print("******************************************")
            print(f"[{MenuOptions.WICKED}] - Wicked by Jon M. Chu")
            print(f"[{MenuOptions.HAMILTON}] - Hamilton by Thomas Kail")
            print(f"[{MenuOptions.EPIC}] - Epic by Jorge Rivera-Herrans")
            print(f"[{MenuOptions.CHARACTERS}] - Show Musical Characters")
            print(f"[{MenuOptions.RATINGS}] - Show Personal Ratings")
            print(f"[{MenuOptions.EXIT}] - Exit")
            print("******************************************")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                buffer()
                continue

            if choice == MenuOptions.EXIT:
                clear_screen()
                print("Thank you for visiting Mika's Module")
                buffer()
                return MenuOptions.EXIT
            
            if MenuOptions.WICKED <= choice <= MenuOptions.RATINGS:
                return choice
            else:
                print("Invalid option. Please pick a number from 0-5.")
                buffer()           

    def process_choice(self, user_choice):
        match user_choice:
            case MenuOptions.WICKED:
                self.display_lyrics(MusicalTitles.WICKED)
            case MenuOptions.HAMILTON:
                self.display_lyrics(MusicalTitles.HAMILTON)
            case MenuOptions.EPIC:
                self.display_lyrics(MusicalTitles.EPIC)
            case MenuOptions.CHARACTERS:
                self.display_main_characters()
            case MenuOptions.RATINGS:
                self.display_musical_ratings()

    def menu(self):
        user_choice = None
        while user_choice != EXIT_OPTION:
            user_choice = self.display_menu()
            self.process_choice(user_choice)