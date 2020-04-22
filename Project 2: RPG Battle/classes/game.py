import random
from classes.inventory import Item


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    B0LD = "\033[1m"
    UNDERLINE = "\033[4m"


class Player:

    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.B0LD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.B0LD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.B0LD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ':', spell.name, '(cost: ', str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.B0LD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item['item'].name, ":", item['item'].description, "x(" +
                  str(item['Quantity']) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.B0LD + "    Target:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + "." + enemy.name)
                i += 1
        choice = int(input("    choose target: ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = ((self.hp / self.max_hp) * 100) / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp += hp_string

        print("                              __________________________________________________")
        print(bcolors.B0LD + self.name + "         " +
              current_hp + " |" + bcolors.FAIL +
              hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.max_hp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.max_mp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 9:
            decr = 9 - len(hp_string)
            while decr > 0:
                current_hp += " "
                decr -= 1
            current_hp += hp_string
        else:
            current_hp += hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decr = 7 - len(mp_string)
            while decr > 0:
                current_mp += " "
                decr -= 1
            current_mp += mp_string
        else:
            current_mp += mp_string

        print("                            _________________________                    __________")
        print(bcolors.B0LD + self.name + "         " +
              current_hp + " |" + bcolors.OKGREEN +
              hp_bar +
              bcolors.ENDC + bcolors.B0LD + "|          " +
              current_mp + " |" + bcolors.OKBLUE +
              mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.get_hp() / self.max_hp * 100

        if self.mp < spell.cost or spell.type == "White" and pct > 50:
            return self.choose_enemy_spell()
        else:
            return spell, magic_dmg
