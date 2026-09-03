from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                              QFrame, QLineEdit, QScrollArea, QSpinBox, 
                              QPushButton, QDialog, QMenuBar, QMenu)
from PySide6.QtCore import Qt
from typing import Callable

from core.entity_lib import PlayableCharacter


class CharacterSheet(QWidget):
    def __init__(self):
        self.character_id :int = int()
        super().__init__()
        self.edit_mode :bool = False
        self.player_mode :bool = True

        self.mode_list :dict = ["edit", "player", "read"]

        # create main layout and add it to the class widget
        self.main_layout :QVBoxLayout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # create main menubar
        self.menu_bar = QMenuBar()
        self.main_layout.setMenuBar(self.menu_bar)

        self.make_ui()

        # make switch ui
        self.switch_mode_ui()


    def open_character_sheet(self):
        if self.character_id:
            self.character :PlayableCharacter = PlayableCharacter(
                self.character_id)
            self.character.get_data


    def make_ui(self):
        """
        initialise character sheet ui

        :param self.edit_mode: (bool) create the ui in edit mode, default False
        """

        # get test stat dict
        stat_dict :dict = stat_test()
        identity_dict :dict = id_test()
        fight_dict :dict = fight_test()
        competence_dict :dict = competences_test()
        equipment_dict :dict = equipment_test()
        spell_dict :dict = spell_test()

        # make identity ui
        self.identity_ui(
            identity_dict)
        self.main_layout.addWidget(
            self.identity_widget, alignment=Qt.AlignCenter)

        # second row
        self.second_row_widget :QWidget = QWidget()
        self.main_layout.addWidget(self.second_row_widget)
        self.second_row_layout :QHBoxLayout = QHBoxLayout()
        self.second_row_widget.setLayout(self.second_row_layout)

        # make fight
        self.fight_ui(fight_dict)
        self.second_row_layout.addWidget(self.fight_widget)

        # make stat sheet ui
        self.stat_sheet_ui(stat_dict)
        self.second_row_layout.addWidget(self.stat_sheet_widget)

        # make competences sheet ui
        self.competence_sheet_ui(competence_dict)
        self.second_row_layout.addWidget(self.competence_sheet_widget)

        # third row
        self.third_row_widget :QWidget = QWidget()
        self.main_layout.addWidget(self.third_row_widget)
        self.third_row_layout :QHBoxLayout = QHBoxLayout()
        self.third_row_widget.setLayout(self.third_row_layout)

        # make equipement sheet ui
        self.equipment_sheet_ui(equipment_dict)
        self.third_row_layout.addWidget(self.equipment_sheet_widget)

        # make spell sheet ui
        self.spell_sheet_ui(spell_dict)
        self.third_row_layout.addWidget(self.spell_sheet_widget)


    # identity function
    def identity_ui(
            self, 
            identity_dict :dict):
        """
        make character id sheet using given stat dictionnary

        :param identity_dict: (dict) stat dictionnary
        :param self.edit_mode: (bool) create the ui in edit mode, default False
        """
        # main widget and layout
        self.identity_widget , identity_layout = self.make_frame()

        if self.edit_mode:
            # name label
            name_label :QLineEdit = QLineEdit(identity_dict["name"])
            identity_layout.addWidget(name_label, alignment=Qt.AlignCenter)

            # other data line edit in edit mode
            main_info_widget :QWidget = QWidget()
            identity_layout.addWidget(main_info_widget)

            main_info_layout :QHBoxLayout = QHBoxLayout()
            main_info_widget.setLayout(main_info_layout)

            for n, info in enumerate(identity_dict):
                if not n == 0:
                    info_line_edit :QLineEdit = QLineEdit(identity_dict[info])
                    main_info_layout.addWidget(info_line_edit)
        else:
            # name label
            name_label :QLabel = QLabel(identity_dict["name"])

            # info label in non edit mode and read mode
            info_list :list = [
                identity_dict[key] for n, key in enumerate(identity_dict) 
                if not n==0
            ]
            info_str :str = ", ".join(info_list)
            main_info_label :QLabel = QLabel(info_str)

            # add name and infos to identity layout
            identity_layout.addWidget(name_label, alignment=Qt.AlignCenter)
            identity_layout.addWidget(main_info_label, alignment=Qt.AlignCenter)


    # fight fuction
    def fight_ui(
            self, 
            fight_dict :dict):
        """
        make fight info sheet using given stat dictionnary

        :param fight_dict: (dict) stat dictionnary
        :param self.edit_mode: (bool) create the ui in edit mode, default False
        :param self.player_mode: (bool) create the ui in player mode, default True
        """
        # main widget and layout
        self.fight_widget, main_fight_layout = \
            self.make_frame(name="fight_info")
        
        # fight stats widget
        fight_stat_widget :QWidget = QWidget()
        main_fight_layout.addWidget(fight_stat_widget, alignment=Qt.AlignCenter)
        fight_stat_layout :QVBoxLayout = QVBoxLayout()
        fight_stat_layout.setContentsMargins(0, 0, 0, 0)
        fight_stat_widget.setLayout(fight_stat_layout)

        # stat loop
        for n, stat in enumerate(fight_dict):
            # new stat info column each 2 stat
            if n % 2 == 0:
                stat_column_widget :QFrame = QFrame()
                stat_column_widget.setFrameStyle(2)
                fight_stat_layout.addWidget(stat_column_widget, alignment=Qt.AlignCenter)

                stat_column_layout :QVBoxLayout = QVBoxLayout()
                stat_column_layout.setContentsMargins(5, 5, 5, 5)
                stat_column_widget.setLayout(stat_column_layout)

            # stat info
            stat_widget :QFrame = QFrame()
            stat_column_layout.addWidget(stat_widget, alignment=Qt.AlignCenter)

            stat_layout :QVBoxLayout = QVBoxLayout()
            stat_layout.setContentsMargins(0, 0, 0, 0)
            stat_widget.setLayout(stat_layout)

            # stat name
            stat_name :QLabel = QLabel(stat)
            stat_layout.addWidget(stat_name, alignment=Qt.AlignCenter)

            # stat info
            if self.edit_mode:
                stat_label :QSpinBox = QSpinBox()
                stat_label.setValue(fight_dict[stat])
            elif stat in ["HP", "temp HP"] and self.player_mode:
                stat_label :QSpinBox = QSpinBox()
                stat_label.setValue(fight_dict[stat])
            else:
                stat_label :QLabel = QLabel(str(fight_dict[stat]))
            stat_layout.addWidget(stat_label, alignment=Qt.AlignCenter)


    # stat function
    def stat_sheet_ui(
            self, 
            stat_dict :dict):
        """
        make stat sheet using given stat dictionnary

        :param stat_dict: (dict) stat dictionnary
        :param self.edit_mode: (bool) create the ui in edit mode, default False
        :param self.player_mode: (bool) create the ui in player mode, default True
        """
        # create main widget, layout and label
        self.stat_sheet_widget, stat_name_layout = \
            self.make_frame(name="stat")

        stat_sheet_widget :QWidget = QWidget()
        self.stat_sheet_layout :QVBoxLayout = QVBoxLayout()
        stat_sheet_widget.setLayout(self.stat_sheet_layout)
        stat_name_layout.addWidget(stat_sheet_widget)
        
        # create stat layout for all stats
        for stat in stat_dict:
            # stat frame and layout
            stat_widget :QFrame = QFrame()
            stat_layout :QVBoxLayout = QVBoxLayout()
            stat_widget.setLayout(stat_layout)

            # stat name
            stat_name_label :QLabel = QLabel(stat)
            stat_layout.addWidget(stat_name_label, alignment=Qt.AlignCenter)

            # stat value
            if self.edit_mode or self.player_mode:
                stat_value :QSpinBox = QSpinBox()
                stat_value.setValue(stat_dict[stat])
            else:
                stat_value :QLabel = QLabel(str(stat_dict[stat]))
            stat_layout.addWidget(stat_value, alignment=Qt.AlignCenter)

            # add stat frame to main stat sheet
            self.stat_sheet_layout.addWidget(stat_widget)


    # competence function
    def competence_sheet_ui(
            self, 
            competence_dict :dict):
        """
        make competence sheet using given competence dictionnary
    
        :param competence_dict: (dict) competence dictionnary
        :param self.edit_mode: (bool) create the ui in edit mode, default False
        :param self.player_mode: (bool) create the ui in player mode, default True
        """
        # create main widget, layout and label
        self.competence_sheet_widget, competence_scroll_layout = \
            self.make_scroll_area(name="competences")

        for competence in competence_dict:
            # competence widget and layout
            competence_widget :QWidget = QWidget()
            competence_scroll_layout.addWidget(competence_widget)
            competence_layout :QHBoxLayout = QHBoxLayout()
            competence_layout.setContentsMargins(0, 0, 0, 0)
            competence_widget.setLayout(competence_layout)

            # competence name
            competence_name :QLabel = QLabel(competence)
            competence_layout.addWidget(competence_name)

            # competence value
            if self.edit_mode or self.player_mode:
                competence_value :QWidget = QSpinBox()
                competence_value.setRange(-100, 100)
                competence_value.setValue(competence_dict[competence])
            else:
                competence_value :QWidget = QLabel(str(competence_dict[competence]))
            competence_layout.addWidget(competence_value)

            # set widget size
            competence_widget.setFixedHeight(
                competence_widget.sizeHint().height())


    # equipment functions
    def equipment_sheet_ui(
            self, 
            equipment_dict :dict):
        """
        make equipment sheet using given equipment dictionnary
    
        :param equipmen_dict: (dict) equipment dictionnary
        :param self.edit_mode: (bool) create the ui in edit mode, default False
        :param self.player_mode: (bool) create the ui in player mode, default True
        """
        # create main widget and layout
        self.equipment_sheet_widget :QWidget = QWidget()
        self.equipment_sheet_layout :QVBoxLayout = QVBoxLayout()
        self.equipment_sheet_widget.setLayout(self.equipment_sheet_layout)
        self.equipment_sheet_layout.setContentsMargins(0, 0, 0, 0)

        # create money ui
        self.money_sheet_widget :QFrame = QFrame()
        self.equipment_sheet_layout.addWidget(self.money_sheet_widget)
        self.money_sheet_layout :QHBoxLayout = QHBoxLayout()
        self.money_sheet_layout.setContentsMargins(0, 0, 0, 0)
        self.money_sheet_widget.setLayout(self.money_sheet_layout)
        self.money_sheet_widget.setFrameStyle(2)

        for currency in equipment_dict["money"]:
            currency_widget :QWidget = QWidget()
            self.money_sheet_layout.addWidget(currency_widget)
            currency_layout :QVBoxLayout = QVBoxLayout()
            currency_widget.setLayout(currency_layout)

            currency_name :QLabel = QLabel(currency)
            currency_layout.addWidget(currency_name)
            currency_value :QLabel = QLabel(
                str(equipment_dict["money"][currency]))
            currency_layout.addWidget(currency_value)

        # create scroll area
        self.equipment_scroll_widget, self.equipment_scroll_layout = \
            self.make_scroll_area("equipment")
        self.equipment_sheet_layout.addWidget(self.equipment_scroll_widget)

        # make add button
        if self.edit_mode or self.player_mode:
            add_button_widget :QPushButton = QPushButton("add equipment")
            self.equipment_scroll_layout.addWidget(
                add_button_widget, alignment=Qt.AlignCenter)
            self.equipment_scroll_layout.setAlignment(
                add_button_widget, Qt.AlignTop)
            add_button_widget.clicked.connect(self.make_add_equimpent(
                "name",
                "damage",
                "infos"))

        # make equipment rows
        for equipment in equipment_dict:
            if equipment == "money":
                continue

            equipment_widget :QWidget = self.make_equipment_row(
                equipment, 
                equipment_dict[equipment])
            self.equipment_scroll_layout.addWidget(equipment_widget)


    def make_equipment_row(
            self, 
            name :str, 
            info_list :list=None) -> QWidget:
        """
        add a new row to equipment tab

        :param name: (str) name of the equipment
        :param info_list: (list) all others infos
        :return QWidget: new widget for the equipement tab
        """
        # create and set equipment widget
        equipment_widget :QWidget = QWidget()
        equipment_layout :QHBoxLayout = QHBoxLayout()
        equipment_layout.setContentsMargins(0, 0, 0, 0)
        equipment_widget.setLayout(equipment_layout)

        # name label
        if not name:
            return
        equipment_name :QLabel = QLabel(name)
        equipment_layout.addWidget(equipment_name, alignment=Qt.AlignLeft)

        # info lalel if it exist
        if info_list:
            # clean info list
            clean_list :list = list()
            for info in info_list:
                if info:
                    clean_list.append(str(info))

            # add widget
            equipment_info :QLabel = QLabel(
                ", ".join(clean_list), alignment=Qt.AlignRight)
            equipment_layout.addWidget(equipment_info)

        # remove button
        if self.edit_mode:
            remove_equipment :QPushButton = QPushButton("X")
            remove_equipment.setFixedWidth(50)
            equipment_layout.addWidget(remove_equipment, Qt.AlignLeft)
            remove_equipment.clicked.connect(self.make_delete_func(equipment_widget))

        # set widget size
        equipment_widget.setFixedHeight(
            equipment_widget.sizeHint().height())

        # return widget
        return equipment_widget


    def make_add_equimpent(
            self, 
            *args) -> Callable:
        """
        make function for the add equipment button
        """
        def add_equimpent():
            # get values
            value_dict :dict = dict()
            for value in args:
                value_dict[value] = None

            values = AddInfo(self, value_dict)
            values.exec_()
            if values.result == 0:
                pass

            # create equipment row
            value_list :str = [
                value_dict[key] for key in value_dict if not key=="name"]

            # add equipment widget to main equipment row
            equipment_widget :QWidget = self.make_equipment_row(
                name=value_dict["name"], 
                info_list = value_list
                )
            if equipment_widget:
                self.equipment_scroll_layout.addWidget(equipment_widget)
            
        return add_equimpent


    # spell function
    def spell_sheet_ui(
            self, 
            spell_dict :dict):
        """
        make spell sheet using given equipment dictionnary
    
        :param equipmen_dict: (dict) equipment dictionnary
        :param self.edit_mode: (bool) create the ui in edit mode, default False
        :param self.player_mode: (bool) create the ui in player mode, default True
        """
        # make main widget and layout
        self.spell_sheet_widget :QFrame = QFrame()
        self.spell_sheet_widget.setFrameStyle(2)
        self.spell_sheet_widget.setContentsMargins(5, 5, 5, 5)
        self.spell_sheet_layout :QVBoxLayout = QVBoxLayout()
        self.spell_sheet_widget.setLayout(self.spell_sheet_layout)

        # sheet title
        title :QLabel= QLabel("spell")
        self.spell_sheet_layout.addWidget(title, alignment=Qt.AlignCenter)

        # make secondary widget and layout
        spell_tab_widget :QWidget = QWidget()
        spell_tab_widget.setContentsMargins(0, 0, 0, 0)

        self.spell_sheet_layout.addWidget(spell_tab_widget)
        self.spell_tab_layout :QHBoxLayout = QHBoxLayout()
        spell_tab_widget.setLayout(self.spell_tab_layout)

        # make switch buttons
        self.previous_spell_button :QPushButton = QPushButton("<")
        self.previous_spell_button.clicked.connect(
            self.make_switch_spell_tab(previous=True))

        self.next_spell_button :QPushButton = QPushButton(">")
        self.next_spell_button.clicked.connect(
            self.make_switch_spell_tab(previous=False))

        # make levels tabs
        self.level_tabs_dict :dict = dict()
        self.level_layout_list :list = list()
        for i in range(10):
            if i % 2 == 0:
                # main level widget
                level_main_widget :QFrame = QFrame()
                level_main_widget.setContentsMargins(0, 0, 0, 0)

                level_main_widget.setFrameStyle(2)
                level_main_Layout :QHBoxLayout = QHBoxLayout()
                level_main_widget.setLayout(level_main_Layout)

                self.level_tabs_dict[str(int(i/2))] = (
                    level_main_widget, level_main_Layout)

            # level scroll area
            level_scroll_widget, level_scroll_Layout = \
                self.make_scroll_area(name=f"lv{i}")

            level_scroll_widget.setFrameStyle(0)
            level_scroll_widget.setContentsMargins(0, 0, 0, 0)
            level_main_Layout.addWidget(level_scroll_widget)
            self.level_layout_list.append(level_scroll_Layout)

            level_spell_dict :dict = spell_dict[f"lv{i}"]

            # make add button for edit mode
            if self.edit_mode:
                level_add_button :QPushButton = QPushButton("add")
                level_add_button.clicked.connect(
                    self.make_add_spell(
                        level_scroll_Layout,
                        "effect",
                        "description"
                    ))
                level_scroll_Layout.addWidget(level_add_button)

            # add aleardy known spells 
            for spell in level_spell_dict:
                # spell widget and layout
                spell_widget : QWidget = self.make_spell_row(
                    spell,
                    level_spell_dict[spell]["effect"],
                    level_spell_dict[spell]["description"])
                
                level_scroll_Layout.addWidget(
                    spell_widget, alignment=Qt.AlignTop)

        # add tabs to layout
        self.current_level_tab :int = 0

        self.spell_tab_layout.addWidget(
            self.previous_spell_button, alignment=Qt.AlignLeft)
        self.spell_tab_layout.setAlignment(
            self.previous_spell_button, Qt.AlignVCenter)

        for index in self.level_tabs_dict:
            self.spell_tab_layout.addWidget(
                self.level_tabs_dict[index][0], alignment=Qt.AlignHCenter)
            self.spell_tab_layout.setAlignment(
                self.level_tabs_dict[index][0], Qt.AlignVCenter)
            
            if not int(index) == 0:
                self.level_tabs_dict[index][0].setVisible(0)
            
        self.spell_tab_layout.addWidget(
            self.next_spell_button, alignment=Qt.AlignRight)
        self.spell_tab_layout.setAlignment(
            self.next_spell_button, Qt.AlignVCenter)


    def make_switch_spell_tab(self, previous :bool=True) -> Callable:
        """
        create and return a function to switch from a spell tab to another

        :param previous: switch to the previous or next tab
        :return switch spell_tab: function to switch tabs
        """
        def switch_spell_tab():
            # determine new tab value
            redraw :bool = False
            if previous and not self.current_level_tab == 0:
                previous_value :int = int(self.current_level_tab)
                self.current_level_tab -= 1
                redraw = True
            elif not previous and not self.current_level_tab == 4:
                previous_value :int = int(self.current_level_tab)
                self.current_level_tab += 1
                redraw = True

            # hide previous tab and show the new one
            if redraw:
                self.level_tabs_dict[str(previous_value)][0].setVisible(0)
                self.level_tabs_dict[
                    str(self.current_level_tab)][0].setVisible(1)

        return switch_spell_tab    


    def make_spell_row(
            self, 
            spell_name :str, 
            spell_effect :str, 
            spell_description :str=None) -> QWidget:
        """
        function to create and return a widget containing the new spell info

        :param spell_name: name of the spell
        :param spell_effect: effect of th spell
        :param spell_description: spell's in depth description
        """
        spell_widget :QWidget = QWidget()
        spell_layout :QHBoxLayout = QHBoxLayout()
        spell_widget.setLayout(spell_layout)

        # name
        spell_name_widget :QLabel = QLabel(spell_name)
        spell_layout.addWidget(spell_name_widget, Qt.AlignLeft)

        # spell effect
        spell_effect_widget :QLabel = QLabel(spell_effect)
        spell_layout.addWidget(spell_effect_widget, Qt.AlignRight)

        # spell details button
        spell_button :QPushButton = QPushButton("?")
        spell_layout.addWidget(spell_button, Qt.AlignRight)

        # remove spell button
        if self.edit_mode:
            remove_button :QPushButton = QPushButton("X")
            spell_layout.addWidget(remove_button, Qt.AlignLeft)
            remove_button.clicked.connect(self.make_delete_func(spell_widget))

        spell_widget.setFixedHeight(spell_widget.sizeHint().height())

        return spell_widget
    

    def make_add_spell(
            self, 
            spell_scroll_tab :QVBoxLayout, 
            *args) -> Callable:
            """
            make function for the add spell button

            :param spell_scroll_tab: scroll layout to add the 
                widget to
            :return add_spell: add spell function
            """
            def add_spell():
                # get values
                value_dict :dict = dict()
                for value in args:
                    value_dict[value] = None
    
                values :AddInfo = AddInfo(self, value_dict)
                values.exec_()
                if values.result == 0:
                    pass
    
                # make spell row
                new_spell_widget :QWidget = self.make_spell_row(
                    value_dict["name"],
                    value_dict["effect"],
                    value_dict["description"]
                )

                spell_scroll_tab.addWidget(
                    new_spell_widget, alignment=Qt.AlignTop)

            # return functions    
            return add_spell


    # make ui function
    def make_frame(self, name=None) -> QFrame:
        """
        make and return a QFrame 

        :param name: name to give to the frame
        """
        # main widget and layout
        main_widget :QFrame= QFrame()
        main_widget.setFrameStyle(2)

        main_layout :QVBoxLayout= QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_widget.setLayout(main_layout)

        # name widget
        if name:
            title :QLabel= QLabel(name)
            main_layout.addWidget(title, alignment=Qt.AlignCenter)

        # return main widget and layout
        return main_widget, main_layout


    def make_scroll_area(
            self, 
            name :str=None) -> QFrame :
        """
        make and return a QFrame containing a scroll area

        :param name: name to give to the frame
        :return main_widget: main frame widget
        :return scroll_layout: layout of the scroll area
        """
        # create main widget, layout and label
        main_widget :QFrame= QFrame()
        main_widget.setFrameStyle(2)
            
        main_layout :QVBoxLayout= QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_widget.setLayout(main_layout)
        
        # name widget
        if name:
            title :QLabel = QLabel(name)
            main_layout.addWidget(title, alignment=Qt.AlignCenter)
        
        # competences scroll areay settings
        scroll_area :QScrollArea = QScrollArea()
        scroll_area.setMinimumHeight(200)
        scroll_area.setFrameStyle(2)
        
        # competences widget
        scroll_widget :QFrame = QFrame()
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        
        # competences layout
        scroll_layout :QVBoxLayout = QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)

        # return scroll area main widget and scroll layout
        return main_widget, scroll_layout


    # delete ui function
    def make_delete_func(self, widget :QWidget):
        """
        make and return a function to delete given widget

        :param widget: widget to detete
        :return delete_func: fuction to delete xidget
        """
        def delete_func():
            widget.deleteLater()

        return delete_func


    # switch mode
    def switch_mode_ui(self):
        """
        make switch menu bar to switch modes
        """
        # create main widget
        if self.edit_mode:
            current_mode = "edit"
        elif self.player_mode:
            current_mode = "player"
        else:
            current_mode = "read"
        
        self.switch_mode_widget :QPushButton = QPushButton(current_mode)

        # create menu
        self.switch_mode_menu :QMenu = QMenu("mode")
        self.menu_bar.addMenu(self.switch_mode_menu)

        # create menu option
        for mode in self.mode_list:
            self.switch_mode_menu.addAction(mode, self.make_switch_action(mode))
            # self.switch_mode_menu.addSeparator()


    def make_switch_action(self, mode:str) -> Callable:
        """
        make and return a function to switch mode

        :param mode: mode to switch to
        :return switch_mode: function to switch mode
        """
        def switch_mode():
            if mode == "edit":
                self.edit_mode = True
                self.player_mode = False
            elif mode == "player":
                self.edit_mode = False
                self.player_mode = True
            else:
                self.edit_mode = False
                self.player_mode = False

            for i in range(self.main_layout.count()):
                self.main_layout.itemAt(i).widget().deleteLater()

            self.make_ui()
            self.resize(self.sizeHint())

        return switch_mode


class AddInfo(QDialog):
    def __init__(self, parent :QWidget, value_dict :dict):
        super().__init__(parent=parent)

        self.value_dict = value_dict

        self.make_ui()


    def make_ui(self):
        main_layout :QVBoxLayout = QVBoxLayout()
        self.setLayout(main_layout)

        for value_name in self.value_dict:
            value_widget :QFrame = QFrame()
            main_layout.addWidget(value_widget)
            value_widget.setFrameStyle(2)
            value_widget.setContentsMargins(0, 0, 0, 0)

            value_layout :QHBoxLayout = QHBoxLayout()
            value_widget.setLayout(value_layout)

            value_name_widget :QLabel = QLabel(value_name)
            value_layout.addWidget(value_name_widget)

            value_line_edit :QLineEdit = QLineEdit()
            value_layout.addWidget(value_line_edit)
            value_line_edit.textChanged.connect(
                self.make_value_line_func(value_name, value_line_edit))

        self.return_button :QPushButton = QPushButton("Done")
        self.return_button.clicked.connect(self.return_value)
        main_layout.addWidget(self.return_button)


    def make_value_line_func(
            self, 
            value_name :str, 
            value_line_edit :QLineEdit) -> Callable:
        def value_line_func():
            self.value_dict[value_name] = value_line_edit.text()

        return value_line_func


    def return_value(self):
        self.accept()


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

def equipment_test():
    return {
        "money": {
            "platinium": 0,
            "gold": 2,
            "silver": 58,
            "bronze": 434
        },
        "short sword": ["damage 1d8"],
        "knife": ["damage 1d6", "poisonous"],
        "rope": None,
        "healing potion": ["heal 2d8"]
    }

def spell_test():
    return {
        "lv0": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv1": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv2": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv3": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv4": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv5": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv6": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv7": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv8": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        },
        "lv9": {
            "test 1": {
                "effect": "hello",
                "description": "The quick brown fox jumps over the lazy dog"
            },
            "test 2": {
                            "effect": "hello",
                            "description": "The quick brown fox jumps over the lazy dog"
                        }
        }
    }
