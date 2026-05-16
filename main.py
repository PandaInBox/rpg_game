import random
from world.location import world
from monster.being import monsters, cr_templates

base = {
    'base_speed': 8,
    'base_shield': 0,
    'base_armor': 10,
    'base_dice_string_hp':'1d8'
}
playeer = {
        'name': 'heroy',
        'hp': None,
        'max_hp': None,
        'level': 1,
        'location': 'лес',
        'proficiency_bonus': 0, #бонус мастерства
        'resistances': [],  #бонус сопротивление
        'vulnerability':[],  #бонус уязвимость
        'armor_class': None,
        'possession':{      #владение 
            'armore':'',
            'weapon':''
        },
        'base_stat':{
            'strength ': None,     
            'dexterity': None,
            'constitution': None, # телосложение
            'intelligence': None,
            'wisdom': None,
            'charisma': None
        },
        'stat_mod':{
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
                'name':'padded',
                'base_armore': 11,
                'max_dex_mod': 99,
                'stealth_inter': True, #помеха скрытности
                'cost': 5,
                'weight': 8
            },
            'shield': {
                'name': 'без щита',
                'type': None,
                'defense': 0
            },
            'weapon':{
                'name':'longsword',
                'category':'military',
                'type_damage':'slashing',
                'mod_stat': 'strength',
                'dice_string':'1d8',
                'dice_string_two':'1d10',
                'cost': 15,
                'weight': 3
            }
        } 
}

# расчет модификатора характеристик
def dex_mod(params):
    scope = (params - 10) // 2
    return (scope, f'Твой модификатор {scope}')

# шанс попадания
def hit_chance(modifier_stat, proficiency_bonus):
    hit = random.randint(1,20) + modifier_stat + proficiency_bonus
    return (hit, f'Выпало {hit} на попадание')

# класс брони универсальная функция
def armor_class(dexterity_scope, armor_item, bonus_shield):
    dex_mod = dexterity_scope
    base_armor = armor_item['base_armor']
    max_dex_mod = armor_item['max_dex_mod']
    ac = base_armor + min(dex_mod, max_dex_mod) + bonus_shield
    return (ac, f'Твой класс брони: {ac}')

# расчет количества урона
def damage(dice_string):
    count_bone = int(dice_string.split('d')[0])
    max_count_bone = int(dice_string.split('d')[1])
    count = 0
    for i in range(count_bone):
        count += random.randint(1, max_count_bone)
    return (count, f'На кубах выпало {count} урона')

# расчет инициативы
def initiative(dexterity_scope):
    init = random.randint(1,20) + dexterity_scope
    return (init, f'Выпало на кубах {init} инициативы')

# расчет максимального хп + увеличение хп, при достижении нового уровня
def max_hp_chance(base_dice_string_hp, playeer, playeer_mod):
    count_bone = int(base_dice_string_hp.split('d')[0])
    max_count_bone = int(base_dice_string_hp.split('d')[1])
    count = 0
    for i in range(count_bone):
        count += random.randint(1, max_count_bone)
    if playeer['max_hp'] is None:    
        max_hp = 0 + count + playeer_mod['constitution']
        return (max_hp, f'Выпало костей хитов: {max_hp}')
    else:
        max_hp = playeer['max_hp'] + count + playeer_mod['constitution']
        return (max_hp, f'Выпало костей хитов: {max_hp}')

# сбор значений из словаря для атаки
def prepare_attack_profile(attacker):
    if 'equipment' in attacker and 'weapon' in attacker['equipment']:
        attack = attacker['stat_mod']['strength'] + attacker['proficiency_bonus']
        dice = attacker['weapon']['dice_string']
        damage_mod = attacker['stat_mod']['strength']
        damage_type = attacker['weapon']['type_damage']
        return {
            'attack_bonus': attack,
            'dice_string': dice,
            'damage_mod': damage_mod,
            'damage_type': damage_type 
        }
    elif 'attack' in attacker:
        attack = attacker['stat_mod']['strength'] + attacker['proficiency_bonus']
        dice = attacker['attack']['dice_string']
        damage_mod = attacker['stat_mod']['strength']
        damage_type = attacker['attack']['type_damage']
        return {
            'attack_bonus': attack,
            'dice_string': dice,
            'damage_mod': damage_mod,
            'damage_type': damage_type 
        }

# сбор значений из словаря для защиты
def prepare_defender_profile(defender):
        ac = defender['armor_class']
        resistances = defender['resistances']
        vulnerability = defender['vulnerability']
        return {
            'armor_class': ac,
            'resistances': resistances,
            'vulnerability': vulnerability
        }

# удар игрока/монстра
def punch(attacker, defender):
    attack_bonus, dice_string, damage_mod, damage_type = prepare_attack_profile(attacker)
    armor_class, resistances, vulnerability = prepare_defender_profile(defender)
    if hit_chance(attack_bonus) >= armor_class:
        hit_damage = damage(dice_string)[0] + damage_mod
        if damage_type in resistances:
            hit_damage /= 2
            return (hit_damage, f'Было нанесено {hit_damage}')
        
        elif damage_type in vulnerability:
            hit_damage *= 2
            return (hit_damage, f'Было нанесено {hit_damage}')
        
        else:
            return (hit_damage, f'Было нанесено {hit_damage}')
    else:
        return (0, 'Ты промахнулся')

def get_enemy(enemy):
   enemy_chel_rat = enemy['challenge_rating']
   if enemy_chel_rat in cr_templates:
       cr_enemy = cr_templates[enemy_chel_rat]
       max_hp = cr_enemy['max_hp']
       proficiency_bonus = cr_enemy['proficiency_bonus']
       dice_string = cr_enemy['attack']['dice_string']
       strength = cr_enemy['base_stat']['strength']
       dexterity = cr_enemy['base_stat']['dexterity']
       constitution = cr_enemy['base_stat']['constitution']
       intelligence = cr_enemy['base_stat']['intelligence']
       wisdom = cr_enemy['base_stat']['wisdom']
       charisma = cr_enemy['base_stat']['charisma']
              
       enemy['proficiency_bonus'] = proficiency_bonus  

       enemy['base_stat']['strength'] = strength
       enemy['base_stat']['dexterity'] = dexterity
       enemy['base_stat']['constitution'] = constitution
       enemy['base_stat']['intelligence'] = intelligence
       enemy['base_stat']['wisdom'] = wisdom
       enemy['base_stat']['charisma'] = charisma

       enemy['stat_mod']['strength'] = dex_mod(strength)[0]
       enemy['stat_mod']['dexterity'] = dex_mod(dexterity)[0]
       enemy['stat_mod']['constitution'] = dex_mod(constitution)[0]
       enemy['stat_mod']['intelligence'] = dex_mod(intelligence)[0]
       enemy['stat_mod']['charisma'] = dex_mod(charisma)[0]
       
       enemy['max_hp'], enemy['hp'] = max_hp_chance(max_hp, enemy['max_hp'], enemy['stat_mod']['constitution'])
       enemy['armor_class'] = armor_class(enemy['stat_mod']['dexterity'], enemy['armor'], enemy['bonus_shield'])[0]
       enemy['attack']['dice_string'] = dice_string            
       return enemy



# функция получения нового оружия игроком(справочник_оружия, будущее_оружие):
#   если будущее_оружее есть в справочнике_оружия
#       справочник_оружия = будущее_оружие[название]
#       обновление_оружие = copy.deepcopy(справочник_оружия)
#       вернуть обновленное_оружие, сообщение, что игрок экипировал оружение название
#   иначе
#       вернуть none, сообщение, что данное оружие невозможно экипировать


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

def game_core2():



def game_core():
    playeer_base = playeer['base_stat']   
    while playeer['hp'] > 0:
        loc = world[playeer['location']]
        print(f'{loc["descriptions"]}')
        print(f'Твое здоровье: {playeer["hp"]}, максимальное здоровье: {playeer["max_hp"]}')
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
            enemy = monsters[name_enemies].copy()
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