import sqlite3
import os


def connect_database(name :str):
    """
    connect or create sqlite database

    :param name(str): name of given database
    :return: database's connection and cursor
    """
    # get current path
    current_path :str = __file__.rpartition("\\")[0]

    # connect to database and create cursor
    connector = sqlite3.connect(f"{current_path}\\{name}_entity.db")
    cursor = connector.cursor()

    # return conection and cursor
    return connector, cursor


def create_table(name :str, template :dict, force : bool=False):
    """
    create entity table using given template

    :param name(str): name of database
    :param template(dict): entity template dictionnary
    :param force(bool): if true delete table before creatind a new one
    """
    # connect to database
    connector, cursor = connect_database(name)

    # data from template
    info = ", ".join(tuple(template))

    # if force delete table befor creating a new one
    if force:
        try:
            cursor.execute("DROP TABLE entity")
        except sqlite3.OperationalError:
            pass
        cursor.execute(f"CREATE TABLE entity ({info})")
    # else create a new table if it doesn't exist
    else:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS entity ({info})")

    cursor.execute("SELECT * FROM entity")
    print(cursor.fetchall(), type(cursor.fetchall()))

    # commit and close connection
    connector.commit()
    connector.close()


def add_entity(name :str, entity :dict):
    """
    add entity to the entity table

    :param name(str): name of the database
    :param entity(dict): entity to add
    """
    # connect to database
    connector, cursor = connect_database(name)


    # get info to add to the table
    row_list :list = [str(entity[key]) for key in entity]

    # make sql statement
    sql :str = "" "INSERT INTO entity VALUES ({})".format("?, "*(len(row_list)-1)+"?")
    #print("?, "*(len(row_list)-1)+"?")

    # execute sql statement
    cursor.execute(sql, row_list)

    cursor.execute("SELECT * FROM entity")
    print(cursor.fetchall(), type(cursor.fetchall()))

    # commit and close connection
    connector.commit()
    connector.close()


def get_template():
    """
    temp for create database fonction
    """
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


def get_data():
    """
    temp for create database fonction
    """
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


create_table("DnD", get_template(), force=True)
add_entity("DnD", get_data())
