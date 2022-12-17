#%%
import sqlalchemy as db
import math  
import sklearn.metrics
from sqlalchemy import Table, Column, Integer, String, Float
from func import *
import sqlite3 as mdb
#connectToDB()
#engine, base, conn = connectToDB()
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
readCSVloadData(ideal.csvname, ideal.tablename, sqliteConnection, cursor, 50)
readCSVloadData(train.csvname, train.tablename, sqliteConnection, cursor, 4)
readCSVloadData(test.csvname, test.tablename, sqliteConnection, cursor, 1)
identifyideal(sqliteConnection, train.tablename, ideal.tablename)



# %%
