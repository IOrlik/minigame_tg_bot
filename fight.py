from abc import ABC, abstractmethod
import random 
from Data import characters, DataBase



class Character(ABC):
    def __init__(self, level, health, strength, name):
        self.level = level 
        self.health = health
        self.strength = strength 
        self.name = name
        self.xp = 0

    @abstractmethod
    def attack(self):
        pass
    
    def take_damage(self, attacks_damage):
        print(f'{self.name} получает {attacks_damage} единиц урона')
        self.health -= attacks_damage 
        if self.health > 0:
            text = (f'У {self.name}а остается {round(self.health, 1)} здоровья')
        else: text = (f'У {self.name}а не осталось здоровья, персонаж погибает')
        print('\n')
        return text
    def is_alive(self):
        if self.health > 0: 
            return True 
        else: return False 
    def level_up(self): 
        if self.xp == 100:
            self.level += 1
            self.health *= 1.1 
            self.strength *= 1.1 
            self.xp = 0 
        else: 
            pass
    def show_stats(self):
        stats = (f'Имя: {self.name}\nУровень: {self.level}\nЗдоровье: {round(self.health, 1)}\nСила: {self.strength}\nОпыт: {self.xp}/100')
        return stats 
    
class Warrior(Character):
    def __init__(self, level, health, strength, name):
        super().__init__(level, health, strength, name)

    def special_ability(self):  
        damage = self.strength * random.uniform(1.5, 2)
        text = f'{self.name} впал в ярость и атаковал, нанеся {round(damage, 1)} единиц урона'
        return damage, text

    def attack(self):
        attacks_damage = random.uniform((self.strength*0.8) , (self.strength*1.2))
        text = f'{self.name} атакует, нанося {round(attacks_damage, 1)} урона'
        return attacks_damage, text

class Archer(Character):
    def __init__(self, level, health, strength, name):
        super().__init__(level, health, strength, name)

    def attack(self):
        chance = random.randint(1,10)
        if chance > 3:
            attacks_damage = random.uniform(self.strength*0.9, self.strength*1.1)
            text = f'{self.name} атакует, нанося {round(attacks_damage, 1)} урона'
            return attacks_damage, text
        
        else: 
            attacks_damage = random.uniform(self.strength*0.9, self.strength*1.1)*1.5
            text = f'{self.name} наносит критический удар, нанося {round(attacks_damage, 1)} урона'
            return attacks_damage, text
    

class Mage(Character):
    def __init__(self, level, health, strength, name):
        super().__init__(level, health, strength, name)
        self.mana = 100

    def special_ability(self): 
        damage = self.strength * random.uniform(1.5, 2)*(self.mana/100)
        text = f'{self.name} бьет молнией, нанося {round(damage, 1)} единиц урона'
        return damage, text

    
    def heal(self):
        if self.health < 0.4 * self.health:
            healed_hp = random.uniform(0,3*self.health, 0,5*self.health)
            self.health += healed_hp
            text = f'Маг восстановил {round(healed_hp, 1)} здоровья'
            return text

    def attack(self):
        attacks_damage = random.uniform(self.strength*0.8 , self.strength*1.2)
        text = f'{self.name} атакует, нанося {round(attacks_damage, 1)} урона'
        return attacks_damage, text
    
char_id = 0 
char_amount = 0 
def create_archer(hp, strength, name):
    #char_id += 1 
    global char_amount
    char_amount += 1 
    if char_amount <= 3:
        return Archer(1, hp, strength, name)
    else: print('Превышено максимальное кол-во персонажей')
def create_mage(hp,strength, name):
    #char_id += 1 
    global char_amount
    char_amount += 1
    if char_amount <= 3:
        return Mage(1, hp, strength, name)
    else: print('Превышено максимальное кол-во персонажей')
def create_warrior(hp, strength, name):
    # char_id += 1 
    global char_amount
    char_amount += 1
    if char_amount <= 3:
        return Warrior(1, hp, strength, name)
    else: print('Превышено максимальное кол-во персонажей')
    

# warrior = create_warrior(150, 40, 'Воин')
# arch = create_archer(80, 50, 'Лучник')
# mage = create_mage(120, 60, 'Маг')

def random_attacking_char(character1, character2, character3 = None):
    if character3 != None:
        choice = random.randint(1, 3)
        if choice == 1: 
            damage_nr, text = character1.attack()
            damage = round(damage_nr, 1)
            if random.randint(1,2) == 1: 
                return character2.take_damage(damage), text
            else: return character3.take_damage(damage), text
        elif choice == 2:
            damage_nr, text = character3.attack()
            damage = round(damage_nr, 1)
            if random.randint(1,2) == 1: 
                return character1.take_damage(damage), text
            else: return character2.take_damage(damage), text
        elif choice == 3:
            damage_nr, text = character2.attack()
            damage = round(damage_nr, 1)
            if random.randint(1,2) == 1: 
                return character1.take_damage(damage), text
            else: return character3.take_damage(damage), text
    else:
        choice = random.randint(1,2)
        if choice == 1:
            damage_nr, text = character1.attack()
            damage = round(damage_nr, 1)
            return character2.take_damage(damage), text
        else: 
            damage_nr, text = character2.attack()
            damage = round(damage_nr, 1)
            return character1.take_damage(damage), text

    if character1 == Mage():
        character1.heal()
    if character2 == Mage():
        character2.heal()
    if character3 != None and character3 == Mage():
        character3.heal()

def create_character(id_user, character_choice):
    DataBase[id_user] = DataBase.get(id_user, [])
    if len(DataBase[id_user]) < 3:
        if character_choice == 1:
            DataBase[id_user].append(create_archer(110, 40, "Archer"))
            w_message = "Лучник создан"
        elif character_choice == 2: 
            DataBase[id_user].append(create_mage(90, 60, "Mage"))  
            w_message = "Маг создан" 
        else:
            DataBase[id_user].append(create_warrior(160, 30, "Warrior"))
            w_message = "Воин создан"        
    else: w_message = 'Превышено максимальное кол-во персонажей'
    return DataBase[id_user], w_message



# def random_attacking_char():
#     a = random.randint(1,3)
#     if a == 1: 
#         damage = round(arch.attack(), 1)
#         if random.randint(1,2) == 1: 
#             mage.take_damage(damage)
#         else: warrior.take_damage(damage)
#     elif a == 2:
#         damage = round(mage.attack(), 1)
#         if random.randint(1,2) == 1: 
#             arch.take_damage(damage)
#         else: warrior.take_damage(damage)
#     elif a == 3: 
#         damage = round(warrior.attack(), 1)
#         if random.randint(1,2) == 1: 
#             mage.take_damage(damage)
#         else: arch.take_damage(damage)

# print("Маг: ")
# mage.show_stats()
# print('\n')
# print("Воин: ")
# warrior.show_stats()
# print('\n')
# print("Лучник: ")
# arch.show_stats()

# print("===================- Бой начался -=====================")     
# while arch.is_alive() and mage.is_alive() and warrior.is_alive():
#     random_attacking_char()


# print("==================- Бой закончился -====================")  
# if arch.is_alive():
#     print(f'{arch.name} жив')
# else: print(f'{arch.name} умер')
# if mage.is_alive():
#     print(f'{mage.name} жив')
# else: print(f'{mage.name} умер')
# if warrior.is_alive():
#     print(f'{warrior.name} жив')
# else: print(f'{warrior.name} умер')