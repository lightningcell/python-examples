# Author: Hamit Şimşek
# GitHub: @lightningcell
# Description: This file contains the main flow of the game.
#              It is the only file that you need to run for play the game.
#              It is easy to add new features to the game.
#              Because, you will not change the other files.
#              You will just add new files and import them here and configure the flow.
#              It's called 'Modular Programming' baby !


from menus import *


def flow():
    WELCOME_MESSAGE = "Welcome to the guessing game."
    print(WELCOME_MESSAGE)

    while True:
        # SHOW MAIN MENU
        action = main_menu()

        if action == 1:
            game()

        elif action == 2:
            display_best_score()

        elif action == 3:
            display_settings()

        elif action == 4:
            configure_settings()

        elif action == 5:
            break


if __name__ == '__main__':
    flow()
