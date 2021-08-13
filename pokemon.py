import random

# defining Pokemon types
fire = "Fire"
water = "Water"
grass = "Grass"


# class of pokemon
class Pokemon:

    def __init__(self, name, element, level=1):
        self.name = name
        self.level = level
        self.health = level * 10
        self.max_health = level * 10
        self.element = element
        self.is_knocked_out = False

    # pokemon info
    def __repr__(self):
        return "In this Pokeball there is {name} Pokemon, {element} type, level {level}".format(name=self.name,
                                                                                                element=self.element,
                                                                                                level=self.level)

    def revive(self):
        # Reviving Pokemon - changing status to False
        self.is_knocked_out = False
        # Revive method can be called only if Pokemon was given health.
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name=self.name))

    def knock_out(self):
        # knocking out Pokemon changing status to True
        self.is_knocked_out = True
        # Defeated Pokemon cannot have any health
        if self.health != 0:
            self.health = 0
        print("{name} passed out!".format(name=self.name))

    def lose_health(self, damage):
        # deducting health from current HP remaining
        self.health -= damage
        if self.health <= 0:
            self.health = 0  # making sure that HP is not negative
            self.knock_out()
        else:
            print("{name} has now {hp} health.".format(name=self.name, hp=self.health))

    def healing(self, amount):
        # healing Pokemon
        # if HP goes from 0 - reviving Pokemon
        if self.health == 0:
            self.revive()
        self.health += amount
        # making sure that HP wont go over max HP
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} has now {hp} health.".format(name=self.name, hp=self.health))

    # attack method
    def attack(self, opponent):
        # checking if pokemon is not knocked out
        if self.is_knocked_out:
            print("{name} cannot attack because it is knocked out!".format(name=self.name))
        # If attacking Pokemon is in disadvantage, it deals half of of the damage (level / 2)
        if (self.element == fire and opponent.element == water) or (
                self.element == water and opponent.element == grass) or (
                self.element == grass and opponent.element == fire):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name=self.name,
                                                                                other_name=opponent.name,
                                                                                damage=round(self.level * 0.5)))
            print("It's not very effective!")
            opponent.lose_health(round(self.level * 0.5))
        # If it is in neutral (same type) - deal 100% damage = level
        if self.element == opponent.element:
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name=self.name,
                                                                                other_name=opponent.name,
                                                                                damage=self.level))
            opponent.lose_health(self.level)
        # if opponent is in disadvantage, deal double damage (level * 2)
        if (self.element == fire and opponent.element == grass) or (
                self.element == water and opponent.element == fire) or (
                self.element == grass and opponent.element == water):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name=self.name,
                                                                                other_name=opponent.name,
                                                                                damage=self.level * 2))
            print("It's super effective!")
            opponent.lose_health(self.level * 2)


# three starting pokemon - charmander - fire, bulbasaur - grass, squirtle - water, subclasses of Pokemon class.
class Charmander(Pokemon):
    def __init__(self, level=1):
        super().__init__("Charmander", fire, level)


class Squirtle(Pokemon):
    def __init__(self, level=1):
        super().__init__("Squirtle", water, level)


class Bulbasaur(Pokemon):
    def __init__(self, level=1):
        super().__init__("Bulbasaur", grass, level)


class Trainer:
    # Trainer will have a list of pokemon, potions and a name. When trainer will be activated, first pokemon will be
    # the active one (number 0)
    def __init__(self, pokedex, num_potions, name):
        self.pokemons = pokedex
        self.potions = num_potions
        self.name = name
        self.current_pokemon = 0

    def __repr__(self):
        # info about trainer and their pokemons
        print("The trainer {name} has the following pokemon:".format(name=self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name=self.pokemons[self.current_pokemon].name)

    def pokemon_switch(self, new_pokemon):
        # Switching pokemon to another one given as a parameter
        # First check if the number is valid
        if len(self.pokemons) > new_pokemon >= 0:
            # check if pokemon is knocked out
            if self.pokemons[new_pokemon].is_knocked_out:
                print("{name} is knocked out. Choose another pokemon.".format(name=self.pokemons[new_pokemon].name))
            # check if it is current pokemon
            elif new_pokemon == self.current_pokemon:
                print("{name} is already your active pokemon.".format(name=self.pokemons[new_pokemon].name))
            else:
                self.current_pokemon = new_pokemon
                print("{name}, I choose you!".format(name=self.pokemons[self.current_pokemon].name))

    def use_potion(self):
        # Uses potion to the active pokemon, when potions are available
        if self.potions > 0:
            print("You used a potion on {name}".format(name=self.pokemons[self.current_pokemon].name))
            # potion restores 20 HP
            self.pokemons[self.current_pokemon].healing(20)
            self.potions -= 1
        else:
            print("You are out of potions!")

    def attack_trainer(self, other_trainer):
        # current pokemon attacks current pokemon of the opponent
        my_pokemon = self.pokemons[self.current_pokemon]
        opponent_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(opponent_pokemon)


# defining pokemons with different levels - default is 1
a = Charmander(5)
b = Squirtle(3)
c = Squirtle(8)
d = Bulbasaur(2)
e = Charmander(7)
f = Bulbasaur(10)

# defining trainers, first 3 pokemons going to trainer 1, second 3 to trainer 2
trainer1 = Trainer([a, b, c], 3, "Jerry")
trainer2 = Trainer([d, e, f], 6, "Jay")

print(trainer1)
print(trainer2)

# Testing methods
trainer1.attack_trainer(trainer2)
trainer2.attack_trainer(trainer1)
trainer2.use_potion()
trainer1.attack_trainer(trainer2)
trainer2.pokemon_switch(0)
trainer2.pokemon_switch(1)
