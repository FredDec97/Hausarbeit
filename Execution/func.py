'''
This script includes most of the functions and classes that are used in order to fullfill the task.
The Mainbranch.py script calls the functions in this sheet.
The func_test.py includes unitstest for some functions in this sheet.
'''

'''
This function tests if the conenction to the data base is active.
If the connection is not active an excepteion is raised.
The passed argument passes the corresponding cursor object of the conenction that should be checked
The function returns "True" or "False" depending if the conenction is active or not
'''
def chk_conn(connx):
    import sqlite3 as mdb
    try:
        connx.cursor()  # Try to connect to 
        return True  # Return is used for unittest
    except Exception as e:  # if no active connection, exception is raised
        return False  # Return is used for unittest
        print(e)  # Prints Error
        print("No active connection to DB")  # Prionts own explaination

'''
    Function "readCSVloadData" opens, reads, sorts data from CSV, and saves data in sql table.
    Exception is raised if file cannot be found.
    Function calls other function to plot the data.
    Passed arguments:
        csvname: Passes name of CSVfile that sould be read and the data save to db
        tablename: Passes name of the table, where data should be saved
        conn: Passes sqllite connection
        cursor: Passes cursor object of the database, where data shall be saved
        ccount: Passes the number of columns that shall be plotted
        scatter: Value = 1 or 2, influences the style of plot that is generated
    '''
def readCSVloadData(csvname, tablename, conn, cursor, ccount, scatter):
    import pandas as pd
    from sqlalchemy import desc
    try:
        with open(csvname) as f:  # open CSV file
            df = pd.read_csv(csvname, skiprows = 0)  # read CSV file
            df.sort_values(["x"],axis=0, ascending=True,inplace=True,na_position='first')  # read values
            df.to_sql(tablename, con= conn, index = False, if_exists = 'replace')  # load data to SQL table
    except FileNotFoundError as e:  # Raise Exception if file was not found
        returnvalue = 0
        print("File was not found, please save the file with the right name on the right location")  # print solution for error
    else:
        print("File was found and script can be continued")
        returnvalue = 1
    if scatter == 1:  
        plottable2(tablename, ccount)  # if scatter value equals 1, data is plotted as scatterplot
    else:
        if scatter == 2:
            plottable1(tablename, ccount)  # if scatter value equals 2, data is plotted as linegraph
        else:
            print("No plot requiered") # if scatter value does not equal 1 or 2, no plot is requiered and a statement is printed instead
    print(chk_conn(cursor))  # function is called to check connection
    return returnvalue

import sqlalchemy as db
from func import *
from sqlalchemy import create_engine
'''
This class is the parent class for all table objects that are generated with classes.
The Attribute tablename is genarated and predefined.
'''
class Tabelle():
    tablename = "Tabelenname"
'''
The FromCSV class is based on the Tabelle Class and is the basis for all tables that are are generated with the help of CSV.
The Attributes csvname, x, and y1 are genarated and predefined.
x and y1 are generated as columns for our tables.
'''
class FromCSV(Tabelle):
    csvname = "examplecsv"
    x = db.Column(db.Float, primary_key=True)
    y1 = db.Column(db.Float, nullable=False)

'''
The Trainclass is based on the FromCSV class and adds exact as many column attributes as are need for the train table later on
'''
class Trainclass(FromCSV):
    y2 = db.Column(db.Float, nullable=False)
    y3 = db.Column(db.Float, nullable=False)
    y4 = db.Column(db.Float, nullable=False)

'''
The Idealclass is based on the Trainclass class and adds exact as many column attributes as are need for the Ideal table later on
'''
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

'''
The "identifyideal"-function identifies the function with lowest mse compared to every training function.
The ideal function is plotted with the corresponding training function.
The index of 4 ideal functions are returned
Passed arguments:
    table_name: Passes the name of the table with the train functions
    table_name2:Passes the name of the table with the ideal function
'''
def identifyideal(table_name, table_name2):
    import pandas as pd
    import sklearn.metrics
    import matplotlib.pyplot as plt
    engine = create_engine('sqlite:///ForCalc.db')
    df4 = pd.DataFrame(columns=['Error1','Error2','Error3','Error4'], index=range(1,50))  # Generate df where the Error values can be saved
    for n in range(1, 51):  # For every column in the ideal data set(for every test function)
        df1 = pd.read_sql_table(table_name,con=engine)  # Define df1 = train data
        df2 = pd.read_sql_table(table_name2,con=engine)  # Define df1 = ideal data

        
        mse1 = sklearn.metrics.mean_squared_error(df1.iloc[:,1] , df2.iloc[:,n])  # Calculating the MSE of 1st Traincolumn and n ideal column and save in variable
        mse2 = sklearn.metrics.mean_squared_error(df1.iloc[:,2] , df2.iloc[:,n])  # Calculating the MSE of 2nd Traincolumn and n ideal column and save in variable
        mse3 = sklearn.metrics.mean_squared_error(df1.iloc[:,3] , df2.iloc[:,n])  # Calculating the MSE of 3rd Traincolumn and n ideal column and save in variable
        mse4 = sklearn.metrics.mean_squared_error(df1.iloc[:,4] , df2.iloc[:,n])  # Calculating the MSE of 4th Traincolumn and n ideal column and save in variable
        
        errors = [mse1, mse2, mse3, mse4]  # Save errors in list
        df4.loc[n-1] = errors  # Add line to df with values = errors
    minvalue_series = df4.idxmin()+1  # save the line number with the lowest error in variable
    print(minvalue_series)
   
    plt.figure()  # Generate new figure
    '''
    Every of the four ideal lines shall be plotted.
    The Datapoints of the test dataset shall be plotted in the same figure.
    '''
    for x in range(0,4):
        X = df1.iloc[:,0]  # Definition of x-values for the plot
        #Y1 = df1.iloc[:,x+1]
        Y2 = df2.iloc[:,minvalue_series[x]]  # Definition of y-values for the ideal line
        #plt.plot(X,Y1, color='#8A0808', linestyle='--',label='Original')
        plt.plot(X,Y2, color='#0B610B', linestyle='-',label='Bestfit'+ str(x+1))
        plt.title('Ideal and Test')
        plt.xlabel('x-Values')
        plt.ylabel('y-Values')
        plt.legend()
        plt.grid(True)
        plt.show

    engine = create_engine('sqlite:///ForCalc.db')
    table_df = pd.read_sql_table(
        "testTable",
        con=engine)  # Definition of table_df = Table with train data
    X = table_df.iloc[:,0]
    Y1 = table_df.iloc[:,1]  # Definition of y-values for the test line
    plt.plot(figsize=(6,4))
    plt.plot(X,Y1, 'o', color='black', label=('Test'))  # plot as scatterplot 
    plt.xlabel('x-Values')
    plt.ylabel('y-Values')
    plt.legend()
    plt.grid(True)
    plt.show
    
    plt.figure()  # Generate new figure
    for x in range(0,4):  # For every test function 
        X = df1.iloc[:,0]  # Definition of x-values
        Y1 = df1.iloc[:,x+1]  # Definition of y-values of the train functions
        Y2 = df2.iloc[:,minvalue_series[x]] # Definition of y-values of the ideal functions
        plt.plot(X,Y1, color='#8A0808', linestyle='--',label='Original')
        plt.plot(X,Y2, color='#0B610B', linestyle='-',label='Bestfit')
        plt.title('Original + Ideal line')
        plt.xlabel('x-Values')
        plt.ylabel('y-Values')
        plt.legend()
        plt.grid(True)
        plt.show
    return minvalue_series  # Return indexes of the 4 ideal functions

'''
The function "mergeTestAndIdeal" merges the Test data with the 4 ideal functions for the passed row of the test dataset.
Merging based on x-values in the test table.
The merged table is saved in a df "Testdf"
Passed arguments:
    Row: Row of the test dataset, the TestX and TestY value can be identified with the help of this value
    Index: Passes the column number of the column in the ideal dataset, that should be merged
    table_df: A df containing the test data
Returns:
    TestX: x-values of test function
    TestY: y-values of test function
    IdealY: y-values of ideal function
    DeltaY: Difference between TestY and IdealY
'''
def mergeTestAndIdeal(Row, Index, table_df):
    import pandas as pd
    import sqlalchemy as db
    from sqlalchemy import engine
    engine = create_engine('sqlite:///ForCalc.db')
    TestX = table_df.iloc[Row-1,0]  # Loads a x-value of the test dataset based on the defined Row
    TestY = table_df.iloc[Row-1,1]  # Loads a y-value of the test dataset based on the defined Row
    Testdf = pd.DataFrame({'x': [TestX],'y': [TestY]})  # Save loaded values in df
    table_name = "idealTable"
    table_df2 = pd.read_sql_table(
    table_name,
    con=engine)
    Testdf = pd.merge(Testdf,table_df2.iloc[:,:51], on="x",how="left")  # Combine loaded Test values with ideal values and save in df
    IdealY = Testdf.iloc[0, Index+1]  # Define variable
    DeltaY = abs(IdealY - TestY)      # Calculate absolute difference between Y-Values       
    return(TestX, TestY, IdealY, DeltaY)  # Return variables
    
'''
The "LoadTablefromDB" function loads the data from a defined table(arguments) and saves it in a df.
Passed argument: table_name: passes name of a sql table in predefined db.
Returns data from sql table as a df.
'''
def LoadTablefromDB(table_name): 
    import pandas as pd
    import sqlalchemy as db
    from decimal import Decimal
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///ForCalc.db')  # Connect to db
    table_df = pd.read_sql_table(
    table_name,
    con=engine)
    return(table_df)  # return loaded data as df

'''
The "SaveRow" function generates a new table "Tresulst" were the solution of the Testing shall be saved.
The passed values are loaded to the table.
Table will be saved.
This function will be call, if the calucalted DeltaY matches the critiria.
Passed arguments:
    TestX: x-values of test function
    TestY: y-values of test function
    DeltaY: Difference between TestY and IdealY
    index: Mentions which ideal-function the calculation is based on
'''
def SaveRow(TestX, TestY, DeltaY, index):
    import sqlalchemy 
    from sqlalchemy import create_engine, Column, Float, String #, MetaData
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    engine = create_engine('sqlite:///ForCalc.db')  # Connect to db
    Session = sessionmaker(bind=engine)  # Generate as session 
    session = Session()
    Base = declarative_base()

    class tresults(Base):  # Define table parameters
        __tablename__= 'Tresults'  # Define tablename
        id = Column(String, primary_key=True)  # Generate Column
        x = Column(Float)  # Generate Column
        Testy = Column(Float)  # Generate Column
        Delta = Column(Float)  # Generate Column
        IndexIdeal = Column(Float)  # Generate Column
    
    Base.metadata.create_all(engine)  # Create table
    idvalue = TestX + TestY + index  # Calculate idvalue, needed as a primary code

    solution1 = tresults(id = idvalue, x = TestX, Testy = TestY, Delta = DeltaY, IndexIdeal = index)  # Add values to a table row
    session.add(solution1)  # Add row to table
    session.commit()  # Commit changes

'''
The "plottable1" function loads data in a df and plots with predefined settings. 
Result is or more line graphs.
Passed arguments:
    tablename: Name of the table that should be plotted
    columcount: Number of columns that need to be plotted
'''
def plottable1(tablename, columncount):
    import matplotlib.pyplot as plt
    import pandas as pd

    engine = create_engine('sqlite:///ForCalc.db')  # Connect to DB
    table_df = pd.read_sql_table(
        tablename,
        con=engine)  # Define df
    plt.figure()  # Generate new figure
    for n in range(1, columncount):  # For every column (Column number was passed)
        X = table_df.iloc[:,0]  # Definition of x-values
        Y1 = table_df.iloc[:,n]  # Definition of y-values
        plt.plot(figsize=(6,4))
        plt.plot(X,Y1, color='#8A0808', linestyle='--',label=('Y' + str(n) ))  # Plot X and Y1
    
    plt.title(tablename + "dataset")
    plt.xlabel('x-Values')
    plt.ylabel('y-Values')
    plt.legend()
    plt.grid(True)
    plt.show

'''
The "plottable2" function loads data in a df and plots with predefined settings.
Difference to "plottable1" function: Instead of linegraphs, scatterplots are generated.
Result is one or more scatterplot.
Passed arguments:
    tablename: Name of the table that should be plotted
    columcount: Number of columns that need to be plotted
'''
def plottable2(tablename, columncount):
    import matplotlib.pyplot as plt
    import pandas as pd

    engine = create_engine('sqlite:///ForCalc.db')  # Connect to DB
    table_df = pd.read_sql_table(
        tablename,
        con=engine)  # Define df
    plt.figure()  # Generate new figure
    for n in range(1, columncount):   # For every column (Column number was passed)
        X = table_df.iloc[:,0]  # Definition of x-values
        Y1 = table_df.iloc[:,n] # Definition of y-values
        plt.plot(figsize=(6,4))
        plt.plot(X,Y1, 'o', color='black', label=('Y' + str(n))) # Plot X and Y1 as scatterplot
    plt.title(tablename + "dataset")
    plt.xlabel('x-Values')
    plt.ylabel('y-Values')
    plt.legend()
    plt.grid(True)
    plt.show
    
