cr_templates = {
    0: {
        'max-hp': '1d6',
        'challenge_rating': 0,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '1d4',
        'base_stat': {
            'strength': 10,
            'dexterity': 12,
            'constitution': 10,
            'intelligence': 6,
            'wisdom': 10,
            'charisma': 8
        }
    },
    1/8: {
        'max-hp': '3d6',
        'challenge_rating': 0.125,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '1d6',
        'base_stat': {
            'strength': 12,
            'dexterity': 12,
            'constitution': 12,
            'intelligence': 8,
            'wisdom': 10,
            'charisma': 8
        }
    },
    1/4: {
        'max-hp': '5d8',
        'challenge_rating': 0.25,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '1d8+1',
        'base_stat': {
            'strength': 14,
            'dexterity': 12,
            'constitution': 13,
            'intelligence': 8,
            'wisdom': 11,
            'charisma': 9
        }
    },
    1/2: {
        'max-hp': '8d8',
        'challenge_rating': 0.5,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '2d6+2',
        'base_stat': {
            'strength': 16,
            'dexterity': 12,
            'constitution': 14,
            'intelligence': 8,
            'wisdom': 11,
            'charisma': 10
        }
    },
    1: {
        'max-hp': '12d8+24',
        'challenge_rating': 1,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '2d8+3',
        'base_stat': {
            'strength': 16,
            'dexterity': 12,
            'constitution': 15,
            'intelligence': 8,
            'wisdom': 12,
            'charisma': 10
        }
    },
    2: {
        'max-hp': '14d8+30',
        'challenge_rating': 2,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '2d12+5',
        'base_stat': {
            'strength': 18,
            'dexterity': 12,
            'constitution': 16,
            'intelligence': 8,
            'wisdom': 12,
            'charisma': 11
        }
    },
    3: {
        'max-hp': '16d8+40',
        'challenge_rating': 3,
        'proficiency_bonus': 2,
        'armor_class': 13,
        'damage': '4d8+6',
        'base_stat': {
            'strength': 19,
            'dexterity': 12,
            'constitution': 17,
            'intelligence': 9,
            'wisdom': 13,
            'charisma': 12
        }
    },
    4: {
        'max-hp': '18d8+50',
        'challenge_rating': 4,
        'proficiency_bonus': 2,
        'armor_class': 14,
        'damage': '4d10+8',
        'base_stat': {
            'strength': 20,
            'dexterity': 13,
            'constitution': 18,
            'intelligence': 10,
            'wisdom': 14,
            'charisma': 13
        }
    },
    5: {
        'max-hp': '20d8+60',
        'challenge_rating': 5,
        'proficiency_bonus': 3,
        'armor_class': 15,
        'damage': '5d10+10',
        'base_stat': {
            'strength': 22,
            'dexterity': 14,
            'constitution': 19,
            'intelligence': 10,
            'wisdom': 15,
            'charisma': 14
        }
    },
    6: {
        'max-hp': '22d8+70',
        'challenge_rating': 6,
        'proficiency_bonus': 3,
        'armor_class': 15,
        'damage': '5d12+10',
        'base_stat': {
            'strength': 23,
            'dexterity': 14,
            'constitution': 20,
            'intelligence': 11,
            'wisdom': 16,
            'charisma': 15
        }
    },
    7: {
        'max-hp': '24d8+80',
        'challenge_rating': 7,
        'proficiency_bonus': 3,
        'armor_class': 15,
        'damage': '6d12+12',
        'base_stat': {
            'strength': 24,
            'dexterity': 14,
            'constitution': 21,
            'intelligence': 12,
            'wisdom': 17,
            'charisma': 16
        }
    },
    8: {
        'max-hp': '26d8+90',
        'challenge_rating': 8,
        'proficiency_bonus': 3,
        'armor_class': 16,
        'damage': '7d12+15',
        'base_stat': {
            'strength': 25,
            'dexterity': 15,
            'constitution': 22,
            'intelligence': 13,
            'wisdom': 18,
            'charisma': 17
        }
    },
    9: {
        'max-hp': '28d8+100',
        'challenge_rating': 9,
        'proficiency_bonus': 4,
        'armor_class': 16,
        'damage': '8d12+18',
        'base_stat': {
            'strength': 26,
            'dexterity': 15,
            'constitution': 23,
            'intelligence': 14,
            'wisdom': 19,
            'charisma': 18
        }
    },
    10: {
        'max-hp': '30d8+110',
        'challenge_rating': 10,
        'proficiency_bonus': 4,
        'armor_class': 17,
        'damage': '9d12+20',
        'base_stat': {
            'strength': 28,
            'dexterity': 16,
            'constitution': 24,
            'intelligence': 15,
            'wisdom': 20,
            'charisma': 19
        }
    }
}
monsters = {
    'wolf':{
        'name': 'wolf',
        'hp': None,
        'max-hp': None,
        'challenge_rating': 0,
        'location': 'лес',
        'proficiency_bonus': 0, #бонус мастерства
        'resistances': [],  #бонус сопротивление
        'vulnerability':[],  #бонус уязвимость
        'armor_class': 'natural armor',
        'damage': None,
        'base_stat':{
            'strength ': None,     
            'dexterity': None,
            'constitution': None,
            'intelligence': None,
            'wisdom': None,
            'charisma': None
        },
    }
}