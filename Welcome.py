from tkinter import *
from PIL import ImageTk, Image


class WelcomeWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self._initialize_view(master)

    def _initialize_view(self, master):
        self.master.title("Self Access Center")

        self.canvas = Canvas(self.master, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.master.geometry(str1)

        #disable resize of the window
        self.master.resizable(width=False, height=False)

        self.frame = Frame(self.master, height=300, width=450)
        self.frame.place(x=80, y=50)


        self.logo = Image.open('images\\logo-upi-removebg-preview.png')
        self.logo2 = self.logo.resize((100,100), Image.ANTIALIAS)
        self.logo3 = ImageTk.PhotoImage(self.logo2)
        
        self.labelLogo = Label(self.frame, image=self.logo3)
        self.labelLogo.place(x=170, y=20)

        self.welcomeTitle = Label(self.frame, text="Selamat Datang di Self Access Center")
        self.welcomeTitle.config(font=("Courier", 12, 'bold'))
        self.welcomeTitle.place(x=50, y=200)

        self.loginButton = Button(self.frame, text="Masuk", command=self.LoginWindow)
        self.loginButton.config(font=("Courier", 8, "italic"))
        self.loginButton.place(x=50, y=250)

        self.registerButton = Button(self.frame, text="Daftar", command=self.RegisterWindow)
        self.registerButton.config(font=("Courier", 8, "italic"))
        self.registerButton.place(x=350, y=250)

    def LoginWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = LoginWindow(app)
    
    def RegisterWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = RegisterWindow(app)

class LoginWindow(Frame):
    def __init__(self, master):
        self.master = master

        self.master.title("Halaman Login")

        self.canvas = Canvas(self.master, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.master.geometry(str1)

        #disable resize of the window
        self.master.resizable(width=False, height=False)

        self.frame = Frame(self.master, height=300, width=450)
        self.frame.place(x=80, y=50)

        self.logo = Image.open('images\\logo-upi-removebg-preview.png')
        self.logo2 = self.logo.resize((100,100), Image.ANTIALIAS)
        self.logo3 = ImageTk.PhotoImage(self.logo2)
        
        self.labelLogo = Label(self.frame, image=self.logo3)
        self.labelLogo.place(x=170, y=20)

        self.nimEntryLabel = Label(self.frame, text="NIM")
        self.nimEntryLabel.config(font=("Courier", 12))
        self.nimEntryLabel.place(x=100, y=150)

        self.nimEntry = Entry(self.frame)
        self.nimEntry.place(x=220, y=150)

        self.passwordEntryLabel = Label(self.frame, text="Password")
        self.passwordEntryLabel.config(font=("Courier", 12))
        self.passwordEntryLabel.place(x=100, y=180)

        self.passwordEntry = Entry(self.frame, show="*")
        self.passwordEntry.place(x=220, y=180)

        self.submitLogin = Button(self.frame,text="Login")
        self.submitLogin.place(x=250, y=220)

        self.registerButton = Button(self.frame, text="Belum Punya Akun? Daftar", command=self.RegisterWindow)
        self.registerButton.place(x=0, y=270)
    
    def RegisterWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = RegisterWindow(app)

class RegisterWindow(Frame):
    def __init__(self, master):
        self.master = master

        self.master.title("Halaman Login")

        self.canvas = Canvas(self.master, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.master.geometry(str1)

        #disable resize of the window
        self.master.resizable(width=False, height=False)

        self.frame = Frame(self.master, height=300, width=450)
        self.frame.place(x=80, y=50)


        self.namaEntryLabel = Label(self.frame, text="Nama")
        self.namaEntryLabel.config(font=("Courier", 12))
        self.namaEntryLabel.place(x=100, y=90)

        self.namaEntry = Entry(self.frame)
        self.namaEntry.place(x=220, y=90)

        self.nimEntryLabel = Label(self.frame, text="NIM")
        self.nimEntryLabel.config(font=("Courier", 12))
        self.nimEntryLabel.place(x=100, y=120)

        self.nimEntry = Entry(self.frame)
        self.nimEntry.place(x=220, y=120)

        self.emailEntryLabel = Label(self.frame, text="Email")
        self.emailEntryLabel.config(font=("Courier", 12))
        self.emailEntryLabel.place(x=100, y=150)

        self.emailEntrty = Entry(self.frame)
        self.emailEntrty.place(x=220, y=150)

        self.passwordEntryLabel = Label(self.frame, text="Password")
        self.passwordEntryLabel.config(font=("Courier", 12))
        self.passwordEntryLabel.place(x=100, y=180)

        self.passwordEntry = Entry(self.frame, show="*")
        self.passwordEntry.place(x=220, y=180)

        self.submitDaftar = Button(self.frame,text="Daftar")
        self.submitDaftar.place(x=250, y=220)

        self.loginButton = Button(self.frame, text="Sudah Punya Akun? Masuk", command=self.LoginWindow)
        self.loginButton.place(x=0, y=270)
    
    def LoginWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = LoginWindow(app)

    





        