#%%
from sqlalchemy import Column, Integer, String, Float
from func import *
import sqlite3
from sqlite3 import connect
import math
test = FromCSV
test.tablename = "testTable"
test.csvname = "test.csv"
ideal = Idealclass
ideal.tablename ="idealTable"
ideal.csvname = "ideal.csv"
train = Trainclass
train.tablename ="trainTable"
train.csvname = "train.csv"
sqliteConnection = sqlite3.connect('ForCalc.db')
cursor = sqliteConnection.cursor()
testXX = "ForCalc.db"
readCSVloadData(ideal.csvname, ideal.tablename, sqliteConnection, cursor, 51, 2)
readCSVloadData(train.csvname, train.tablename, sqliteConnection, cursor, 5, 2)
readCSVloadData(test.csvname, test.tablename, sqliteConnection, cursor, 2, 1)
#identifyideal(sqliteConnection, train.tablename, ideal.tablename)
minvalue_series = identifyideal(sqliteConnection, train.tablename, ideal.tablename)

for n in range(0, 4):
    print(minvalue_series[n])
    for i in range(0, 100):
        table_df = LoadTablefromDB(test.tablename)
        TestX, TestY, IdealY, DeltaY = mergeTestAndIdeal(int(i), minvalue_series[n], table_df)
        if float(DeltaY) < math.sqrt(2): 
            SaveRow(TestX, TestY, DeltaY, minvalue_series[n])
print("Script finished successfully, please find the solution table with the name tresults in the Database")


# %%
