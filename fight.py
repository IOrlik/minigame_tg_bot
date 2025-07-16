from abc import ABC, abstractmethod
import random 
from Data import DataBase, fantasy_warrior_names, fantasy_archer_names, fantasy_mage_names


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

    def show_stats(self):
        stats = (f'Класс: Воин\nИмя: {self.name}\nУровень: {self.level}\nЗдоровье: {round(self.health, 1)}\nСила: {self.strength}\nОпыт: {self.xp}/100')
        return stats 

    def attack(self):
        a = random.randint(1, 10)
        if a > 2:
            attacks_damage = random.uniform((self.strength*0.8) , (self.strength*1.2))
            text = f'{self.name} атакует, нанося {round(attacks_damage, 1)} урона'
            return attacks_damage, text
        else: 
            damage = self.strength * random.uniform(1.5, 2)
            text = f'{self.name} впал в ярость и атаковал, нанеся {round(damage, 1)} единиц урона'
            return damage, text


class Archer(Character):
    def __init__(self, level, health, strength, name):
        super().__init__(level, health, strength, name)

    def show_stats(self):
        stats = (f'Класс: Лучник\nИмя: {self.name}\nУровень: {self.level}\nЗдоровье: {round(self.health, 1)}\nСила: {self.strength}\nОпыт: {self.xp}/100')
        return stats 

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

    def show_stats(self):
        stats = (f'Класс: Маг\nИмя: {self.name}\nУровень: {self.level}\nЗдоровье: {round(self.health, 1)}\nСила: {self.strength}\nОпыт: {self.xp}/100')
        return stats 
    
    def heal(self):
        healed = 0 
        if self.health < 30 and healed == 0 and self.health > 0:
            healed_hp = random.uniform(0.9*self.health, 1.25*self.health)
            self.health += healed_hp
            text = f'{self.name} восстановил {round(healed_hp, 1)} здоровья\nТеперь у персонажа {round(self.health, 1)} здоровья'
            healed += 1
            return text
        return ''

    def attack(self):
        a = random.randint(1, 10)
        if a > 2: 
            attacks_damage = random.uniform(self.strength*0.8 , self.strength*1.2)
            text = f'{self.name} атакует, нанося {round(attacks_damage, 1)} урона'
            return attacks_damage, text
        else: 
            damage = self.strength * random.uniform(1.5, 2)*(self.mana/100)
            text = f'{self.name} бьет молнией, нанося {round(damage, 1)} единиц урона'
            return damage, text

    
def create_archer(hp, strength, name):
    return Archer(1, hp, strength, name)
def create_mage(hp,strength, name):
    return Mage(1, hp, strength, name)
def create_warrior(hp, strength, name):
    return Warrior(1, hp, strength, name)
    

# warrior = create_warrior(150, 40, 'Воин')
# arch = create_archer(80, 50, 'Лучник')
# mage = create_mage(120, 60, 'Маг')

def attack_n_heal(character_att, character_defense1, character_defense2):
    damage_nr, text = character_att.attack()
    damage = round(damage_nr, 1)
    if random.randint(1,2):
        text += ' \n' + character_defense1.take_damage(damage)
        if isinstance(character_defense1, Mage):
            text += ' \n' + character_defense1.heal()
        return text
    else: 
        text += ' \n' + character_defense2.take_damage(damage)
        if isinstance(character_defense2, Mage): 
            text += ' \n' + character_defense2.heal()
        return text 
    

def random_attacking_char(character1, character2, character3):
    text = ''
    choice = random.randint(1, 3)
    if choice == 1: 
        return attack_n_heal(character1, character2, character3)
    elif choice == 2:
        return attack_n_heal(character2, character1, character3)
    elif choice == 3:
        return attack_n_heal(character3, character1, character2)


def create_character(id_user, character_choice):
    w_message = ''
    DataBase[id_user] = DataBase.get(id_user, [])
    if len(DataBase[id_user]) < 3:
        if character_choice == 1:
            name = ''
            name1 = random.choice(fantasy_archer_names)
            while name1 == name: 
                name1 = random.choice(fantasy_archer_names)
            name = name1 
            DataBase[id_user].append(create_archer(110, 40, name))
            w_message = '🏹 Лучник создан'
        elif character_choice == 2: 
            name = ''
            name1 = random.choice(fantasy_mage_names)
            while name1 == name: 
                name1 = random.choice(fantasy_mage_names)
            name = name1 
            DataBase[id_user].append(create_mage(90, 40, name))
            w_message = "🔮 Маг создан" 
        else:
            name = ''
            name1 = random.choice(fantasy_warrior_names)
            while name1 == name: 
                name1 = random.choice(fantasy_warrior_names)
            name = name1 
            DataBase[id_user].append(create_warrior(160, 30, name))
            w_message = "⚔ Воин создан"      
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