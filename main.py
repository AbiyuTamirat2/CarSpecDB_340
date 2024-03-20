# Team Abiyu and Scott
# CNE 340 Winter quarter 2024
# Final Project
# Car Specifications Database
# Due date March 20, 2024

# Import libraries
import mysql.connector
import json
import requests
import pandas as pd
# from sqlalchemy import create_engine
from matplotlib import pyplot as plt


# Function to connect to MySQL database
def connect_to_sql():
    connection = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='CarSpecDB1')
    return connection


# Function to read car data from CSV
def fetch_cars():
    data = pd.read_csv(
        r"C:\Users\abiyu\OneDrive - Renton Technical College\Documents\GitHub\CarSpecDB_340\carsdatabase.csv")
    return data.to_dict('records')


# Function to create 'Cars' table if not exists
def create_table(cursor):
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Cars (id INT PRIMARY KEY auto_increment, model TEXT, mpg TEXT, cylinders TEXT, 
        displacement TEXT, horsepower TEXT, drag_efficiency TEXT, weight TEXT)''')


# Function to add a new car to database
def add_new_car(cursor, car):
    try:
        model = car['model']
        mpg = car.get('mpg', "NA")
        cyl = car.get('cyl', "NA")
        disp = car.get('disp', "NA")
        hp = car.get('hp', "NA")
        drat = car.get('drat', "NA")
        wt = car.get('wt', "NA")
        cursor.execute(
            'INSERT INTO Cars (model, mpg, cylinders, displacement, horsepower, drag_efficiency, weight) VALUES(%s, '
            '%s, %s, %s, %s, %s, %s)',
            (model, mpg, cyl, disp, hp, drat, wt))
        print(f'New Car added to DB {car["model"]}')
    except KeyError as e:
        print(f"Error: Missing key {e} in car data. Skipping car")


# Function to check if car already exists in database
def check_if_car_exists(cursor, car):
    model = car['model']
    query = "SELECT * FROM Cars WHERE model = %s"
    cursor.execute(query, (model,))
    return cursor.fetchall()


# Function to delete a car from database
def delete_car(cursor, car):
    model = car['model']
    query = "DELETE FROM Cars WHERE model = %s"
    cursor.execute(query, (model,))


# Function to add a car or print if it already exists
def add_or_print_car(cursor, fetched_cars):
    for car in fetched_cars:
        if not check_if_car_exists(cursor, car):
            add_new_car(cursor, car)
            print(f'New Car added to DB {car["model"]}')
        else:
            print(f'Existing Car found in DB {car["model"]}')


# Main function to execute the script
def main():
    # Establish connection to the database
    conn = connect_to_sql()
    # Create a cursor object
    cursor = conn.cursor()
    # Create the 'Cars' table in the database
    create_table(cursor)
    # Fetch car data
    fetched_cars = fetch_cars()
    # Add or print cars
    add_or_print_car(cursor, fetched_cars)
    # Commit changes to the database
    conn.commit()
    # Close the database connection
    conn.close()


# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()
