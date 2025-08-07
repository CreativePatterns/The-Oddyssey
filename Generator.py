from json import load
import random

OUTPUT_FILE = "npc_card.txt"
MODES = ["Single" , "Duo"]

names = load(open('data_bank/names.json'))
classes = load(open('data_bank/classes.json'))
realms = load(open('data_bank/realms.json'))
traits = load(open('data_bank/traits.json'))
mood_map = load(open('data_bank/mood map.json'))
backstory = load(open('data_bank/backstory.json'))
action = load(open('data_bank/action.json'))
event = load(open('data_bank/event.json'))
duo_backstory = load(open('data_bank/duo_backstory.json'))
side_quest = load(open('data_bank/side_quest.json'))
quest_info = load(open('data_bank/quest_info.json'))

weird_location = random.choice(quest_info['weird_locations'])
weird_objects = random.choice(quest_info['weird_objects'])
faction =  random.choice(quest_info['factions'])


def make_character(mood, mode):

    # Check which mode the user chose!
    if mode == MODES[0]:
        generate_single_character(mood, mode)
    if mode == MODES[1]:
        generate_duo_character(mood, mode)

def generate_single_character(mood, mode):
    character_name = random.choice(names)
    character_work = random.choice(classes)
    character_realm = random.choice(realms)
    character_trait = random.choice(traits)
    character_event = random.choice(event)
    character_action = random.choice(action)
    character_backstory = random.choice(backstory[mood])
    character_side_quest = random.choice(side_quest[mood])
    char_mood = random.choice(mood_map[mood])

    generate_backstory(character_backstory, character_name, character_realm, character_work
                       , character_trait, character_event, character_action, mode , character_side_quest, char_mood)

def generate_duo_character(mood, mode):
    first_char = random.choice(names)
    second_char = random.choice(names)
    first_mood = random.choice(mood_map[mood])
    second_mood = random.choice(mood_map[mood])

    character_side_quest = random.choice(side_quest[mood])

    # make sure there aren't any duplicate characters or moods
    while first_char == second_char:
        second_char = random.choice(names)

    while first_mood == second_mood:
        second_mood = random.choice(mood_map[mood])

    character_realm = random.choice(realms)
    character_event = random.choice(event)
    character_action = random.choice(action)
    chosen_duo_backstory = random.choice(duo_backstory[mood])

    generate_duo_backstory(first_char, second_char, chosen_duo_backstory,
                           character_event, character_action, character_realm, mode, character_side_quest, first_mood, second_mood)


def generate_backstory(character_backstory, character_name, character_realm,
                       character_work, character_trait,character_event, character_action, mode, character_side_quest, char_mood):

    finished_character_backstory = character_backstory.format(name=character_name, event=character_event,
                                                              realm=character_realm, action=character_action)


    finished_side_quest = character_side_quest.format(object=weird_objects, weird_location=weird_location, faction=faction)
    character_sheet = {
        "name": character_name,
        "mood": char_mood,
        "event": event,
        "action": action,
        "character_work": character_work,
        "character_trait": character_trait,
        "character_backstory": finished_character_backstory,
        "character_realm": character_realm,
        "side_quest": finished_side_quest,
    }
    output_and_save_character(character_sheet, OUTPUT_FILE, mode)


def generate_duo_backstory(first_char, second_char, chosen_duo_backstory,
                           character_event, character_action, character_realm, mode, character_side_quest, first_mood, second_mood):

    finished_duo_backstory = chosen_duo_backstory.format(name1=first_char,name2=second_char, event=character_event,
                                                              realm=character_realm, action=character_action)

    finished_side_quest = character_side_quest.format(object=weird_objects, weird_location=weird_location, faction=faction)

    character_sheet = {
        "Name1": first_char,
        "Mood1": first_mood,
        "Name2": second_char,
        "Mood2": second_mood,
        "Duo Backstory": finished_duo_backstory,
        "side_quest": finished_side_quest,
    }
    output_and_save_character(character_sheet, OUTPUT_FILE, mode)


def output_and_save_character(character, file_name, mode):

    if mode == "Single":
        # Print full character
        print(f"\n🧙 Name: {character['name']}")
        print(f" They feel: {character['mood']}")
        print(f"💼 Class: {character['character_work']}")
        print(f"📍 Realm: {character['character_realm']}")
        print(f"🧠 Trait: {character['character_trait']}")
        print(f"📜 Backstory:\n{character['character_backstory']}\n")
        print(f"Side Quest:\n{character['side_quest']}")

        with open(file_name, "w", encoding="utf-8") as f:
            # Print full character
            f.write(f"\n🧙 Name: {character['name']}\n")
            f.write(f"They feel: {character['mood']}\n")
            f.write(f"💼 Class: {character['character_work']}\n")
            f.write(f"📍 Realm: {character['character_realm']}\n")
            f.write(f"🧠 Trait: {character['character_trait']}\n")
            f.write(f"📜 Backstory:\n{character['character_backstory']}\n")
            f.write(f"Side Quest:\n{character['side_quest']}")

    elif mode == "Duo":
        print(f"🧙 Name: {character["Name1"]}")
        print(f" They feel: {character['Mood1']}")
        print(f"🧙 Name: {character["Name2"]}")
        print(f" They feel: {character['Mood2']}")
        print(f"📜 Backstory:\n{character['Duo Backstory']}\n")
        print(f"Side Quest:\n{character['side_quest']}")

        with open(file_name, "w", encoding="utf-8") as f:
            # Print full character
            f.write(f"🧙 Name: {character["Name1"]}\n")
            f.write(f"They feel: {character['Mood1']}\n")
            f.write(f"🧙 Name: {character["Name2"]}\n")
            f.write(f"They feel: {character['Mood2']}\n")
            f.write(f"📜 Backstory:\n{character["Duo Backstory"]}\n")
            f.write(f"Side Quest:\n{character['side_quest']}")
