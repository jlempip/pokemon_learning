weakness_dict = {'fire': 'water', 'water': 'grass', 'grass': 'fire'}
resistance_dict = {'water': 'fire', 'fire': 'grass', 'grass': 'water'}

class Pokemon:
    def __init__(self, name, level=1, pokemon_type='Normal', curr_hp=0, knocked_out=True, moves={'Scratch': 10}):
        self.name = name
        self.level = level
        self.type = pokemon_type
        self.mhp = 10 * self.level
        self.chp = curr_hp
        self.ko = knocked_out
        self.moves = moves

    def lose_health(self, dmg):
        self.chp = self.chp - dmg
        if self.chp <= 0:
            print("{name} now has 0 left.".format(name=self.name, chp=self.chp))
            print("{name} got knocked out!".format(name=self.name))
            self.knocked_out = True
            self.chp = 0
        else:
            print("{name} now has {chp} left.".format(name=self.name, chp=self.chp))

    def revive(self, heal):
        self.chp += heal
        self.knocked_out = False
        if self.chp > self.mhp:
            self.chp = self.mhp
        print("{name} is back with {chp}".format(name=self.name, chp=self.chp))

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

charmander = Pokemon('Charmander', 5, 'fire', 50, False, {'Scratch': 10, 'Fire Breath': 30})
#charmander2 = Pokemon('Charmander2', 5, 'fire', 50, False, {'Scratch': 10, 'Fire Breath': 30})
squirtle = Pokemon('Squirtle', 5, 'water', 5, False, {'Tackle': 10, 'Water Gun': 30})
bulbasaur = Pokemon('Bulbasaur', 5, 'grass', 50, False, {'Wine Whip': 10, 'Seedstorm': 30})

#charmander.attack(squirtle, 'Scratch')
#squirtle.attack(charmander, 'Water Gun')
#charmander.attack(charmander2, 'Fire Breath')

class Trainer:
    def __init__(self, name, pokemons, potions, active_pokemon=0):
        self.name = name
        self.pokemons = pokemons
        self.active = active_pokemon
        self.potions = potions

    def attack_trainer(self, target_trainer, move):
        self.pokemons[self.active].attack(target_trainer.pokemons[target_trainer.active], move)

    def use_potion(self, potion):
        pass

ash = Trainer('Ash', [charmander, squirtle], 0, {'hp_potion': 10})
gary = Trainer('Gary', [bulbasaur, squirtle], 0, {'hp_potion': 10, 'super_hp_potion': 30})

ash.attack_trainer(gary, 'Scratch')