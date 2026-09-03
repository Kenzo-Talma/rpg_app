import json

from database.database_lib import (create_table, replace_row, 
                                   replace_value, return_single_row, 
                                   return_single_column)


class Entity():
    def __init__(self, data_base_location):
        self.data_base_location :str = data_base_location
        self.name :str = str()
        self.entity_type :str = str()
        self.size :str = str()
        self.entity_HP :int = 10
        self.temp_HP:int = 0
        self.description :str = str()

        self.entity_dict :dict = {
            "entity_name": self.name,
            "HP": self.entity_HP,
            "temp_HP": self.temp_HP,
            "description": self.description,
            "type": self.entity_type,
            "size": self.size,
        }

    def take_damage(self, damage_value :int):
        self.entity_HP -= damage_value

    def heal(self, heal_value :int):
        self.entity_HP += heal_value

    
class PlayableCharacter(Entity):
    character_count :int = int()
    def __init__(self):
        super().__init__("DnD")
        self.stat_dict :dict = {
            "strenght": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
        self.character_id :int = int()
        self.entity_dict["character_id"] = self.character_id
        self.entity_dict["stats"] = self.stat_dict
        self.competence_dict :dict = dict()
        self.entity_dict["competences"] = self.competence_dict
        self.money_dict :dict = {
            "platinium": 0,
            "gold": 0,
            "silver": 0,
            "copper": 0
        }
        self.entity_dict["money"] = self.money_dict
        self.equipment_dict :dict = dict()
        self.entity_dict["equipment"] = self.equipment_dict
        self.spell_dict :dict = dict()
        self.entity_dict["spells"] = self.spell_dict

        self.count_saved_characters()


    @staticmethod
    def count_saved_characters():
        PlayableCharacter.character_count = len(
            return_single_column("DnD", "character_table", "character_id"))


    def new_character(self):
        self.character_id = int(PlayableCharacter.character_count)
        self.save_character()


    def open_character(character_id :int):
        return_single_row("DnD", "character_table", 0)

    def save_character(self):
        create_table(
            self.data_base_location,
            "character_table",
            return_template(),
            force=False)

        character_dict :dict= dict(self.entity_dict)

        del character_dict["stats"]

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
        "type",
        "entity_name",
        "class",
        "specie",
        "size",
        "alignment",
        "description",
        "HP",
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

# test = PlayableCharacter()
# print(test.character_count)
# test.save_character()
# test.count_saved_characters()
# test.update_value("charisma", 20)
# test.new_character()
