'''The Purpose of this script is to test 2 functions of the func.py'''
import unittest
from func import *
import sqlite3
sqliteConnection = sqlite3.connect('ForCalc.db')  # Connect to databse
cursor = sqliteConnection.cursor()  # Save cursor in a variable
table_name = "UnitTestTable"  # Define variable, will be needed to open a specific Table, for testing purposes

'''Definition of a TestClass to make the inheritance of TestCases possible'''
class UnitTests(unittest.TestCase):
    '''Tetsing of chk_conn'''
    def test_chk_connection(self):
        result = chk_conn(cursor)  # Save acutal value in variable
        self.assertEqual(result, False, "There should not be a connection to the database")  # Compare actual with planned value
    '''Tetsing of "FileNotFoundException" handling'''
    def test_FileNotFoundException(self):
        result = readCSVloadData("NotaFile.csv", "idealTable", sqliteConnection, cursor, 51, 0)  # Save acutal value in variable
        self.assertEqual(result, 0)  # Compare actual with planned value
    '''Tetsing of LoadTablefromDB'''
    def test_loadtable(self):
        result = LoadTablefromDB("UnitTestTable")  # Load Table in a df
        result = result.iloc[0,0]  # Save acutal value(one specific cell of df) in variable
        self.assertEqual(result, 123) # Compare actual with planned value
if __name__ == '__main__':
    # run script in unittest context
    unittest.main()
