# main.py
#
# SQL Shell - Personal Project

import sqlite3


def main():

    # connects SQLite to the :memory: database
    _connect_to_memory()

    # prints the initial rules of the program
    _initial_rules()

    while True:
        # Takes one statement of SQL input
        statement = _get_sql_input()

        # processes the statement and ensures validity
        _process_sql_statement(statement)



if __name__ == '__main__':
    main()
