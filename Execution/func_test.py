import unittest
from func import *
import sqlite3

'''
The Target of this script is to test 2 functions of the func.py
'''

sqliteConnection = sqlite3.connect('ForCalc.db')  # Connect to databse
cursor = sqliteConnection.cursor()  # save cursor in a variable
table_name = "UnitTestTable"  # define variable, will be needed to open a specific Table, for testing purposes

class UnitTests(unittest.TestCase):
    '''
    Definition of a TestClass to make the inheritance of TestCases possible
    '''
    def test_chk_connection(self):
        '''
        Tetsing of chk_conn
        '''
        result = chk_conn(cursor)  # save acutal value in variable
        self.assertEqual(result, False, "There should not be a connection to the database")  # compare actual with planned value
    def test_FileNotFoundException(self):
        '''
        Tetsing of "FileNotFoundException" handling
        '''
        result = readCSVloadData("NotaFile.csv", "idealTable", sqliteConnection, cursor, 51, 0)  # save acutal value in variable
        self.assertEqual(result, 0)  # compare actual with planned value
    def test_loadtable(self):
        '''
        Tetsing of LoadTablefromDB
        '''
        result = LoadTablefromDB("UnitTestTable")  # load Table in a df
        result = result.iloc[0,0]  # save acutal value(one specific cell of df) in variable
        self.assertEqual(result, 123) # compare actual with planned value
if __name__ == '__main__':
    '''
    run script in unittest contextd
    '''
    unittest.main()
