import random

def make_name():
    choose_firstname = ['Uter', 'Yalley', ' Hundrex', 'Skeevol', 'Lyla', 'Ransori']
    choose_surname = ['Pearl', 'Hanor', 'Lysand', 'Precisol', 'Koler', 'Lar']
    rand_surname = random.choice(choose_surname)
    rand_first_name = random.choice(choose_firstname)
    rand_name = rand_first_name, rand_surname
    print(rand_name)
def random_type():
    type = ['Human', 'Korle', 'Retiara', 'Halpoe']
    rand_type = random.choice(type)
    print(rand_type)
def random_homeland():
    pick_homeland = ["Libyo", "Junla", "Castrol", "Carilona"]
    rand_homeland = random.choice(pick_homeland)
    print(rand_homeland)
def rand_npc():
    make_name()
    random_type()
    random_homeland()
def speech():
        speech_options = ["'Oh, I don't like you.'", "'What in the name of Carilona do you want?'", "'Just leave me alone.'", "'Go away.'", "Good day to you.", "Is it really the hero of all Anlax?", "It's really good to see you!"]
        speech_choice = random.choice(speech_options)
        print(speech_choice)
rand_npc()
speech()
