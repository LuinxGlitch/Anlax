import random
from random import randint
import json
import randnpcmake
from randnpcmake import random_type, make_name, random_homeland, rand_npc, speech

def create_character():
    player_homeland = input("Where do you hail from? Libyo, Junla, Castrol, or Carilona?")
    player_type = input("Are you the law-abiding Humans? Are you the thieving rat species, the Korle? Are you the kind but skilled Retiara? Or are you the big, fearsome mechanical creations the Halpoe?")
    player_name = input("What is ye name?")
    player_class = input("Pick a class - Thief, Warrior, Merchant or mage?")
    print("Your name is", player_name, ", your species is", player_type, ", your homeland is", player_homeland, "and your class is", player_class)
    print("There are four stats: Personality, Robbery, Combat, and Magic. They all start at 40, and depending on what type or class you chose, there will be increases to them.")
    magic = 40
    personality = 40
    robbery = 40
    combat = 40
    if player_type in ["Human", "Humans"]:
        personality = personality * 1.7
    elif player_type == "Korle":
        robbery = robbery * 1.7
    elif player_type == "Retiara":
        magic = magic * 1.7
    elif player_type == "Halpoe":
        combat = combat * 1.7
    if player_class == "Warrior":
        combat = combat * 1.9
    elif player_class == "Mage":
        magic = magic * 1.9
    elif player_class == "Merchant":
        personality = personality * 1.9
    elif player_class == "Thief":
        robbery = robbery * 1.9
    print("You will also have a reputation stat. This affects how people speak to you.")
    reputation = randint(1, 50)
    print("Your starting HP (this can be upgraded) is your combat skill x1.9.")
    hp = combat * 1.9
    print("The starting level is 1.")
    level = 1
    print("Here are your stats and reputation:")
    print("Combat:", combat)
    print("Magic:", magic)
    print("Robbery", robbery)
    print("Personality:", personality)
    print("Reputation", reputation)
    player = {
        "name": player_name,
        "type": player_type,
        "homeland": player_homeland,
        "class": player_class,
        "combat": combat,
        "magic": magic,
        "robbery": robbery,
        "personality": personality,
        "reputation": reputation,
        "hp": hp,
        "inventory": [],
        "level": level,
        "xp": 0,
        "guild": "none",
        "gold": 0
    }
    return player
def reputation_speech(player):
    if player["reputation"] > 25:
        npc_positive_speech = ["Good day to you.", "Is it really the hero of all Anlax?", "It's really good to see you!"]
        npc_rand_pos = random.choice(npc_positive_speech)
        print(npc_rand_pos)
    if player["reputation"] < 25:
        npc_negative_speech = ["'Oh, I don't like you.'", "'What in the name of Carilona do you want?'", "'Just leave me alone.'", "'Go away.'"]
        npc_rand_neg = random.choice(npc_negative_speech)
        print(npc_rand_neg)
    return player
def game_loop(player):
    while True:
        print("ANLAX")
        print("1. View Your Character")
        print("2. Explore Anlax")
        print("3. Dungeon Crawl")
        print("4. Join / Quest with a Guild")
        print("5. Save your character")
        print("6. Exit the game")
        menuchoose = int(input(">"))
        if menuchoose == 1:
            print(player)
        if menuchoose == 2:
            explore(player)
        if menuchoose == 3:
            dungeon(player)
            save_character(player)
            print("AUTOSAVED")
        if menuchoose == 4:
            guildwork(player)
            save_character(player)
            print("AUTOSAVED")
        if menuchoose == 5:
            save_character(player)
            print("SAVED")
        if menuchoose == 6:
            break


def combat(player):
    enemy_hp = 0
    enemy_list = ["archer", "swordsman", "burglar", "troll", "goblin", "dragon"]
    rand_enemy = random.choice(enemy_list)
    if rand_enemy == "archer":
        enemy_hp =  10
    elif rand_enemy == "swordsman":
        enemy_hp = 15
    elif rand_enemy == "burglar":
        enemy_hp = 10
    elif rand_enemy == "troll":
        enemy_hp = 20
    elif rand_enemy == "goblin":
        enemy_hp = 15
    elif rand_enemy == "dragon":
        enemy_hp = 500
    print("\n A rogue", rand_enemy, "appears!")
    while enemy_hp > 0:
        input("Press Enter to attack...")
        attack_chance = randint(1, 2)
        base_damage = randint(6, 12)
        multiplier = player["combat"] / 40 # Base multiplier
        damage = int(base_damage * multiplier)
        if attack_chance == 1:
            print("You swing... and miss!")
        else:
            enemy_hp -= damage
            print(f"You hit the enemy for {damage} damage!")
            player["xp"] += 10
            print("XP:", player["xp"])
            if enemy_hp > 0:
                print(f"Enemy HP: {enemy_hp}")
    return player
def dungeon_loot(player):
    print("HERE IS THE LOOT YOU FOUND.")
    luck = randint(1, 50)
    print("With a luck of", luck, "you found:")
    chest_contents = "nothing"
    if luck > 45:
        chest_contents = "DungeonMaster armor", "DungeonMaster sword"
        player["inventory"].extend(chest_contents)
    elif luck < 45 and luck > 20:
        chest_contents = "fur armor", "basic bow"
        player["inventory"].extend(chest_contents)
    elif luck < 20:
        chest_contents = "scallop", "pork", "wooden sword"
        player["inventory"].extend(chest_contents)
    gold_found = randint(1, 200)
    print("You found:", ", ".join(chest_contents))
    if len(player["inventory"]) >= 2:
        print("You can't carry any more items! Drop something first.")
        print("Inventory full. Drop an item? (1 or 2)")
        drop_choice = input("> ")
        dropped = player["inventory"].pop(int(drop_choice) - 1)
        print(f"You dropped {dropped}.")
    else:
        space_left = 2 - len(player["inventory"])
        items_to_add = chest_contents[:space_left]
        player["inventory"].extend(items_to_add)
        print("Added to inventory:", ", ".join(items_to_add))
    print("You found", gold_found, "gold pieces.")
    player["gold"] = gold_found + player["gold"]
    save_character(player)

def dungeon(player):
    levels(player)
    dungeon_rooms = randint(1, 15)
    dungeon_chests = randint(1, 25)
    print("DUNGEON ROOMS:", dungeon_rooms)
    print("DUNGEON CHESTS:", dungeon_chests)
    player = combat(player)
    dungeon_loot(player)
    print("After", dungeon_rooms, "hours, you leave")
    return player
def levels(player):
    if player["xp"] >= 600:
        player["level"] = 4
    elif player["xp"] >= 400:
        player["level"] = 3
    elif player["xp"] >= 200:
        player["level"] = 2
def save_character(player, filename="character.json"):
    with open(filename, "w") as file:
        json.dump(player, file, indent=4)
def date():
    dayofweeklist = ["Lunae", "Tiwesdaeg", "Mercuri", "Lovis", "Frigedae", "Saturni", "Sol"]
    listmonth = ["Geol", "Caed", "Linear", "Sun-rise", "Neardawn", "Crakenleaf", "Torel", "Juniper", "Holdat", "Reator", "Novan", "Chriscemn"]
    daynumber = randint(1, 30)
    day = random.choice(dayofweeklist)
    month = random.choice(listmonth)
    date = day, daynumber, month, "4th Titan"
    print(date)
def load_character(filename="character.json"):
    with open(filename, "r") as file:
        return json.load(file)
        # Ensure XP and level exist even in older save files
    if "xp" not in player:
        player["xp"] = 0
    if "level" not in player:
        player["level"] = 1
    return player

def main():
    print("=== Welcome to Anlax ===")
    choice = input("Do you want to (N)ew game or (L)oad game? ").lower()

    if choice == "l":
        try:
            player = load_character()
            print(f"Welcome back, {player['name']}!")
        except FileNotFoundError:
            print("No saved game found. Starting new game...")
            player = create_character()
    else:
        player = create_character()  # NOW player exists
    save_character(player)  # Safe to call now
    date()
    levels(player)
    game_loop(player)
def guildwork(player):
    if player["guild"] == "none":
        print("Join the Warrior Faction, the Merchant Republic, the Thieve's Scowl or the Mage's Clan?")
        guild = input(">")
        print("You joined the", guild, "guild. They greet you with open arms.")
        player["guild"] = guild
    else:
        print("There is no work available now.")
def explore(player):
    travelchoice = input("Go to Jarlking, Redyarn, Scaul, Dargr or Fien?")
    if travelchoice == "Redyarn":
        redcitylook = input("Tavern, shop or guild?")
        if redcitylook == "tavern":
            print("This is the Solid Archer. Closed for building works.")
            rand_npc()
            reputation_speech(player)
        if redcitylook == "shop":
            print("The Crow [illegible]. It is open, but heavily damaged by gangs.")
            rand_npc()
            reputation_speech(player)
        if redcitylook == "guild":
            print("There is the Warrior Faction, the Merchant Republic, the Thieve's Scowl and the Mage's Clan.")
            rand_npc()
            reputation_speech(player)
    if travelchoice == "Jarlking":
        print("Tavern, shop or guild?")
        jarlcitylook = input(">")
        if jarlcitylook == "shop":
            print("This is Hundrex's Odd Ends general store. ")
            rand_npc()
            reputation_speech(player)
        if jarlcitylook == "tavern":
            print("This is the Ugly Argon tavern.")
            rand_npc()
            reputation_speech(player)
        if jarlcitylook == "guild":
            print("There is the Warrior Faction, the Merchant Republic, the Thieve's Scowl and the Mage's Clan.")
            rand_npc()
            reputation_speech(player)
    if travelchoice == "Fien":
        print("Go to ye ol' pub, yeh flimseh shops or yar ghoulish guilds, Eh?")
        fiencitylook = input(">")
        if fiencitylook == "tavern":
            print("There is a small stout man. He waves and says 'Hello, hello, come on in to the Goul's Backbone! Sit down, sit down!'")
            rand_npc()
            reputation_speech(player)
        if fiencitylook == "shop":
            print("There is a tall, lanky teen. 'Oh, G'day mate, didn't see you there. Take a look, will you?'")
            rand_npc()
            reputation_speech(player)
        if fiencitylook ==  "guild":
            print("There is the Warrior Faction, the Merchant Republic, the Thieve's Scowl and the Mage's Clan.")
            rand_npc()
            reputation_speech(player)
    if travelchoice == "Draer":
        draecitylook = input("Tavern, shop or guild?")
        if draecitylook == "tavern":
            print("This is the Gaelic Rowboat. It is a joyful shade of green, though smells very strange.")
            rand_npc()
            reputation_speech(player)
        if draecitylook == "shop":
            print("The Cracker Commercial. It is a large market, with lots of people.")
            rand_npc()
            reputation_speech(player)
        if draecitylook == "guild":
            print("There is the Warrior Faction, the Merchant Republic, the Thieve's Scowl and the Mage's Clan.")
            rand_npc()
            reputation_speech(player)
    if travelchoice == "Scaul":
        scaucitylook = input("Tavern, shop or guild?")
        if scaucitylook == "tavern":
            print("This is the Woden Crow. The building is wooden and rotten.")
            rand_npc()
            reputation_speech(player)
        if scaucitylook == "shop":
            print("The Grim Man's Hole. It is an empty shade of gray, tainted with the reek of death.")
            rand_npc()
            reputation_speech(player)
        if scaucitylook == "guild":
            print("No Guild wants to be here.")
            rand_npc()
            reputation_speech(player)
    return player


if __name__ == "__main__":
    main()









