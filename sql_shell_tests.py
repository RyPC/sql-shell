# sql_shell_tests.py
#
# SQL Shell - Personal Project

import unittest
from unittest.mock import patch
import main
import sqlite3

class SQL_Shell_Tests(unittest.TestCase):

    @patch("builtins.input", side_effect = ["SELECT * FROM people;"])
    def test_one_line_sql_input(self, mock_input):
        statement = main._get_sql_input()
        self.assertEqual("SELECT * FROM people;", statement)


    @patch("builtins.input", side_effect = ["SELECT * FROM people", "WHERE age > 20;"])
    def test_multiple_line_sql_input(self, mock_input):
        statement = main._get_sql_input()
        self.assertEqual("SELECT * FROM people\nWHERE age > 20;", statement)


    @patch("builtins.input", side_effect = ["SELECT * FROM people", "WHERE age > 20", ""])
    def test_sql_input_not_ending_in_semicolon(self, mock_input):
        statement = main._get_sql_input()
        self.assertEqual("SELECT * FROM people\nWHERE age > 20\n", statement)

