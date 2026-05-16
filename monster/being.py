from armor.armor import armor_templates
cr_templates = {
  0: {
    "max_hp": "1d8",
    "challenge_rating": 0,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "1d4"
    },
    "base_stat": {
      "strength": 10,
      "dexterity": 12,
      "constitution": 10,
      "intelligence": 6,
      "wisdom": 10,
      "charisma": 8
    }
  },
  0.125: {
    "max_hp": "2d8",
    "challenge_rating": 0.125,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "1d6"
    },
    "base_stat": {
      "strength": 12,
      "dexterity": 13,
      "constitution": 12,
      "intelligence": 6,
      "wisdom": 10,
      "charisma": 8
    }
  },
  0.25: {
    "max_hp": "2d6",
    "challenge_rating": 0.25,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "1d6"
    },
    "base_stat": {
      "strength": 13,
      "dexterity": 14,
      "constitution": 12,
      "intelligence": 6,
      "wisdom": 10,
      "charisma": 8
    }
  },
  0.5: {
    "max_hp": "2d8",
    "challenge_rating": 0.5,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "1d12"
    },
    "base_stat": {
      "strength": 14,
      "dexterity": 12,
      "constitution": 14,
      "intelligence": 7,
      "wisdom": 11,
      "charisma": 9
    }
  },
  1: {
    "max_hp": "5d8",
    "challenge_rating": 1,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "2d8"
    },
    "base_stat": {
      "strength": 15,
      "dexterity": 12,
      "constitution": 14,
      "intelligence": 7,
      "wisdom": 11,
      "charisma": 9
    }
  },
  2: {
    "max_hp": "7d10",
    "challenge_rating": 2,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "2d8"
    },
    "base_stat": {
      "strength": 18,
      "dexterity": 10,
      "constitution": 16,
      "intelligence": 5,
      "wisdom": 7,
      "charisma": 7
    }
  },
  3: {
    "max_hp": "9d8",
    "challenge_rating": 3,
    "proficiency_bonus": 2,
    "armor_class": 13,
    "attack": {
      "dice_string": "1d8"
    },
    "base_stat": {
      "strength": 16,
      "dexterity": 13,
      "constitution": 14,
      "intelligence": 10,
      "wisdom": 11,
      "charisma": 10
    }
  },
  4: {
    "max_hp": "10d10",
    "challenge_rating": 4,
    "proficiency_bonus": 2,
    "armor_class": 14,
    "attack": {
      "dice_string": "2d8"
    },
    "base_stat": {
      "strength": 21,
      "dexterity": 8,
      "constitution": 17,
      "intelligence": 6,
      "wisdom": 10,
      "charisma": 8
    }
  },
  5: {
    "max_hp": "8d10",
    "challenge_rating": 5,
    "proficiency_bonus": 3,
    "armor_class": 15,
    "attack": {
      "dice_string": "2d6"
    },
    "base_stat": {
      "strength": 18,
      "dexterity": 13,
      "constitution": 20,
      "intelligence": 7,
      "wisdom": 9,
      "charisma": 7
    }
  },
  6: {
    "max_hp": "12d10",
    "challenge_rating": 6,
    "proficiency_bonus": 3,
    "armor_class": 15,
    "attack": {
      "dice_string": "2d6"
    },
    "base_stat": {
      "strength": 19,
      "dexterity": 11,
      "constitution": 19,
      "intelligence": 3,
      "wisdom": 14,
      "charisma": 10
    }
  },
  7: {
    "max_hp": "13d8",
    "challenge_rating": 7,
    "proficiency_bonus": 3,
    "armor_class": 15,
    "attack": {
      "dice_string": "2d10"
    },
    "base_stat": {
      "strength": 19,
      "dexterity": 16,
      "constitution": 18,
      "intelligence": 14,
      "wisdom": 12,
      "charisma": 15
    }
  },
  8: {
    "max_hp": "12d12",
    "challenge_rating": 8,
    "proficiency_bonus": 3,
    "armor_class": 16,
    "attack": {
      "dice_string": "3d12"
    },
    "base_stat": {
      "strength": 23,
      "dexterity": 9,
      "constitution": 21,
      "intelligence": 9,
      "wisdom": 10,
      "charisma": 12
    }
  },
  9: {
    "max_hp": "13d12",
    "challenge_rating": 9,
    "proficiency_bonus": 4,
    "armor_class": 16,
    "attack": {
      "dice_string": "6d6"
    },
    "base_stat": {
      "strength": 25,
      "dexterity": 9,
      "constitution": 23,
      "intelligence": 10,
      "wisdom": 14,
      "charisma": 13
    }
  },
  10: {
    "max_hp": "17d10",
    "challenge_rating": 10,
    "proficiency_bonus": 4,
    "armor_class": 17,
    "attack": {
      "dice_string": "3d8"
    },
    "base_stat": {
      "strength": 22,
      "dexterity": 9,
      "constitution": 20,
      "intelligence": 3,
      "wisdom": 11,
      "charisma": 1
    }
  }
}
monsters = {
    'wolf':{
        'name': 'wolf',
        'hp': None,
        'max_hp': None,
        'challenge_rating': 0,
        'location': 'лес',
        'proficiency_bonus': 0, #бонус мастерства
        'resistances': [],  #бонус сопротивление
        'vulnerability':[],  #бонус уязвимость
        'armor_class': None,
        'type_armor': 'natural armor',
        'armor': armor_templates['narutal_armor'],
        'bonus_shield':0,
        'attack': {                         # аналог оружия
            'dice_string': None,    
            'type_damage': 'piercing',
            'mod_stat': 'strength'
        },
        'base_stat':{
            'strength ': None,     
            'dexterity': None,
            'constitution': None,
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
        }
    }
}