# Author: Hamit Şimşek
# GitHub: @lightningcell
# Description: This file contains some utility functions for the guess game.
#              These functions are not related to the game itself.
#              They are just to make the code cleaner.
#              If you want to see the usage of these functions, check the guess_game\run.py and guess_game\menus.py file.


import json


def get_int(special_msg="Please enter a number: ", specific_range: range = None, show_specific_range=True) -> int:
    """
    Customized input function to get integer type numbers.
    :param special_msg: The message to show user
    :param specific_range: Custom number range
    :param show_specific_range: Adjust the show settings
    :return: Returns integer
    """

    # SET INPUT MESSAGE
    msg = special_msg
    if not (specific_range is None) and show_specific_range:
        msg += f" (Min: {specific_range.start} - Max: {specific_range.stop - 1}) -> "

    num = input(msg)

    if num.isdecimal():
        if specific_range:
            if int(num) not in specific_range:
                print(f"{num} is not in the between {specific_range.start} and {specific_range.stop - 1} (inclusive)")
                return get_int(special_msg, specific_range, show_specific_range)

        return int(num)
    else:
        print(f"{num} is invalid.")
        return get_int(special_msg, specific_range, show_specific_range)


def get_game_data() -> dict:
    with open("gamedata.json", "r") as data_file:
        return json.loads(data_file.read())


def set_game_data(**kwargs) -> dict:
    data = get_game_data()
    for key in kwargs:
        data[key] = kwargs[key]

    with open("gamedata.json", "w") as data_file:
        data_file.write(json.dumps(data))

    return data
