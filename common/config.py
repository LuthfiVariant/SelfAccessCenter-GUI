import mysql.connector as mysql
from passlib.hash import sha256_crypt

data = None

con = mysql.connect(
        host = "localhost",
        user = "root",
        password = "kanaderu",
        database = "sac"
    )

cursor = con.cursor()

def user_login(nim, passCandidate):
    global data
    try:
        cursor.execute("SELECT * FROM akun WHERE nim=%s and password=%s", [nim, passCandidate])
        data = cursor.fetchone()
        return data
    except:
        return False

