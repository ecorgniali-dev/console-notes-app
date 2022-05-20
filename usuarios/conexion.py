import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    database = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]