
#the purpose of this class is that it has properties which are shared by both player and enemy
class Character(object):
    def __init__(self,Name,Weapon):
        self.Name= Name
        self.HP = -1
        self.WeaponName = Weapon[0]
        self.WeaponPower = Weapon[1]

    def __str__(self):
        return ('Name: {}. HP: {}. Weapon: {} ({} damage).'.format(self.Name, self.HP,self.WeaponName, self.WeaponPower))

    def attack(self, enemy):
        if enemy.HP > 0:
            enemy.HP -= self.WeaponPower
            print("{} attacked {}!".format(self.Name, enemy.Name))
        if enemy.HP <= 0:
            print("{} is Dead!".format(enemy.Name))


class Ork(Character):
    def __init__(self, Name, Weapon):
        Character.__init__(self, Name, Weapon)
        self.HP = 20


class Player(Character):
    def __init__(self, Name, Weapon):
        Character.__init__(self, Name, Weapon)
        self.HP = 100
        self._bandages = 3
    def heal(self):
        if self._bandages > 0:
            self.HP = 100
            self._bandages -= 1
            print("{}'s health is restored to 100!".format(self.Name))
        else:
            print("No bandages left!")

    def loot(self,body):
        if body.HP <= 0:
            self.WeaponName = str(body.WeaponName)
            self.Power = str(body.WeaponPower)
            print ("Yay you received the item {} with the strenght {}".format(self.WeaponName,self.Power))


Frodo = Player("Frodo", ("Dolch", 12))
Orkan = Ork("Orkan", ("Keule", 15.5))

print(Frodo)
print(Orkan)

Frodo.attack(Orkan)
Orkan.attack(Frodo)
Frodo.attack(Orkan)

print(Frodo)

Frodo.loot(Orkan)
Frodo.heal()

print(Frodo)
print(Orkan)


