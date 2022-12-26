#%%
from func import *  # imports all functions and classes from func.py
import sqlite3
import math
'''
Running this script the given task will be fullfilled.
Including the identification of the ideal functions from the ideal dataset,
plotting various datasets,
testing the result with the test dataset.
This script accesses functions and classes from the func.py script.
'''
test = FromCSV  # generating an object from the FromCSV class
test.tablename = "testTable"  # changing an attribute value
test.csvname = "test.csv"  # changing an attribute value
ideal = Idealclass  # generating an object from the FromCSV class
ideal.tablename = "idealTable"  # changing an attribute value
ideal.csvname = "ideal.csv"  # changing an attribute value
train = Trainclass  # generating an object from the FromCSV class
train.tablename = "trainTable"  # changing an attribute value
train.csvname = "train.csv"  # changing an attribute value
sqliteConnection = sqlite3.connect('ForCalc.db')  # conencting to sqllite
cursor = sqliteConnection.cursor()  # creating a cursor object using the cursor() method
readCSVloadData(ideal.csvname, ideal.tablename, sqliteConnection, cursor, 51, 2)  # read and load data from CSV to db using a function, plots dataset
readCSVloadData(train.csvname, train.tablename, sqliteConnection, cursor, 5, 2)  # read and load data from CSV to db using a function, plots dataset 
readCSVloadData(test.csvname, test.tablename, sqliteConnection, cursor, 2, 1)  # read and load data from CSV to db using a function, plots dataset
minvalue_series = identifyideal(train.tablename, ideal.tablename) # identifies the matching ideal functions and plots the results

for n in range(0, 4):  # for loop the range of 0:4 stands for the 4 ideal functions
    for i in range(0, 100):  # for loop the range of 0:100 stands for the 100 test datasets 
        table_df = LoadTablefromDB(test.tablename)  # calls function and loads test data from database and save in df 
        '''
        Call function mergeTestAndIdeal.
        Merge the TestData and IdealFunctions based on the x-value.
        Returns values for variable definition.
        '''
        TestX, TestY, IdealY, DeltaY = mergeTestAndIdeal(int(i), minvalue_series[n], table_df)
        if float(DeltaY) < math.sqrt(2):  # Test if testing criteria is fullfilled
            #SaveRow(TestX, TestY, DeltaY, minvalue_series[n])  # call function, saves row if criteria is fullfilled
            print("x")
print("Script finished successfully, please find the solution table with the name tresults in the Database")  # prints confirmation once script ran successfully

# %%