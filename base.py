import mysql.connector
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer le mot de passe de la base de données à partir des variables d'environnement
db_password = os.environ.get('DB_PASS')

def connecter():
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password=db_password,
    database='laetydb'
    # database='teste2'
    )
    return db