from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                              QFrame, QLineEdit, QScrollArea, QSpinBox)
from PySide6.QtCore import Qt

from core.entity_lib import playable_character


class CharacterSheet(QWidget, playable_character):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self, edit_mode :bool=False):
        """
        initialise character sheet ui

        :param edit_mode: (bool) create the ui in edit mode, default False
        """
        # create main layout and add it to the class widget
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # get test stat dict
        stat_dict = stat_test()
        identity_dict = id_test()
        fight_dict = fight_test()
        competence_dict = competences_test()

        # make identity ui
        self.identity_ui(identity_dict, edit_mode=edit_mode)
        self.main_layout.addWidget(self.identity_widget)

        # make fight
        self.fight_ui(fight_dict, edit_mode=edit_mode)
        self.main_layout.addWidget(self.fight_widget)

        # make stat sheet ui
        self.stat_sheet_ui(stat_dict, edit_mode=edit_mode)
        self.main_layout.addWidget(self.stat_sheet_widget)

        # make stat sheet ui
        self.competence_sheet_ui(competence_dict, edit_mode=True)
        self.main_layout.addWidget(self.competence_sheet_widget)


    def identity_ui(
            self, 
            identity_dict :dict, 
            edit_mode :bool=False):
        """
        make character id sheet using given stat dictionnary

        :param identity_dict: (dict) stat dictionnary
        :param edit_mode: (bool) create the ui in edit mode, default False
        """
        # main widget and layout
        self.identity_widget = QFrame()
        self.identity_widget.setFrameStyle(2)

        identity_layout = QVBoxLayout()
        identity_layout.setContentsMargins(5, 5, 5, 5)
        self.identity_widget.setLayout(identity_layout)

        if edit_mode:
            # name label
            name_label = QLineEdit(identity_dict["name"])

            # other data line edit in edit mode
            main_info_widget = QWidget()
            main_info_layout = QHBoxLayout()
            main_info_widget.setLayout(main_info_layout)
            for n, info in enumerate(identity_dict):
                if not n == 0:
                    info_line_edit = QLineEdit(identity_dict[info])
                    main_info_layout.addWidget(info_line_edit)
        else:
            # name label
            name_label = QLabel(identity_dict["name"])

            # info label in non edit mode and read mode
            info_list = [
                identity_dict[key] for n, key in enumerate(identity_dict) 
                if not n==0
            ]
            info_str = ", ".join(info_list)
            main_info_label = QLabel(info_str)

        # add name and infos to identity layout
        identity_layout.addWidget(name_label, alignment=Qt.AlignCenter)
        identity_layout.addWidget(main_info_label, alignment=Qt.AlignCenter)


    def fight_ui(
            self, 
            fight_dict :dict, 
            edit_mode :bool=False):
        """
        make fight info sheet using given stat dictionnary

        :param fight_dict: (dict) stat dictionnary
        :param edit_mode: (bool) create the ui in edit mode, default False
        """
        # main widget and layout
        self.fight_widget = QFrame()
        self.fight_widget.setFrameStyle(2)
        main_fight_layout = QVBoxLayout()
        main_fight_layout.setContentsMargins(5, 5, 5, 5)
        self.fight_widget.setLayout(main_fight_layout)

        # name label
        name_label = QLabel("fight info")
        main_fight_layout.addWidget(name_label, alignment=Qt.AlignCenter)
        
        # fight stats widget
        fight_stat_widget = QWidget()
        main_fight_layout.addWidget(fight_stat_widget, alignment=Qt.AlignCenter)
        fight_stat_layout = QHBoxLayout()
        fight_stat_layout.setContentsMargins(0, 0, 0, 0)
        fight_stat_widget.setLayout(fight_stat_layout)

        # stat loop
        for n, stat in enumerate(fight_dict):
            # new stat info column each 2 stat
            if n % 2 == 0:
                stat_column_widget = QFrame()
                stat_column_widget.setFrameStyle(2)
                fight_stat_layout.addWidget(stat_column_widget, alignment=Qt.AlignCenter)

                stat_column_layout = QVBoxLayout()
                stat_column_layout.setContentsMargins(5, 5, 5, 5)
                stat_column_widget.setLayout(stat_column_layout)

            # stat info
            stat_widget = QFrame()
            stat_column_layout.addWidget(stat_widget, alignment=Qt.AlignCenter)

            stat_layout = QVBoxLayout()
            stat_layout.setContentsMargins(0, 0, 0, 0)
            stat_widget.setLayout(stat_layout)

            # stat name
            stat_name = QLabel(stat)
            stat_layout.addWidget(stat_name, alignment=Qt.AlignCenter)

            # stat info
            if edit_mode:
                stat_label = QLineEdit(str(fight_dict[stat]))
            else:
                stat_label = QLabel(str(fight_dict[stat]))
            stat_layout.addWidget(stat_label, alignment=Qt.AlignCenter)


    def stat_sheet_ui(
            self, 
            stat_dict :dict, 
            edit_mode :bool=False):
        """
        make stat sheet using given stat dictionnary

        :param stat_dict: (dict) stat dictionnary
        :param edit_mode: (bool) create the ui in edit mode, default False
        """
        # create main widget, layout and label
        self.stat_sheet_widget = QFrame()
        self.stat_sheet_widget.setFrameStyle(2)

        stat_name_layout = QVBoxLayout()
        stat_name_layout.setContentsMargins(5, 5, 5, 5)
        self.stat_sheet_widget.setLayout(stat_name_layout)

        sheet_name = QLabel("stat")
        stat_name_layout.addWidget(sheet_name, alignment=Qt.AlignCenter)

        stat_sheet_widget = QWidget()
        self.stat_sheet_layout = QHBoxLayout()
        stat_sheet_widget.setLayout(self.stat_sheet_layout)
        stat_name_layout.addWidget(stat_sheet_widget)
        
        # create stat layout for all stats
        for stat in stat_dict:
            # stat frame and layout
            stat_widget = QFrame()
            stat_layout = QVBoxLayout()
            stat_widget.setLayout(stat_layout)

            # stat name
            stat_name_label = QLabel(stat)
            stat_layout.addWidget(stat_name_label, alignment=Qt.AlignCenter)

            # stat value
            if edit_mode:
                stat_value = QLineEdit(str(stat_dict[stat]))
            else:
                stat_value = QLabel(str(stat_dict[stat]))
            stat_layout.addWidget(stat_value, alignment=Qt.AlignCenter)

            # add stat frame to main stat sheet
            self.stat_sheet_layout.addWidget(stat_widget)


    def competence_sheet_ui(
                self, 
                competence_dict :dict, 
                edit_mode :bool=False):
            """
            make competence sheet using given competence dictionnary
    
            :param competence_dict: (dict) competence dictionnary
            :param edit_mode: (bool) create the ui in edit mode, default False
            """
            # create main widget, layout and label
            self.competence_sheet_widget = QFrame()
            self.competence_sheet_widget.setFrameStyle(2)
    
            competence_sheet_layout = QVBoxLayout()
            competence_sheet_layout.setContentsMargins(5, 5, 5, 5)
            self.competence_sheet_widget.setLayout(competence_sheet_layout)

            # name widget
            competence_title = QLabel("competences")
            competence_sheet_layout.addWidget(competence_title)

            # competences scroll areay settings
            competence_scroll_area = QScrollArea()
            competence_scroll_area.setMinimumHeight(200)
            competence_scroll_area.setFrameStyle(2)

            # competences widget
            competence_scroll_widget = QFrame()
            competence_scroll_area.setWidget(competence_scroll_widget)
            competence_scroll_area.setWidgetResizable(True)
            competence_sheet_layout.addWidget(competence_scroll_area)

            # competences layout
            competence_scroll_layout = QVBoxLayout()
            competence_scroll_widget.setLayout(competence_scroll_layout)

            for competence in competence_dict:
                # competence widget and layout
                competence_widget = QWidget()
                competence_scroll_layout.addWidget(competence_widget)
                competence_layout = QHBoxLayout()
                competence_layout.setContentsMargins(0, 0, 0, 0)
                competence_widget.setLayout(competence_layout)

                # competence name
                competence_name = QLabel(competence)
                competence_layout.addWidget(competence_name)

                # competence value
                if edit_mode:
                    competence_value = QSpinBox()
                    competence_value.setRange(-100, 100)
                    competence_value.setValue(competence_dict[competence])
                else:
                    competence_value = QLabel(str(competence_dict[competence]))
                competence_layout.addWidget(competence_value)


################################################################################
# test
################################################################################

 # stats test values
def fight_test():
    return {
        "HP": 25,
        "temp HP": 3,
        "initialive": 12,
        "speed": 30,
        "class armor": 15,
        "inspiration": 1
    }

def id_test():
    return {
        "name": "Lila Van Gref",
        "class": "rogue",
        "species": "half-elf",
        "size": "medium",
        "alignment": "neutral evil",
    }

def stat_test():
    return {
        "strenght": 15,
        "dexterity": 13,
        "constitution": 16,
        "intelligence": 11,
        "wisdom": 8,
        "charisma": 9
    }

def competences_test():
    return {
        "acrobacies": 1,
        "acrane": 0,
        "athletisme": 3,
        "stealth": 4,
        "animal handling": -2,
        "slight of hand": 6,
        "history": 1,
        "intimidation": 0,
        "intuition": 3,
        "investigation": 5,
        "medecine": 2,
        "nature": 1,
        "perception": 0,
        "persuasion": 2,
        "acrobacies": 4,
        "acrobacies": 0
    }
