import json

from core.database.database_lib import (create_table, replace_row, 
                                   replace_value, return_single_data, 
                                   return_single_column)


class Entity():
    def __init__(self, data_base_location):
        self.data_base_location :str = data_base_location
        self.entity_name :str = str()
        self.entity_type :str = str()
        self.size :str = str()
        self.initiative :int = int()
        self.speed :int = int()
        self.entity_HP :int = int()
        self.temp_HP:int = int()
        self.description :str = str()

    def take_damage(self, damage_value :int):
        self.entity_HP -= damage_value

    def heal(self, heal_value :int):
        self.entity_HP += heal_value

    
class PlayableCharacter(Entity):
    character_count :int = int()
    def __init__(self):
        super().__init__("DnD")

        self.character_id :int = int()
        self.stat_dict :dict = dict
        self.character_class :str = str()
        self.character_specie :str = str()
        self.alignment :str = str()
        self.competences :dict = dict()
        self.class_armor :int = int()
        self.inspiration :int = int()
        self.money :dict = dict()
        self.equipment :dict = dict()
        self.spells :dict = dict()

        create_table(
            self.data_base_location,
            "character_table",
            return_template(),
            force=False)

        self.count_saved_characters()


    @staticmethod
    def count_saved_characters():
        PlayableCharacter.character_count = len(
            return_single_column("DnD", "character_table", "character_id"))


    def new_character(self):
        self.character_id = int(PlayableCharacter.character_count)
        self.save_character()


    def open_character(self, character_id :int):
        table_info :list = ("DnD", "character_table")
        id_info_list :list = ["character_id", character_id]

        self.stat_dict = {
            "strenght": int(return_single_data(*table_info, "strenght", 
                                           id_info_list)),
            "dexterity": int(return_single_data(*table_info, "dexterity", 
                                           id_info_list)),
            "constitution": int(return_single_data(*table_info, "constitution",
                                           id_info_list)),
            "intelligence": int(return_single_data(*table_info, "intelligence",
                                           id_info_list)),
            "wisdom": int(return_single_data(*table_info, "wisdom", 
                                           id_info_list)),
            "charisma": int(return_single_data(*table_info, "charisma", 
                                           id_info_list))
        }

        for data in return_template():
            if not data in self.stat_dict:
                data_string :str = return_single_data(*table_info,
                                                  data, id_info_list)

                try:
                    data_value = eval(data_string)
                except:
                    data_value = data_string

                setattr(self, data, data_value)


    def save_character(self):
        character_dict :dict= dict()

        for data in return_template():
            if not data in self.stat_dict:
                character_dict[data] = getattr(self, data)

        character_dict["strenght"] = self.stat_dict["strenght"]
        character_dict["dexterity"] = self.stat_dict["dexterity"]
        character_dict["constitution"] = self.stat_dict["constitution"]
        character_dict["intelligence"] = self.stat_dict["intelligence"]
        character_dict["wisdom"] = self.stat_dict["wisdom"]
        character_dict["charisma"] = self.stat_dict["charisma"]

        replace_row(self.data_base_location, "character_table", character_dict)


    def update_value(self, info_name, info_value):
        replace_value(
            self.data_base_location,
            "character_table",
            ["character_id", self.character_id],
            info_name,
            info_value)
        


################################################################################
# test
################################################################################

def return_template():
    return [
        "character_id",
        "entity_type",
        "entity_name",
        "character_class",
        "character_specie",
        "size",
        "alignment",
        "description",
        "entity_HP",
        "temp_HP",
        "initiative",
        "speed",
        "class_armor",
        "inspiration",
        "strenght",
        "dexterity",
        "constitution",
        "intelligence",
        "wisdom",
        "charisma",
        "competences",
        "money",
        "equipment",
        "spells"
    ]

# raise TypeError

"""test = PlayableCharacter()
test.entity_name = "new character"
test.entity_type = "character"
test.size = "M"
test.initiative = 0
test.speed = 30
test.entity_HP = 10
test.temp_HP = 0
test.stat_dict = {
            "strenght": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
test.description = "describe your character"
test.character_class = "fighter"
test.character_specie = "tiefling"
test.alignment = "true neutral"
test.competences = {
        "acrobacies": 0,
        "acrane": 0,
        "athletisme": 0,
        "stealth": 0,
        "animal handling": 0,
        "slight of hand": 0,
        "history": 0,
        "intimidation": 0,
        "intuition": 0,
        "investigation": 0,
        "medecine": 0,
        "nature": 0,
        "perception": 0,
        "persuasion": 0,
        "acrobacies": 0,
        "acrobacies": 0
    }
test.class_armor = 10
test.inspiration = 0
test.money = {
            "platinium": 0,
            "gold": 0,
            "silver": 0,
            "copper": 0
        }
test.equipment = {
        "short sword": ["damage 1d8"],
        "knife": ["damage 1d6", "poisonous"],
        "rope": None,
        "healing potion": ["heal 2d8"]
    }
test.spells = {
        "lv0": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv1": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv2": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv3": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv4": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv5": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv6": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv7": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv8": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        },
        "lv9": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            }
        }
    }

test.save_character()"""
