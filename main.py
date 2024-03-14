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
#from sqlalchemy import create_engine
from matplotlib import pyplot as plt

def connect_to_sql():
    connection = mysql.connector.connect(user='CarSpecDB', password='A2-lX@tZt5r50eG1', host='209.38.174.23', database='CarSpecDB')
    return connection

def fetch_cars():
    data = pd.read_csv("C:\\Users\\Scott\\PycharmProjects\\CarSpecDB_340\\carsdatabase.csv")
    return data.to_dict('records')

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Cars (id INT PRIMARY KEY auto_increment, model TEXT, mpg TEXT, cylinders TEXT, displacement TEXT, horsepower TEXT, drag_efficiency TEXT, weight TEXT)''')

def add_new_car(cursor, car):
    try:
        model = car['model']
        mpg = car.get('mpg', "NA")
        cyl = car.get('cylinders', "NA")
        disp = car.get('displacement', "NA")
        hp = car.get('horsepower', "NA")
        drat = car.get('drag_efficiency', "NA")
        wt = car.get('weight', "NA")
        cursor.execute('INSERT INTO Cars (model, mpg, cylinders, displacement, horsepower, drag_efficiency, weight) VALUES(%s, %s, %s, %s, %s, %s, %s)', (model, mpg, cyl, disp, hp, drat, wt))
        print(f'New Car added to DB {car["model"]}')
    except KeyError as e:
        print(f"Error: Missing key {e} in car data. Skipping car")

def check_if_car_exists(cursor, car):
    model = car['model']
    query = "SELECT * FROM Cars WHERE model = %s"
    cursor.execute(query, (model,))
    return cursor.fetchall()

def delete_car(cursor, car):
    model = car['model']
    query = "DELETE FROM Cars WHERE model = %s"
    cursor.execute(query, (model,))

def add_or_print_car(cursor, fetched_cars):
    for car in fetched_cars:
        if not check_if_car_exists(cursor, car):
            add_new_car(cursor, car)
            print(f'New Car added to DB {car["model"]}')
        else:
            print(f'Existing Car found in DB {car["model"]}')

def main():
    conn = connect_to_sql()
    cursor = conn.cursor()
    create_table(cursor)
    fetched_cars = fetch_cars()
    add_or_print_car(cursor, fetched_cars)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()