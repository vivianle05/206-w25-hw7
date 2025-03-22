# Name:
# Student ID:
# Email:
# List who you have worked with on this homework:
# List any AI tool you used (e.g. ChatGPT, GitHub Copilot):


import unittest
import sqlite3
import json
import os


def read_data_from_file(filename):
    """
    Reads data from a file with the given filename.

    Parameters
    -----------------------
    filename: str
        The name of the file to read

    Returns
    -----------------------
    dict:
        Parsed JSON data from the file
    """
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data


def set_up_pokemon_database(db_name):
    """
    Sets up a SQLite database connection and cursor.

    Parameters
    -----------------------
    db_name: str
        The name of the SQLite database

    Returns
    -----------------------
    Tuple (cursor, connection):
        A tuple containing the database cursor and connection objects.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn


def set_up_types_table(data, cur, conn):
    """
    Sets up the Types table in the database using the provided Pokemon data.

    Parameters
    -----------------------
    data: list
        List of Pokemon data in JSON format

    cur: cursor
        The database cursor object

    conn: connection
        The database connection object

    Returns
    -----------------------
    None
    """
    type_list = []
    for pokemon in data:
        pokemon_type = pokemon["type"][0]
        if pokemon_type not in type_list:
            type_list.append(pokemon_type)
        if len(pokemon["type"]) > 1:
            pokemon_type = pokemon["type"][1]
            if pokemon_type not in type_list:
                type_list.append(pokemon_type)
    
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Types (id INTEGER PRIMARY KEY, type TEXT UNIQUE)"
    )

    for i in range(len(type_list)):
        cur.execute(
            "INSERT OR IGNORE INTO Types (id,type) VALUES (?,?)", (i,
                                                                   type_list[i])
        )
    conn.commit()


#############################################################################
####### START BELOW, DO NOT CHANGE THE CODE FROM THE ABOVE FUNCTIONS ########
#############################################################################


def create_pokemon_table(data, cur, conn):
    """
    Parameters
    -----------------------
    data: str
        Stores pokemon.json, written in JSON format
    
    cur: cursor
        The database cursor object

    conn: connection
        The database connection object

    Returns
    -----------------------
    Nothing
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_pokemon_by_spdefense_range(spdefense_min, spdefense_max, cur):
    """
    Parameters
    -----------------------
    spdefense_min: int
        Passed in special defense MIN value

    spdefense_max: int
        Passed in special defense MAX value
    
    cur: cursor
        The database cursor object

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, special_defense),...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_top_attack_pokemon(base_attack, cur):
    """
    Parameters
    -----------------------
    base_attack: int
        Passed in attack value

    cur: cursor
        The database cursor object
    
    Returns
    -----------------------
    list:
        list of tuples [(name, attack),...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_pokemon_physical_sweepers(attack, speed, HP, cur):
    """
    Parameters
    -----------------------
    attack: int
        Passed in attack value

    speed: int
        Passed in speed value

    HP: int
        Passed in HP value
    
    cur: cursor
        The database cursor object

    Returns
    -----------------------
    list:
        list of tuples [(name, attack, speed, HP),...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass


def get_pokemon_type_above_speed_defense(pokemon_type, speed, defense, cur):
    """
    Parameters
    -----------------------
    pokemon_type: str
        Passed in type str (e.g. 'Grass')

    speed: int
        Passed in speed value

    defense: int
        Passed in defense value

    cur: cursor
        The database cursor object

    Returns
    -----------------------
    list:
        list of tuples [(name, type, speed, defense),...]

    """
    # YOUR CODE IMPLEMENTATION HERE
    pass



###### EXTRA CREDIT ######
def get_pokemon_type_above_attack_HP(pokemon_type, attack, HP, cur):
    """
    Parameters
    -----------------------
    pokemon_type: str
        Passed in type str (e.g. 'Grass')

    attack: int
        Passed in attack value

    HP: int
        Passed in HP value

    cur: cursor
        The database cursor object
    
    Parameters
    -----------------------
    list:
        list of tuples: [(name, type, attack, HP), ...]
    """
    # YOUR CODE IMPLEMENTATION HERE
    pass



###### DO NOT CHANGE TEST CASES ######
class TestAllMethods(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(path + "/" + "pokemon.db")
        self.cur = self.conn.cursor()
        self.data = read_data_from_file("pokemon.json")


    def test_pokemon_table(self):
        self.cur.execute("SELECT * from Pokemon")
        pokemon_list = self.cur.fetchall()
        self.assertEqual(len(pokemon_list), 106)
        self.assertEqual(len(pokemon_list[0]), 9)
        self.assertIs(type(pokemon_list[0][0]), int)
        self.assertIs(type(pokemon_list[0][1]), str)
        self.assertIs(type(pokemon_list[0][2]), int)
        self.assertIs(type(pokemon_list[0][3]), int)
        self.assertIs(type(pokemon_list[0][4]), int)
        self.assertIs(type(pokemon_list[0][5]), int)
        self.assertIs(type(pokemon_list[0][6]), int)
        self.assertIs(type(pokemon_list[0][7]), int)
        self.assertIs(type(pokemon_list[0][8]), int)


    def test_get_pokemon_by_spdefense_range(self):
        x = get_pokemon_by_spdefense_range(40, 50, self.cur)
        self.assertEqual(len(x), 23)
        self.assertEqual(len(x[0]), 3)
        self.assertEqual(x[0], (4, 'Charmander', 50))
        self.assertEqual(x[1], (17, 'Pidgeotto', 50))
        self.assertEqual(x[-1], (104, 'Ducklett', 50))

        y = get_pokemon_by_spdefense_range(100, 200, self.cur)
        self.assertEqual(len(y), 10)
        self.assertEqual(len(y[0]), 3)
        self.assertEqual(y[0], (3, 'Venusaur', 100))
        self.assertEqual(y[1], (9, 'Blastoise', 105))
        self.assertEqual(y[-1], (100, 'Gothitelle', 110))


    def test_get_top_attack_pokemon(self):
        x = get_top_attack_pokemon(100, self.cur)
        self.assertEqual(len(x), 13)
        self.assertEqual(x[0], ('Archeops', 140))
        self.assertEqual(x[1], ('Kingler', 130))
        self.assertEqual(x[2], ('Rhydon', 130))
        self.assertEqual(x[-1], ('Sandslash', 100))


    def test_get_pokemon_physical_sweepers(self):
        x = get_pokemon_physical_sweepers(60, 30, 20, self.cur)
        self.assertEqual(len(x), 4)
        self.assertEqual(len(x[0]), 4)
        self.assertEqual(x[0], ('Pidgeotto', 60, 71, 63))
        self.assertEqual(x[1], ('Spearow', 60, 70, 40))
        self.assertEqual(x[-1], ('Magneton', 60, 70, 50))

        y = get_pokemon_physical_sweepers(90, 50, 60, self.cur)
        self.assertEqual(len(y), 3)
        self.assertEqual(len(y[0]), 4)
        self.assertEqual(y[0], ('Beedrill', 90, 75, 65))
        self.assertEqual(y[1], ('Fearow', 90, 100, 65))
        self.assertEqual(y[-1], ('Weezing', 90, 60, 65))


    def test_get_pokemon_type_above_speed_defense(self):
        x = get_pokemon_type_above_speed_defense("Ground", 40, 50, self.cur)
        self.assertEqual(len(x), 2)
        self.assertEqual(len(x[0]), 4)
        self.assertEqual(x[0], ('Sandslash', 'Ground', 65, 110))
        self.assertEqual(x[-1], ('Marowak', 'Ground', 45, 110))

        y = get_pokemon_type_above_speed_defense("Grass", 50, 60, self.cur)
        self.assertEqual(len(y), 4)
        self.assertEqual(len(y[0]), 4)
        self.assertEqual(y[0], ('Ivysaur', 'Grass', 60, 63))
        self.assertEqual(y[1], ('Venusaur', 'Grass', 80, 83))
        self.assertEqual(y[-1], ('Tangela', 'Grass', 60, 115))


    ###### CREATE 8 TEST CASES BELOW FOR EXTRA CREDIT ######
    def test_get_pokemon_type_above_speed_defense(self):
        pass


def main():
    json_data = read_data_from_file("pokemon.json")
    cur, conn = set_up_pokemon_database("pokemon.db")
    set_up_types_table(json_data, cur, conn)
    create_pokemon_table(json_data, cur, conn)
    conn.close()


if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)