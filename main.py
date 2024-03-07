# CNE 340 Winter quarter 2024
# Abiyu and Scott


import mysql.connector
import json
import requests


def connect_to_sql():
    connection = mysql.connector.connect(user='CarSpecDB', password='A2-lX@tZt5r50eG1', host='http://209.38.174.23/phpmyadmin/', database='CarSpecDB')

    return connection


# Create a cars table if it doesn't exist
def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (model VARCHAR(255), mpg FLOAT, cyl INT, disp FLOAT, hp INT, 
    drat FLOAT, wt FLOAT, qsec FLOAT, vs INT, am INT, gear INT, carb INT)''')


# Insert a new car record into the cars table
def add_new_car(cursor):
    cursor.execute('''INSERT INTO cars(model, mpg, cyl, disp, hp, drat, wt, qsec, vs, am, gear, carb) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')


def fetch_cars():
    response = requests.get('https://gist.github.com/noamross/e5d3e859aa0c794be10b')
    data = json.loads(response.text)
    return data


def main():
    conn = connect_to_sql()
    cursor = conn.cursor()
    create_table(cursor)


if __name__ == '__main__':
    main()

