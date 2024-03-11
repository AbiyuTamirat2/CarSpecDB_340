# Team Abiyu and Scott
# CNE 340 Winter quarter 2024
# Final Project
# Car Specifications Database
# Due date March 20, 2024

# Import libraries
import pandas as pd
from sqlalchemy import create_engine
from matplotlib import pyplot as plt


# Define database connection
hostname = '127.0.0.1'
username = 'root'
pwd = ''
dbname = 'CarSpecDB'

# Create database connection engine
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=username, pw=pwd))

# Read data from Excel file
tables = pd.read_excel(r'C:\Users\abiyu\OneDrive - Renton Technical College\Documents\GitHub\CarSpecDB_340\Car '
                       r'Specifications Database.xlsx', header=0, index_col=None)

# Create connection to the database
connection = engine.connect()

tables.to_sql('car_specifications', con=engine, if_exists='replace')


df = pd.read_sql_table('car_specifications', engine.connect())

