import random

class Pokemon(object):

    def __init__(self,kind):

        # store as private instance variable
        self.__kind = kind
        self.__strength = random.randint(1,255)
        self.__catchrate = random.randint(1,10)

    def __update_strength(self,minus):
        self.__strength = self.__strength - minus

    def attack(self,other):
        return other.__update_strength(1.1 * self.__strength)

    def get_kind(self):
        return self.__kind

    def get_strength(self):
        return self.__strength

    def get_catchrate(self):
        return self.__catchrate


class Trainer(object):

    def __init__(self,name):


        # store as private instance variable
        self.__name = name

        # create empty list to store caught pokemon
        self.__pokemons = []


    def catch_pokemon(self,pkmn):


        # use random number to model likeliness of catching the pokemon
        random_number = random.randint(1,100)

        # check if random number is a multiple of the pokemon's catch rate
        if random_number % pkmn.get_catchrate() == 0:

            # trainer can only keep 6 pokemon
            if len(self.__pokemons) < 6:
                print("YES! {0:s} caught a wild {1:s}".format(self.__name,pkmn.get_kind()))
                self.__pokemons.append(pkmn)

            else:
                print("{0:s} already has 6 pokemon sorry :(".format(self.__name))

        # pokemon gets away
        else:
            print("Wild {0:s} fled.".format(pkmn.get_kind()))



    def print_pokemon_stats(self):


        print("{0:s}'s Pokemon:".format(self.__name))

        index = 0
        for pkmn in self.__pokemons:
            print("\tPokemon {0:d}: {1:s} - {2:d}".format(index,pkmn.get_kind(),pkmn.get_strength()))
            index += 1


    def release_pokemon(self,index):

        # ensure index is a valid index before removing pokemon
        if index >= 0 and index < len(self.__pokemons):
            del self.__pokemons[index]


    def get_pokemons(self):

        return self.__pokemons



    def get_name(self):

        return self.__name



def fight(trainer1,trainer2):


    # get list of pokemon from both trainers
    pkmn_trainer1 = trainer1.get_pokemons()
    pkmn_trainer2 = trainer2.get_pokemons()

    # if both don't have any pokemon they cannot fight
    if pkmn_trainer1 == [] and pkmn_trainer2 == []:
        print("You cannot fight!")
        return

    # if only trainer2 has pokemon trainer2 wins
    elif pkmn_trainer1 == []:
        print("{0:s} has no pokemon left. {1:s} won!".format(trainer2.get_name(),trainer1.get_name()))
        return

    # if only trainer1 has pokemon trainer1 wins
    elif pkmn_trainer2 == []:
        print("{0:s} has no pokemon left. {1:s} won!".format(trainer2.get_name(),trainer1.get_name()))
        return

    # get the first pokemon they caught
    pkmn1 = pkmn_trainer1[0]
    pkmn2 = pkmn_trainer2[0]

    # let the two pokemon attack each other as long as none has below 0 strength
    counter = 1
    while pkmn1.get_strength() > 0 and pkmn2.get_strength() > 0:

        # make sure only one pokemon attacks at a time
        if counter % 2 == 1:
            pkmn1.attack(pkmn2)
            print("{0:s}'s {1:s} attacks {2:s}'s {3:s}".format(trainer1.get_name(),pkmn1.get_kind(),trainer2.get_name(),pkmn2.get_kind()))
        else:
            pkmn2.attack(pkmn1)
            print("{0:s}'s {1:s} attacks {2:s}'s {3:s}".format(trainer2.get_name(),pkmn2.get_kind(),trainer1.get_name(),pkmn1.get_kind()))
        counter += 1

    # release the pokemon whose strength is below 0 (only consider the ones who just fought)
    if pkmn1.get_strength() <= 0:
        trainer1.release_pokemon(0)

    if pkmn2.get_strength() <= 0:
        trainer2.release_pokemon(0)

    # call next round of fighting recursively
    fight(trainer1,trainer2)

################################################################################

### test code ###

ash = Trainer("Ash")
ash.catch_pokemon(Pokemon("Pidgey"))
ash.catch_pokemon(Pokemon("Onix"))
ash.catch_pokemon(Pokemon("Azumarill"))
ash.catch_pokemon(Pokemon("Eevee"))
ash.catch_pokemon(Pokemon("Primeape"))
ash.catch_pokemon(Pokemon("Phanpy"))
ash.catch_pokemon(Pokemon("Rattata"))

misty = Trainer("Misty")
misty.catch_pokemon(Pokemon("Pidgey"))
misty.catch_pokemon(Pokemon("Onix"))
misty.catch_pokemon(Pokemon("Azumarill"))
misty.catch_pokemon(Pokemon("Eevee"))
misty.catch_pokemon(Pokemon("Primeape"))
misty.catch_pokemon(Pokemon("Phanpy"))
misty.catch_pokemon(Pokemon("Rattata"))

ash.print_pokemon_stats()
misty.print_pokemon_stats()
#
fight(ash,misty)
