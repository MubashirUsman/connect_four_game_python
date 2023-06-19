#   Mubashir Usman Ijaz
# This function is defined to provide the functionality of
# getting the user input from one of the keys used in the game.

def game_options():
    print("""
Press Q to Quit
Press R to Restart
Enter column number from 1-5 to drop the token
""")
    while True:
        entry = input()
        if entry in ("q", "Q", "R", "r", "1", "2", "3", "4", "5"):
            return entry
        else:
            print("Please choose one of the key bindings")

