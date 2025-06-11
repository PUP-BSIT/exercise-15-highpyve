import os

#Constant for Main Menu
class MusicalMenuOptions:
    WICKED = 1
    HAMILTON = 2
    EPIC = 3
    EXIT = 0

#Constant for Titles
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
            ('"The line between naïveté and hopefulness is almost invisible" '
             '— Ruthlessness, Poseidon'),
            ('"You\'re the worst kind of good \'cause you\'re '
            'not even great" '
             '— Ruthlessness, Poseidon') 
        ]
    }

    def __init__(self):
        self.favorite_musical_lyrics = self.MUSICAL_LYRICS

    def display_lyrics(self, musical):
        clear_screen()
        lyrics = self.favorite_musical_lyrics.get(musical)
        if lyrics:
            print(f"{musical} Lyrics:\n")
            for index, lyric in enumerate(lyrics, 1):
                print(f'{index}. {lyric}')
        buffer()

    def display_menu(self):
        clear_screen()
        print("******************************************")
        print("\tMika's Favorite Musical")
        print("\t  Lyrics Compilation")
        print("******************************************")
        print(f"[{MusicalMenuOptions.WICKED}] - Wicked by Jon M. Chu")
        print(f"[{MusicalMenuOptions.HAMILTON}] - Hamilton by Thomas Kail")
        print(f"[{MusicalMenuOptions.EPIC}] - Epic by Jorge Rivera-Herrans")
        print(f"[{MusicalMenuOptions.EXIT}] - Exit")
        print("******************************************")

    def menu(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                buffer()
                continue

            match choice:
                case MusicalMenuOptions.WICKED:
                    self.display_lyrics(MusicalTitles.WICKED)
                case MusicalMenuOptions.HAMILTON:
                    self.display_lyrics(MusicalTitles.HAMILTON)
                case MusicalMenuOptions.EPIC:
                    self.display_lyrics(MusicalTitles.EPIC)
                case MusicalMenuOptions.EXIT:
                    clear_screen()
                    print("Thank you for visiting Mika's Module")
                    buffer()
                    break
                case _:
                    print("Invalid option. Please pick a number from 0-3.")
                    buffer()