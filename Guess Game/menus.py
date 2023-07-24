# Author: Hamit Şimşek
# GitHub: @lightningcell
# Description:  This file contains game menus. Each function represents a menu.
#               Some menus have while loop inside.
#               It provides a comfortable transition between menus.
#               And it is easy to add new menus.
#               Because the only thing you need to do is to add a new function.
#               You can see the usage of this script in guess_game\run.py


from utils import *
import random


def game():
    # ADJUST THE GAME PROPERTIES
    _min = get_game_data()["MIN_VALUE"]
    _max = get_game_data()["MAX_VALUE"]
    number = random.randint(_min, _max)
    # print(number)  # You can uncomment this line for testing purposes.
    max_total_guess = (_max - _min + 1) // 2
    base_point = (_max - _min) * 100
    all_guesses = set()

    total_guess = get_int("How many guesses would you like ? ", specific_range=range(1, max_total_guess))
    remaining_guess = total_guess


    # START THE GAME
    while remaining_guess > 0:
        # TAKE THE GUESS
        guess = get_int("Please, enter your guess -> ", specific_range=range(_min, _max + 1), show_specific_range=True)

        if guess in all_guesses:
            print(f"You've already made that guess ! -> {guess}")
            continue

        if guess == number:
            # CALCULATE THE SCORE
            if remaining_guess != total_guess:
                score = str(int(base_point * remaining_guess / (total_guess ** 2)))
            else:
                score = str(base_point)

            print(f"CONGRATS ! THE NUMBER IS {number}")
            print(f"Score: {score}")
            best_score = get_game_data()["BEST_SCORE"]

            if best_score < score:
                set_game_data(BEST_SCORE=score)

            break

        else:
            remaining_guess -= 1
            all_guesses.add(guess)
            print(f"{guess} is wrong number. ")

def display_best_score():
    print(f"            THE BEST SCORE IS: {get_game_data()['BEST_SCORE']}")

def display_settings():
    data = get_game_data()
    print(f"""SETTINGS:
            MINIMUM NUMBER: {data['MIN_VALUE']}
            MAXIMUM NUMBER: {data['MAX_VALUE']}""")

def configure_settings():
    while True:
        data = get_game_data()
        print(f"""For previous menu, enter 3...
            [1] MINIMUM NUMBER: {data['MIN_VALUE']}
            [2] MAXIMUM NUMBER: {data['MAX_VALUE']}""")

        _act = get_int("Please choose the settings that you wanna change -> ", range(1, 4))

        if _act == 1:
            # MINIMUM NUMBER OPTION
            new_min_value = get_int("Enter new min value: ")
            if data["MAX_VALUE"] <= new_min_value:
                print(f"The minimum value cannot be higher than the maximum value!")
                continue
            else:
                set_game_data(MIN_VALUE=new_min_value)

        elif _act == 2:
            # MAXIMUM NUMBER OPTION
            new_max_value = get_int("Enter new max value: ")
            if data["MIN_VALUE"] >= new_max_value:
                print(f"The maximum value cannot be less than the minimum value!")
            else:
                set_game_data(MAX_VALUE=new_max_value)
        else:
            break


def main_menu():
    MENU = """What do you want to do ?
    1 - PLAY
    2 - SHOW BEST SCORE
    3 - SHOW SETTINGS
    4 - CONFIGURE SETTINGS
    5 - EXIT"""

    print("\n" + MENU)
    action = get_int("Choose action (1 / 2 / 3 / 4 / 5): ", specific_range=range(1, 6), show_specific_range=False)
    print("\n")

    return action
