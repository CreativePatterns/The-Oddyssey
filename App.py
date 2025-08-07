import Generator
from Generator import mood_map

""" Type a mood and get a randomly generated character!!! """
keys = []

# The app starts here
def start_app():

    # show available options
    for key in mood_map.keys():
        keys.append(key)
    print(keys)
    mood = input("Type a mood to generate a character: ")

    if mood not in Generator.mood_map:
        print("Invalid mood")
        exit()

    print(Generator.MODES)
    mode = input("Please choose a mode: ")
    mode = mode.capitalize()

    if mode not in Generator.MODES:
        print("Please choose a valid mode")
        exit()

    Generator.make_character(mood, mode)


start_app()

# I want the user to be able to toggle between 2 different modes (single and dual characters)