from mimetypes import init
from pprint import pprint
from unittest import result
import requests
import time
import json
import sqlite3
import mysql.connector

def get_service():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1600&offset=0'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                pokename = x['name']
                write_db(pokename)


def write_db(pokename):
    conexion = mysql.connector.connect(
        user='root',
        password='feisima54321',
        host='localhost',
        database='Pokemones',
        port='3306'
    )
    mycursor = conexion.cursor()
    sql = "INSERT INTO poke(pokename) VALUES ('{0}')".format(pokename)
    mycursor.execute(sql)
    conexion.commit()


if __name__ == "__main__":
    init_time = time.time()
 
    get_service()  
    end_time = time.time() - init_time
    print(end_time)