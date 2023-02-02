# main.py
#
# SQL Shell - Personal Project

import sqlite3


def _connect_to_memory() -> None:
    pass

def _initial_rules() -> None:
    print("")

def _get_sql_input() -> str:
    """
    Takes the input for a SQL statement
    Takes lines of input until semicolon or empty input
    """
    statement = ""
    while True:

        next_line = input().strip()
        statement+= next_line
        if next_line == "" or next_line[-1] == ";" :
            return statement

        statement+= "\n"


def _process_sql_statement(statement: str) -> None:
    pass


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
