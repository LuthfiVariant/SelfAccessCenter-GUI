import mysql.connector as mysql
from passlib.hash import sha256_crypt
from tkinter import messagebox,filedialog
from tkinter import *
import smtplib
import os

con = mysql.connect(
        host = "localhost",
        user = "root",
        password = "kanaderu",
        database = "sac"
    )

cursor = con.cursor()

def user_login(nim, passCandidate):
    try:
        cursor.execute("SELECT * FROM akun WHERE nim=%s", [nim])
        data = cursor.fetchone()
        password = data[3]
        user_login.nama = data[1]
        if sha256_crypt.verify(passCandidate, password):
            return True
        else:
            return messagebox.showerror("Login", "Password Anda Salah") 
    except:
        return False

def user_detail(nim):
    try:
        cursor.execute("SELECT * FROM akun WHERE nim=%s", [nim])
        data = cursor.fetchone()
        user_detail.nama = data[1]
    except:
        return False


def user_register(nama, nim, email, password, verifikasi):
    try:
        password_hash = sha256_crypt.encrypt(str(password))
        cursor.execute("INSERT INTO akun (nama, nim, email, password, verifikasi) VALUES (%s,%s,%s,%s,%s)", [nama, nim, email, password_hash, False])
        return True
    except:
        return False

def fetch_document(nama):
    try:
        hasil = cursor.execute("SELECT * FROM skripsi WHERE penulis LIKE %s", [nama])
        data = cursor.fetchall()
        return data
    except:
        return False

def read_data(bytes, filename):
    fn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File", defaultextension=".pdf", filetypes=(("PDF file", "*.pdf"), ("All Files", "*.*")))

    with open(fn, "wb") as f:
        f.write(bytes)
    f.close()
    messagebox.showinfo("Success", "Save Successful")