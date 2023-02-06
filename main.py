# main.py
#
# SQL Shell - Personal Project

import sqlite3


def _connect_to_memory() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")

def _initial_rules() -> None:
    print("TYPE SQL CODE :)")

def _get_sql_input() -> str:
    """
    Takes the input for a SQL statement
    Takes lines of input until semicolon or empty input
    """
    statement = ""
    print(">>> ", end = "")

    while True:

        next_line = input().strip()
        statement+= next_line
        if next_line == "" or next_line[-1] == ";" :
            return statement

        statement+= "\n"

        print("... ", end = "")


def _process_sql_statement(statement: str, connection: sqlite3.Connection) -> sqlite3.Cursor | None:
    try:
        return connection.execute(statement)
    except sqlite3.OperationalError as e:
        print(f"ERROR: {e}")
        return None


def main():

    # connects SQLite to the :memory: database
    connection = _connect_to_memory()

    # prints the initial rules of the program
    _initial_rules()

    while True:
        # Takes one statement of SQL input
        statement = _get_sql_input()

        # processes the statement and ensures validity
        cursor = _process_sql_statement(statement, connection)

        if cursor is not None:
            rows = cursor.fetchall()
            if rows:
                print(*[row for row in rows], sep = "\n")
            cursor.close()



if __name__ == '__main__':
    main()
