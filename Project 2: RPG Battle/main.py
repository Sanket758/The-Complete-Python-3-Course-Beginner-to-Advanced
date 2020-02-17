from classes.game import Player, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create black magic
Fire = Spell("Fire", 25, 600, "Black")
Thunder = Spell("Thunder", 25, 600, "Black")
Blizzard = Spell("Blizzard", 20, 400, "Black")
Meteor = Spell("Meteor", 40, 1200, "Black")
Quake = Spell("Quake", 25, 850, "Black")

# create white magic
Cure = Spell("Cure", 25, 600, "White")
Aspirin = Spell("Aspirin", 35, 1200, "White")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP of one party", 10000)
hielixir = Item("MegaElixir", "elixir", "Fully restores HP/MP", 10000)

grenade = Item("Granade", "attack", "Deals 500 damage", 500)

player1_spells = [Fire, Thunder, Blizzard, Meteor, Cure, Aspirin]
player1_items = [{'item': potion, 'Quantity': 15},
                 {'item': hipotion, 'Quantity': 5},
                 {'item': superpotion, 'Quantity': 5},
                 {'item': elixir, 'Quantity': 5},
                 {'item': hielixir, 'Quantity': 5},
                 {'item': grenade, 'Quantity': 5}]

# Instantiate Characters
player1 = Player("Naruto :", 3500, 132, 300, 40, player1_spells, player1_items)
player2 = Player("Sasuke :", 3400, 130, 311, 40, player1_spells, player1_items)
player3 = Player("Sakura :", 2300, 148, 288, 40, player1_spells, player1_items)

# enemy party
enemy_spells = [Fire, Thunder, Blizzard, Meteor, Cure, Aspirin]

enemy1 = Player("Obito  :", 5000, 130, 400, 23, enemy_spells, [])
enemy2 = Player("Madara :", 11000, 781, 525, 23, enemy_spells, [])
enemy3 = Player("Pain   :", 3000, 221, 445, 23, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print(bcolors.FAIL + bcolors.B0LD + "Game On!!!" + bcolors.ENDC)
while running:

    print("="*80)
    print("Name                         HP                                          MP   ")

    for player in players:

        player.get_stats()

    print()
    print("=" * 38 + bcolors.FAIL + "Enemies" + bcolors.ENDC + "=" * 38)

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player1 in players:
        player1.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice)-1

        if index == 0:
            dmg = player1.generate_damage()
            enemy = player1.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name + "for ", dmg, "points")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name, "has died.")
                del enemies[enemy]

        elif index == 1:
            player1.choose_magic()
            magic_choice = int(input("    Choose Magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player1.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player1.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou don't have enough mp" + bcolors.ENDC)
                continue

            if spell.type == "White":
                player1.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals for" + str(magic_dmg), "HP: " + bcolors.ENDC)
            elif spell.type == "Black":
                enemy = player1.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                player1.reduce_mp(spell.cost)
                enemy1.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of damage to " +
                      enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name, "has died.")
                    del enemies[enemy]

        elif index == 2:
            player1.choose_item()
            item_choice = (int(input("Choose item: ")))-1

            if item_choice == -1:
                continue

            item = player1.items[item_choice]["item"]

            if player1.items[item_choice]["Quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None Left...." + bcolors.ENDC)
                continue

            player1.items[item_choice]["Quantity"] -= 1

            if item.type == "potion":
                player1.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)

            elif item.type == "elixir":
                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player1.hp = player1.max_hp
                    player1.mp = player1.max_mp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player1.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                enemy1.take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals" + str(item.prop) +
                      "point of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name, "has died.")
                    del enemies[enemy]

        '''
        print("="*50)
        print("Enemy HP: ", bcolors.FAIL + str(enemy1.get_hp()) + "/" + str(enemy1.get_max_hp()) + bcolors.ENDC)
        print("Your HP: ", bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_max_hp()) + bcolors.ENDC)
        print("Your MP: ", bcolors.OKGREEN + str(player1.get_mp()) + "/" + str(player1.get_max_mp()) + bcolors.ENDC)
        '''

    # check if game is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False

    # check if enemy won
    elif defeated_players == 2:
        print(bcolors.FAIL + "You Lost!" + bcolors.ENDC)
        running = False

    # Enemy attack Phase
    for enemy in enemies:

        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # choose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name + " deals", str(enemy_dmg), " points of damage to " +
                  players[target].name + bcolors.ENDC)

        if enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "White":
                enemy.heal(magic_dmg)

                print(bcolors.OKBLUE + spell.name + "heals" + enemy.name +
                      "for" + str(magic_dmg), "HP: " + bcolors.ENDC)

            elif spell.type == "Black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)

                print(bcolors.FAIL + enemy.name + " deals", str(magic_dmg), " points of damage to " +
                      players[target].name + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name, "has died.")
                    del players[target]

