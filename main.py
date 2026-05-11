import random
from world.location import world
#from monster.wolf import wolf


base = {
    'base_speed': 8,
    'base_shield': 0,
    'base_armor': 10,
    'base_dice_string_hp':'1d8'
}
playeer_1 = {
        'name': 'heroy',
        'hp': None,
        'max-hp': None,
        'level': 1,
        'location': 'лес',
        'proficiency_bonus': 0, #бонус мастерства
        'resistances': [],  #бонус сопротивление
        'vulnerability':[],  #бонус уязвимость
        'base_stat':{
            'strength ': None,     
            'dexterity': None,
            'constitution': None,
            'intelligence': None,
            'wisdom': None,
            'charisma': None
        },
        'inventory':{},
        'equipment':{
            'armor':{
                'name': 'легкий доспех',
                'max_dex_mod': 99,
                'base_armor': 0
            },
            'shield': {
                'name': 'без щита',
                'type': None,
                'defense': 0
            },
            'weapon':{
                'name':'длинный меч',
                'type':'меч',
                'dice_string': '1d8',
                'mod_power':''
            }
        } 
}
# попадание: игрок бросает кубик 1д20
# к результату брока кубика 1д20 + модификатор силы/ловкости + бонус мастерства
# сравниваем результат броска с защитой противника и если она больше или равно - попадание
# дальше бросаем кость урона в зависимости от оружия, например, 1д8 + модификатор силы/ловкости
# если есть сопротивления или уязвимости, то делем или умножаем конечный результат на 2

# расчета силы и ловкости
def dex_mod(params):
    scope = (params - 10) // 2
    return scope

# шанс попадания
def hit_chance(modifier_stat, proficiency_bonus):
    hit = random.randint(1,20) + modifier_stat + proficiency_bonus
    return hit

# класс брони универсальная функция
def armor_class(dexterity_scope, armor_item, bonus_shield):
    dex_mod = dexterity_scope
    base_armor = armor_item['base_armor']
    max_dex_mod = armor_item['max_dex_mod']
    ac = base_armor + min(dex_mod, max_dex_mod) + bonus_shield
    return ac

# расчет количества урона
def damage(dice_string):
    count_bone = int(dice_string.split('d')[0])
    max_count_bone = int(dice_string.split('d')[1])
    count = 0
    for i in range(count_bone):
        count += random.randint(1, max_count_bone)
    return count

def initiative(dexterity_scope):
    init = random.randint(1,20) + dexterity_scope
    return init

# функция расчета здоровья(базовая кость, существо):
#       max_hp = базовая кость + существо[мод телосложения]
#       
#       
#       
#           
         
#def playeer_punch(враг, игрок, сила_мод)
#    if попадание игрока больше или равно ас_врага:
#       урон = функция_получения_урона + сила_мод
#        если враг имеет резист к типу атаки оружия:
#               урон /=  2
#               вернуть (урон, сообщение о том сколько нанес игрок врагу)
#        иначе если враг имеет уязвимость к типу атаки оружия
#               урон *= 2
#               вернуть (урон, сообщение о том сколько нанес игрок врагу)
#        иначе:
#               вернуть (урон, сообщение о том сколько нанес игрок врагу)
#   иначе
#       вернуть сообщение, что игрок промахнулся
#

playeer = {
            'name': 'heroy',
            'hp': 20,
            'max-hp': 20,
            'location': 'лес',
            'damage': 8,
            'base_stat':{
                'strength ': 5,     
                'agility': 7,
                'luck': None,
                'speed': 5,
                'shield': 2
            },
            'effects':[],
            'inventory':{},
            'equipment':{
                'armor':{
                    'name': 'бам',
                    'shield': 5
                }
            }
        } 
enemies = {
            'волк': {
                'name':'Волк',
                'hp': 6,
                'max_hp': 5,
                'location': ['лес', 'пещера'],
                'base_stat':{
                    'damage': 4,
                    'agility': 7,
                    'luck': None,
                    'speed': 7,
                    'shield': 1
                },
                'effects':[]
            }
        }

def playeer_punch(enemy, playeer_base, enemy_base):
    if playeer_base['luck'] > random.random():
        count_block = playeer_base['damage'] - enemy_base['shield']
        if count_block <= 0:
            return (enemy['hp'], f'{enemy["name"]} заблокировал твой удар')
        else:
            enemy['hp'] -= count_block
            return (enemy['hp'], f'Вы попали по {enemy["name"]}у и нанесли {count_block} урона. У существа осталось {enemy["hp"]}')
    else:
        return (enemy['hp'], 'Вы промахнулись')

def enemy_punch(enemy, playeer, player_state, state_active, playeer_base, enemy_base):
    if enemy_base['luck'] > random.random():
        if player_state == 'уклониться' and state_active:
            baff_agility = (playeer_base['agility'] * 2) / 15
            if baff_agility >= enemy_base['agility']:
                return (playeer['hp'], f'{enemy["name"]} не попал по тебе')
            
            else:
                playeer['hp'] -= enemy_base['damage']
                return (playeer['hp'], f'{enemy["name"]} нанес тебе {enemy_base["damage"]}')              
        
        if player_state == 'защищаться' and state_active:
            baff_shield = playeer_base['shield'] * 2
        else:
            baff_shield = playeer_base['shield']

        count_block = enemy_base['damage'] - baff_shield
        if count_block <=0:
            return (playeer['hp'], f'Ты заблокировал атаку {enemy["name"]}а')
            
        else:
            playeer['hp'] -= count_block
            return (playeer['hp'], f'{enemy["name"]} нанес тебе {count_block}')
             
    else:
        return (playeer['hp'], f'{enemy["name"]} промахнулся')

def choice_playeer(enemy, choice, playeer_base, enemy_base):
    if choice == 'атаковать':
        player_state = 'атаковать'
        enemy['hp'], message = playeer_punch(enemy, playeer_base, enemy_base)
        state_active = False
        return (player_state, enemy['hp'], message, state_active)                           
    elif choice == 'защищаться':
        player_state = 'защищаться'
        state_active = True
        return (player_state, enemy['hp'], 'Вы выбрали защищаться', state_active)
    
    elif choice == 'уклониться':
        player_state = 'уклониться'
        state_active = True
        return (player_state, enemy['hp'], 'Вы выбрали уклониться', state_active)

def game_core():
    playeer_base = playeer['base_stat']   

    while playeer['hp'] > 0:
        loc = world[playeer['location']]
        print(f'{loc["descriptions"]}')
        print(f'Твое здоровье: {playeer["hp"]}, максимальное здоровье: {playeer["max-hp"]}')
        print('Ты можешь пойти на', ' или '.join(loc['exit'].keys()))
        
        while True:
            command = input('Что ты будешь делать? \n').lower()
            if command in loc['exit']:
                break
            else:
                print('Ты не можешь туда пойти')

        playeer['location'] = loc['exit'][command]
        if random.random() < 0.5 and 'enemies' in loc:
            name_enemies = random.choice(loc['enemies'])
            enemy = enemies[name_enemies].copy()
            enemy_base = enemy['base_stat']
            enemy_base['luck'] = enemy_base['agility'] / 10

            print(f'На вас напал {enemy["name"]}! hp: {enemy["hp"]}, damage:{enemy_base["damage"]}')
            
            # сравниваю скорость существ, чтобы определить кто будет ходить первым
            if base['base_speed'] + playeer_base['speed'] > base['base_speed'] + enemy_base['speed']:
                first_move = 'игрок'

            elif base['base_speed'] + enemy_base['speed'] > base['base_speed'] + playeer_base['speed']:
                first_move = 'враг'

            else:
                first_move = random.choice(['игрок','враг'])

            player_state = None
            state_active = False
            # основной цикл боя                
            while playeer['hp'] > 0 and enemy['hp'] > 0:                                
                if first_move == 'игрок':
                    if playeer['hp'] > 0:
                        # атака игрока + цикл, который проверяет что написал игрок
                        while True:
                            choice = input('Ты можешь атаковать, защищаться или уклониться. Что ты выбирешь? \n').lower()
                            if choice in ('атаковать', 'защищаться', 'уклониться'):
                                break
                            else:
                                print('Вам необходимо ввести: атаковать, защищаться или уклониться')
                                continue
                    player_state, enemy_hp, message, state_active = choice_playeer(enemy, choice, playeer_base, enemy_base)                            
                    enemy['hp'] = enemy_hp
                    if message:
                        print(message)

                    if enemy['hp'] <= 0:
                        print('Вы победили существо')
                        break
                    
                    # атака врага
                    playeer['hp'], message = enemy_punch(enemy, playeer, player_state, state_active, playeer_base, enemy_base)
                    print(message)
                    if state_active:
                        state_active = False                           

                elif first_move == 'враг':
                    # атака врага
                    playeer['hp'], message = enemy_punch(enemy, playeer, player_state, state_active, playeer_base, enemy_base)
                    print(message)
                    if state_active:
                        state_active = False

                    if playeer['hp'] <= 0:
                        print('Вас убили')
                        break

                    if playeer['hp'] > 0:
                        # атака игрока
                        while True:
                            choice = input('Ты можешь атаковать, защищаться или уклониться. Что ты выбирешь? \n').lower()
                            if choice in ('атаковать', 'защищаться', 'уклониться'):
                                break
                            else:
                                print('Вам необходимо ввести: атаковать, защищаться или уклониться')
                                continue
                    player_state, enemy_hp, message, state_active = choice_playeer(enemy, choice, playeer_base, enemy_base)
                    enemy['hp'] = enemy_hp
                    if message:
                        print(message)
            else:
                print('Вас убили')
        else:
            continue



# Добавить уровень персонажа
# добавить новых существ
# добавить новые предметы, у предмета будет параметр шанса получения %, сам параметр предмет, будет иметь тип обьект значений {'шкура': 1}
# Добавить условие после цикла или внутри него? если рандомное число меньше шанса получения предмета
#   игрок идет дальше
# иначе
#   выводится сообщение, что игрок получил предмет
#   переменной из инвентаря игрока добавляется предмет, например, шкура += 1, изначально значение None
# Добавить виды урона - колющий, дробящий, рубящий
# Добавить виды состояний - отравление, воспломенение, кровотячение

