# Weaknesses and resistances that will affect how moves interact with a specific pokemon
weakness_dict = {'fire': 'water', 'water': 'grass', 'grass': 'fire'}
resistance_dict = {'water': 'fire', 'fire': 'grass', 'grass': 'water'}

# Pokemon-class serves as ancestor for all pokemons
class Pokemon:
    def __init__(self, name, level=1, pokemon_type='Normal', current_hp=0, knocked_out=True, moves={'Scratch': 10}):
        self.name = name
        self.level = level
        self.type = pokemon_type
        self.mhp = 10 * self.level # Max hitpoints of this pokemon
        self.chp = current_hp
        self.ko = knocked_out
        self.moves = moves

    # Method used for taking damage
    def lose_health(self, dmg):
        self.chp -= dmg
        if self.chp <= 0:
            print("{name} now has 0 left.".format(name=self.name, chp=self.chp))
            print("{name} got knocked out!".format(name=self.name))
            self.knocked_out = True
            self.chp = 0
        else:
            print("{name} now has {chp} left.".format(name=self.name, chp=self.chp))

    # Method for healing a pokemon
    def gain_health(self, healing_received):
        self.chp += healing_received
        if self.chp > self.mhp:
            self.chp = self.mhp
            print("{name} was healed and is back at full hp".format(name=self.name))
        else:
            print("{name} was healed and now has {chp}".format(name=self.name, chp=self.chp))

    # Method used for reviving a pokemon whose self.ko=True
    def revive(self, heal):
        self.chp += heal
        self.knocked_out = False
        if self.chp > self.mhp:
            self.chp = self.mhp
        print("{name} is back with {chp}".format(name=self.name, chp=self.chp))

    # Method used for attacking another pokemon
    def attack(self, target, move):
        if self.type == weakness_dict[target.type]:
            print("It's super effective!")
            target.lose_health(self.moves[move] * 2)
        elif self.type == resistance_dict[target.type]:
            print("It's not very effective...")
            target.lose_health(int(self.moves[move] * 0.5))
        else:
            print("It hits!")
            target.lose_health(self.moves[move])

# Instantiating some pokemons for testing
charmander = Pokemon('Charmander', 5, 'fire', 50, False, {'Scratch': 10, 'Fire Breath': 30})
squirtle = Pokemon('Squirtle', 5, 'water', 5, False, {'Tackle': 10, 'Water Gun': 30})
bulbasaur = Pokemon('Bulbasaur', 5, 'grass', 50, False, {'Wine Whip': 10, 'Seedstorm': 30})
#charmander2 = Pokemon('Charmander2', 5, 'fire', 50, False, {'Scratch': 10, 'Fire Breath': 30})

# Using some pokemon-methdods for testing
#charmander.attack(squirtle, 'Scratch')
#squirtle.attack(charmander, 'Water Gun')
#charmander.attack(charmander2, 'Fire Breath')

# Trainer-class serves as base for player-character and NPCs
class Trainer:
    def __init__(self, name, pokemons, potions, active_pokemon=0):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.active = active_pokemon
        

    # Used for targeting and attacking other trainers
    def attack_trainer(self, target_trainer, move):
        self.pokemons[self.active].attack(target_trainer.pokemons[target_trainer.active], move)

    # Used for using potions
    def use_potion(self, potion):
        if potion in self.potions:
            self.pokemons[self.active].gain_health(self.potions[potion])
            self.potions.pop(potion)
        else:
            print("No such potion in inventory.")

    # Used for switching pokemons
    def switch_pokemon(self, new_active_pokemon):
        if new_active_pokemon < len(self.pokemons):
            print("Come back {old}, you've had enough".format(old=self.pokemons[self.active].name))
            self.active = new_active_pokemon
            print("Go {new}, I choose you!".format(new=self.pokemons[self.active].name))
        else:
            print("That pokemon does not exist.")
    
    # Used for checking what items the trainer has in inventory
    def check_inventory(self):
        print(self.potions)

# Instantiating some trainers for testing
ash = Trainer('Ash', [charmander, squirtle], {'hp_potion': 10}, 1)
gary = Trainer('Gary', [bulbasaur, squirtle], {'hp_potion': 10, 'super_hp_potion': 30}, 0)

# Using some trainer-methods for testing
# ash.attack_trainer(gary, 'Scratch')
# ash.use_potion("hp_potion")
# ash.check_inventory()
ash.switch_pokemon(0)