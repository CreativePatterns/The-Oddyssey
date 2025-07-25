from json import load
import random

OUTPUT_FILE = "npc_card.txt"

names = load(open('names.json'))
classes = load(open('classes.json'))
realms = load(open('realms.json'))
traits = load(open('traits.json'))
mood_map = load(open('mood map.json'))
backstory = load(open('backstory.json'))


def make_character(mood):
    check_user_mood(mood)

def check_user_mood(mood):
    # Make sure only the moods in the mood map are entered
    if mood not in mood_map:
        print("Mood not found")
        exit()
    generate_random_story(mood)


def generate_random_story(mood):
    character_name = random.choice(names)
    character_work = random.choice(classes)
    character_realm = random.choice(realms)
    character_trait = random.choice(traits)
    character_backstory = random.choice(backstory[mood])
    char_mood = random.choice(mood_map[mood])

    # TODO
    # add event and action later, make the things that you have usable
    generate_backstory(character_backstory, character_name, character_realm, character_work, character_trait)


def generate_backstory(character_backstory, character_name, character_realm, character_work, character_trait,
                       event="Judgement day", action="mopping the floor"):

    finished_character_backstory = character_backstory.format(name=character_name, event=event,
                                                              realm=character_realm, action=action)

    final_character = {
        "name": character_name,
        "event": event,
        "action": action,
        "character_work": character_work,
        "character_trait": character_trait,
        "character_backstory": finished_character_backstory,
        "character_realm": character_realm,
    }

    output_and_save_character(final_character, OUTPUT_FILE)



def output_and_save_character(character, file_name):
    # Print full character
    print(f"\n🧙 Name: {character['name']}")
    print(f"💼 Class: {character['character_work']}")
    print(f"📍 Realm: {character['character_realm']}")
    print(f"🧠 Trait: {character['character_trait']}")
    print(f"📜 Backstory:\n{character['character_backstory']}")

    with open(file_name, "w", encoding="utf-8") as f:
        # Print full character
        f.write(f"\n🧙 Name: {character['name']}\n")
        f.write(f"💼 Class: {character['character_work']}\n")
        f.write(f"📍 Realm: {character['character_realm']}\n")
        f.write(f"🧠 Trait: {character['character_trait']}\n")
        f.write(f"📜 Backstory:\n{character['character_backstory']}\n")