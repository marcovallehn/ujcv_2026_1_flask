import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ujcv_2026_2_progra2',
        ssl_disabled=True  # Desactiva SSL
    )
