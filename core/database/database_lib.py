import sqlite3
import os
import json


def connect_database(file_name :str):
    """
    connect or create sqlite database

    :param file_name(str): name of given database
    :return: database's connection and cursor
    """
    # get current path
    current_path :str = __file__.rpartition("\\")[0]

    # connect to database and create cursor
    connector = sqlite3.connect(f"{current_path}\\{file_name}_BDD.db")
    cursor = connector.cursor()

    # return conection and cursor
    return connector, cursor


def create_table(
        file_name :str,
        table_name :str,
        template :list, 
        force : bool=False
    ):
    """
    create table using given template

    :param file_name(str): name of database
    :param table_name(str): name of the table to add
    :param template(dict): entity template dictionnary
    :param force(bool): if true delete table before creatind a new one
    """
    # connect to database
    connector, cursor = connect_database(file_name)

    # data from template
    info :str = ", ".join(template)

    # if force delete table befor creating a new one
    if force:
        try:
            cursor.execute(f"DROP TABLE {table_name}")
        except sqlite3.OperationalError:
            pass
        cursor.execute(f"CREATE TABLE {table_name} ({info})")
    # else create a new table if it doesn't exist
    else:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({info})")

    # cursor.execute(f"SELECT * FROM {table_name}")
    # print(cursor.fetchall(), type(cursor.fetchall()))

    # commit and close connection
    connector.commit()
    connector.close()


def return_single_column(file_name :str, table_name :str, column_name :str):
    # connect to database
    connector, cursor = connect_database(file_name)

    cursor.execute(f"SELECT {column_name} FROM {table_name}")
    column_value :list = cursor.fetchall()

    # close connection
    connector.close()

    # return value
    return column_value


def return_table(file_name :str, table_name :str):
    # connect to database
    connector, cursor = connect_database(file_name)
    
    cursor.execute(f"SELECT * FROM {table_name}")
    table_value :list = cursor.fetchall()
    
    # close connection
    connector.close()

    # return value
    return table_value


def return_single_row(file_name :str, table_name :str, row_id :int):
    # connect to database
    connector, cursor = connect_database(file_name)
    
    cursor.execute(f"SELECT * FROM {table_name}")
    table_value :list = cursor.fetchall()
    
    # close connection
    connector.close()

    row_data = [row for row in table_value if row[0] == str(row_id)][0]

    # return value
    return row_data

def return_single_data(
        file_name :str, table_name :str, 
        column_name :str, row_id :list[:str, :int]):
    # connect to database
    connector, cursor = connect_database(file_name)

    sql = (f"SELECT {column_name} "
        f"FROM {table_name} "
        f"WHERE {row_id[0]} == ?")

    cursor.execute(sql, str(row_id[1]))
    value :list = cursor.fetchall()

    # close connection
    connector.close()

    # return value
    return value[0][0]


def add_row(file_name :str, table_name : str, entity :dict):
    """
    add entity to the given table

    :param file_name(str): name of the database
    :parama table_name(str): name of the table
    :param entity(dict): entity to add
    """
    # connect to database
    connector, cursor = connect_database(file_name)


    # get info to add to the table
    row_list :list = [str(entity[key]) for key in entity]

    # make sql statement
    sql :str = "INSERT INTO {} VALUES ({})".format(
        table_name, 
        "?, "*(len(row_list)-1)+"?"
    )

    # execute sql statement
    cursor.execute(sql, row_list)

    # cursor.execute(f"SELECT * FROM {table_name}")
    # print(cursor.fetchall(), type(cursor.fetchall()))

    # commit and close connection
    connector.commit()
    connector.close()


def replace_row(file_name :str, table_name :str, value_dict :dict):
    """
    add entity to the given table

    :param file_name(str): name of the database
    :parama table_name(str): name of the table
    :param entity(dict): entity to add
    """
    # connect to database
    connector, cursor = connect_database(file_name)


    # get info to add to the table
    row_entry :list = [str(key) for key in value_dict]
    row_list :list = [str(value_dict[key]) for key in value_dict]

    # make sql statement

    sql :str = "REPLACE INTO {} ({}) " \
                "VALUES ({})".format(
            table_name, 
            ",".join(row_entry),
            "?, "*(len(row_list)-1)+"?"
        )

    # execute sql statement
    cursor.execute(sql, row_list)

    # commit and close connection
    connector.commit()
    connector.close()


def replace_value(
        file_name :str, 
        table_name :str, 
        condition_list :list[:str, :str],
        info_name :str, 
        info_value:str):
    """
    add entity to the given table
        
    :param file_name(str): name of the database
    :parama table_name(str): name of the table
    :param entity(dict): entity to add
    """
    # connect to database
    connector, cursor = connect_database(file_name)

    sql :str = "UPDATE {} " \
                "SET {}=? " \
                "WHERE {}=?;".format(
                    table_name,
                    info_name,
                    condition_list[0])

    # execute sql statement
    cursor.execute(sql, (str(info_value), str(condition_list[1])))

    # commit and close connection
    connector.commit()
    connector.close()


##########################################################################################
# test
##########################################################################################


def get_template(val):
    """
    temp for create database fonction
    """
    if val == 1:
        return {
            "name": (str, "info"),
            "species": (str, "info"),
            "strenght": (int, "stat"),
            "dexterity": (int, "stat"),
            "constitution": (int, "stat"),
            "intelligence": (int, "stat"),
            "wisdom": (int, "stat"),
            "charisma": (int, "stat")
        }
    
    if val == 2:
        return {
            "name": (str, "info"),
            "constitution": (int, "stat"),
            "intelligence": (int, "stat"),
            "wisdom": (int, "stat"),
            "charisma": (int, "stat")
        }


def get_data(val):
    """
    temp for create database fonction
    """
    if val == 1:
        return {
            "name": "test_na",
            "species": "test_species",
            "strenght": 15,
            "dexterity": 13,
            "constitution": 16,
            "intelligence": 11,
            "wisdom": 8,
            "charisma": 9
        }
    if val == 2:
        return {
            "name": "test_na",
            "constitution": 16,
            "intelligence": 11,
            "wisdom": 8,
            "charisma": 9
        }


def test_data():
    """
    test made to write data in a database
    """
    connector, cursor = connect_database("DnD")

    value = ", ".join(list(get_template()))
    cursor.execute(f"""CREATE TABLE entity ({value})""")

    row_list = [str(get_data()[key]) for key in get_data()]

    cursor.execute(
        """INSERT INTO entity VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        row_list
    )
    cursor.execute("""SELECT name FROM entity""")
    print(cursor.fetchall())

    connector.commit()
    connector.close()


"""create_table("DnD", "test1", get_template(1), force=True)
create_table("DnD", "test2", get_template(2), force=False)
add_row("DnD", "test1", get_data(1))
add_row("DnD", "test2", get_data(2))"""

"""print(return_table("DnD", "character_table"))
print(return_single_column("DnD", "character_table", "charisma"))
print(return_single_row("DnD", "character_table", 0))
print(return_single_data("DnD", "character_table", "charisma", ["entity_id", 0]))"""
