import mysql.connector as mysql
from passlib.hash import sha256_crypt


con = mysql.connect(
        host = "localhost",
        user = "root",
        password = "kanaderu",
        database = "sac"
    )

cursor = con.cursor()

def user_login(nim, passCandidate):
    try:
        cursor.execute("SELECT * FROM akun WHERE nim=%s and password=%s", [nim, passCandidate])
        return cursor.fetchone()
    except:
        return False