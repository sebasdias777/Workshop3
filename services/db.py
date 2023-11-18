import pandas as pd
import json
import psycopg2


def connect():
    with open('C:/Users/CHZ/Desktop/ETL/Workshop3/services/db_config.json') as f:
        dbfile = json.load(f)
    
    connection = psycopg2.connect(
        host= dbfile['host'],
        user= dbfile['user'],
        password= dbfile['password'],
        database= dbfile['database'],
        port=5432
    )
    
    print("Database connection ok")
    return connection


def create_tables():
    connection = connect()
    cursor = connection.cursor()
    Tabla = f"""CREATE TABLE IF NOT EXISTS prediccion (
        id serial primary key,
        Happiness_Score float,
        GDP_per_capita float,
        Social_support float,
        Healthy_life_expectancy float,
        Freedom float,
        Prediccion_H float
        )
        """
    cursor.execute(Tabla)
    connection.commit()

def insert(df):
    connection = connect()
    cursor = connection.cursor()
    create_tables()
    row = df.iloc[0]
    query = f"INSERT INTO prediccion (Happiness_Score, GDP_per_capita, Social_support, Healthy_life_expectancy, Freedom, Prediccion_H) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (row["Happiness Score"], row["GDP per capita"], row["Social support"], row["Healthy life expectancy"], row["Freedom"], row["Prediccion_H"]))
    connection.commit()
    connection.close()
