def chk_conn(connx):
    import sqlite3 as mdb
    try:
        connx.cursor()
        return True
    except Exception as e:
        return False
        print(e)
        print("No active connection to DB")


def connectToDB():
    import sqlalchemy as db
    from sqlalchemy_utils import database_exists, create_database
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database
    from sqlalchemy import Table, Column, Integer, String, Float
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import mapper
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import relationship
    engine = create_engine('sqlite:///ForCalc.db')
    base = declarative_base()
    conn = engine.connect()
    return engine, base, conn

def readCSVloadData(csvname, tablename, conn, cursor, ccount):
    import pandas as pd
    from sqlalchemy import desc
    try:
        with open(csvname) as f:
            df = pd.read_csv(csvname, skiprows = 0)
            df.sort_values(["x"],axis=0, ascending=True,inplace=True,na_position='first')
            df.to_sql(tablename, con= conn, index = False, if_exists = 'replace')
    except FileNotFoundError as e:
        print("File was not found, please save the file with the right name on the right spot")
    else: print("done")
    plottable(tablename, ccount)
    print(chk_conn(cursor))

import sqlalchemy as db
from func import *
from sqlalchemy import create_engine
import sqlite3
class Tabelle():
    #engine = create_engine('sqlite:///ForCalc.db')
    #conn = engine.connect()
    tablename = "Tabelenname"
class FromCSV(Tabelle):
    csvname = "examplecsv"
    x = db.Column(db.Float, primary_key=True)
    y1 = db.Column(db.Float, nullable=False)

test = FromCSV

class Trainclass(FromCSV):
    y2 = db.Column(db.Float, nullable=False)
    y3 = db.Column(db.Float, nullable=False)
    y4 = db.Column(db.Float, nullable=False)

class Idealclass(Trainclass):
    y5 = db.Column(db.Float, nullable=False)
    y6 = db.Column(db.Float, nullable=False)
    y7 = db.Column(db.Float, nullable=False)
    y8 = db.Column(db.Float, nullable=False)
    y9 = db.Column(db.Float, nullable=False)
    y10 = db.Column(db.Float, nullable=False)
    y11 = db.Column(db.Float, nullable=False)
    y12 = db.Column(db.Float, nullable=False)
    y13 = db.Column(db.Float, nullable=False)
    y14 = db.Column(db.Float, nullable=False)
    y15 = db.Column(db.Float, nullable=False)
    y16 = db.Column(db.Float, nullable=False)
    y17 = db.Column(db.Float, nullable=False)
    y18 = db.Column(db.Float, nullable=False)
    y19 = db.Column(db.Float, nullable=False)
    y20 = db.Column(db.Float, nullable=False)
    y10 = db.Column(db.Float, nullable=False)
    y11 = db.Column(db.Float, nullable=False)
    y12 = db.Column(db.Float, nullable=False)
    y13 = db.Column(db.Float, nullable=False)
    y14 = db.Column(db.Float, nullable=False)
    y15 = db.Column(db.Float, nullable=False)
    y16 = db.Column(db.Float, nullable=False)
    y17 = db.Column(db.Float, nullable=False)
    y18 = db.Column(db.Float, nullable=False)
    y19 = db.Column(db.Float, nullable=False)
    y20 = db.Column(db.Float, nullable=False)
    y21 = db.Column(db.Float, nullable=False)
    y22 = db.Column(db.Float, nullable=False)
    y23 = db.Column(db.Float, nullable=False)
    y24 = db.Column(db.Float, nullable=False)
    y25 = db.Column(db.Float, nullable=False)
    y26 = db.Column(db.Float, nullable=False)
    y27 = db.Column(db.Float, nullable=False)
    y28 = db.Column(db.Float, nullable=False)
    y29 = db.Column(db.Float, nullable=False)
    y30 = db.Column(db.Float, nullable=False)
    y31 = db.Column(db.Float, nullable=False)
    y32 = db.Column(db.Float, nullable=False)
    y33 = db.Column(db.Float, nullable=False)
    y34 = db.Column(db.Float, nullable=False)
    y35 = db.Column(db.Float, nullable=False)
    y36 = db.Column(db.Float, nullable=False)
    y37 = db.Column(db.Float, nullable=False)
    y38 = db.Column(db.Float, nullable=False)
    y39 = db.Column(db.Float, nullable=False)
    y40 = db.Column(db.Float, nullable=False)
    y41 = db.Column(db.Float, nullable=False)
    y42 = db.Column(db.Float, nullable=False)
    y43 = db.Column(db.Float, nullable=False)
    y44 = db.Column(db.Float, nullable=False)
    y45 = db.Column(db.Float, nullable=False)
    y46 = db.Column(db.Float, nullable=False)
    y47 = db.Column(db.Float, nullable=False)
    y48 = db.Column(db.Float, nullable=False)
    y49 = db.Column(db.Float, nullable=False)
    y50 = db.Column(db.Float, nullable=False)


def chk_conn(conn):
    try:
        conn.cursor()
        return True
        print(Conenction is open)
    except Exception as ex:
        return False
        print("No connection to sqllite DB")

def plottable(tablename, columncount):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from matplotlib import style
    import math  

    import pandas as pd
    import sqlalchemy as db
    import numpy as np
    from sqlalchemy import Integer
    from sqlalchemy import create_engine, Integer, Column, String, Float
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base


    engine = create_engine('sqlite:///ForCalc.db')
    table_df = pd.read_sql_table(
        tablename,
        con=engine)

    for n in range(2, columncount):
        X = table_df.iloc[:,0]
        Y1 = table_df.iloc[:,n]
        plt.plot(X,Y1, color='#8A0808', linestyle='--',label=('Y' + str(n) ))
    
    plt.title(tablename + "dataset")
    plt.xlabel('x-Values')
    plt.ylabel('y-Values')
    plt.legend()
    plt.grid(True)
    plt.show

def identifyideal(conn, table_name, table_name2):
    import pandas as pd
    import sklearn.metrics
    import matplotlib.pyplot as fig
    engine = create_engine('sqlite:///ForCalc.db')
    df4 = pd.DataFrame(columns=['Error1','Error2','Error3','Error4'], index=range(1,50))
    for n in range(1, 51):
        df1 = pd.read_sql_table(table_name,con=engine)
        df2 = pd.read_sql_table(table_name2,con=engine)

        
        mse1 = sklearn.metrics.mean_squared_error(df1.iloc[:,1] , df2.iloc[:,n])
        mse2 = sklearn.metrics.mean_squared_error(df1.iloc[:,2] , df2.iloc[:,n])
        mse3 = sklearn.metrics.mean_squared_error(df1.iloc[:,3] , df2.iloc[:,n])
        mse4 = sklearn.metrics.mean_squared_error(df1.iloc[:,4] , df2.iloc[:,n])
        
        errors = [mse1, mse2, mse3, mse4]
        #df3 = pd.DataFrame([[mse1, mse2, mse3, mse4]], columns=['Error1','Error2','Error3','Error4'])
        #df4.append(errors, ignore_index=False)
        df4.loc[n-1] = errors
    print(df4)
    minvalue_series = df4.idxmin()
    for x in range(0,4):
        X = df1.iloc[:,0]
        Y1 = df1.iloc[:,x+1]
        Y2 = df2.iloc[:,minvalue_series[x]]
        fig.plot(X,Y1, color='#8A0808', linestyle='--',label='Original')
        fig.plot(X,Y2, color='#0B610B', linestyle='-',label='Bestfit')
        fig.title('Original + Ideal line')
        fig.xlabel('x-Values')
        fig.ylabel('y-Values')
        fig.legend()
        fig.grid(True)
        fig.show

