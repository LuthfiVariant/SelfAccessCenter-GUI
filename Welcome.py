from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import common.config
from common.config import user_login, user_register, user_detail, fetch_document, read_data, simpan_data, hapus_data, edit_data, update_data
from common.functions import RegisterWindow

#global variable
nim = None
passCandidate = None
nama = None

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


        self.logo = Image.open('images\\SAC_big.jpg')
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
        self.master.iconbitmap("images\\sac_small_GG7_icon.ico")
        self.master.title("Halaman Masuk")

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

        self.logo = Image.open('images\\SAC_big.jpg')
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

        self.submitLogin = Button(self.frame,text="Login", command=self.login)
        self.submitLogin.place(x=250, y=220)

        self.registerButton = Button(self.frame, text="Belum Punya Akun? Daftar", command=self.RegisterWindow)
        self.registerButton.place(x=0, y=270)
    
    def login(self):
        global nim
        global passCandidate
        nim = self.nimEntry.get()
        passCandidate = self.passwordEntry.get()

        if user_login(nim, passCandidate):
            messagebox.showinfo("Login", "Anda Berhasil Masuk")
            DashboardWindow(self.master)
        else:
            return messagebox.showerror("Loginn", "NIM atau Password Anda Salah")
    
    def RegisterWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = RegisterWindow(app)

    def DashboardWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = DashboardWindow(app)


class RegisterWindow(Frame):
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("images\\sac_small_GG7_icon.ico")
        self.master.title("Halaman Pendaftaran")

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

        self.submitDaftar = Button(self.frame,text="Daftar", command=self.register)
        self.submitDaftar.place(x=250, y=220)

        self.loginButton = Button(self.frame, text="Sudah Punya Akun? Masuk", command=self.LoginWindow)
        self.loginButton.place(x=0, y=270)

    def register(self):
        nama = self.namaEntry.get()
        nim = self.nimEntry.get()
        email = self.emailEntrty.get()
        password = self.passwordEntry.get()
        verifikasi = False

        if user_register(nama, nim, email, password, verifikasi):
            messagebox.showinfo("Daftar", "Akun anda berhasil didaftarkan")
            LoginWindow(self.master)
        else:
            return messagebox.showwarning("Daftar", "Terjadi kesalahan saat mendaftarkan akun anda. Silahkan coba lagi.")
    
    def LoginWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = LoginWindow(app)


class DashboardWindow(Frame):
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("images\\sac_small_GG7_icon.ico")
        self.master.title("Dashboard")

        self.canvas = Canvas(self.master, width=600, height=400, bg='white')
        self.canvas.place(x=0, y=0)

        #show window in center of the screen
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.master.geometry(str1)

        #disable resize of the window
        self.master.resizable(width=False, height=False)

        self.frame = Frame(self.master, height=300, width=450, bg='white')
        self.frame.place(x=80, y=50)
        
        user_detail(nim)
        global nama
        nama = str(user_detail.nama)

        skripsi = fetch_document(nama)

        
        length = len(skripsi)

        i = 0
        for i in range(length):
            jarak = i * 45


            id = skripsi[i][0]

            id = id

            print(id)

            judul = skripsi[i][1]

            print(judul)


            self.id = Label(self.frame, text=skripsi[i][0])
            self.id.place(x=80, y=150+jarak)
            
            self.judul = Label(self.frame, text=skripsi[i][1])
            self.judul.place(x=100, y=150+jarak)

            self.penulis = Label(self.frame, text=skripsi[i][2])
            self.penulis.place(x=100, y=175+jarak)

            self.downloadButton = Button(self.frame, text="Download", command=lambda: read_data(skripsi[i][5]), height=1, width=10)
            self.downloadButton.place(x=250, y=170+jarak)

        self.tambahSkripsi = Button(self.frame, text="Tambah Skripsi", command=self.AddWindow)
        self.tambahSkripsi.place(x=100, y=100)

        self.id = Entry(self.frame)
        self.id.place(x=200, y=100)

        self.hapus = Button(self.frame, text="Hapus", command=self.delete)
        self.hapus.place(x=300, y=100)

        self.editButton = Button(self.frame, text="Edit", command=self.edit)
        self.editButton.place(x=350, y=100)

    def edit(self):
        editor = Toplevel(self.master)
        editor.title("Edit Berkas")


        width = editor.winfo_screenwidth()
        height = editor.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        editor.geometry(str1)

        edit_data(self.id.get())

        data = edit_data.data

        self.judulEdit = Label(editor, text="Judul")
        self.judulEdit.config(font=("Courier", 12))
        self.judulEdit.place(x=30, y=20)

        self.judulEntry = Entry(editor, width=20)
        self.judulEntry.place(x=150, y=20)

        self.tahunEdit = Label(editor, text="Tahun")
        self.tahunEdit.config(font=("Courier", 12))
        self.tahunEdit.place(x=30, y=50)

        self.tahunEntry = Entry(editor, width=20)
        self.tahunEntry.place(x=150, y=50)

        self.abstrakEdit = Label(editor, text="abstrak")
        self.abstrakEdit.config(font=("Courier", 12))
        self.abstrakEdit.place(x=30, y=80)

        self.abstrakEntry = Text(editor, height=10, width=17)
        self.abstrakEntry.place(x=150, y=80)
            
        self.berkasEdit = Button(editor, text="Simpan Data", command=self.update)
        self.berkasEdit.config(font=("Courier", 12))
        self.berkasEdit.place(x=30, y=240)


        for record in data:
            self.judulEntry.insert(0, record[1])
            self.tahunEntry.insert(0, record[3])
            self.abstrakEntry.insert('1.0', record[4])

    def update(self):
        id = self.id.get()
        judul = self.judulEntry.get()
        penulis = nama
        tahun = self.tahunEntry.get()
        abstrak = self.abstrakEntry.get('1.0', END)
        if update_data(id, judul, penulis, tahun, abstrak):
            messagebox.showinfo("Berhasil", "Data berhasil di-edit")
        else:
            messagebox.showwarning("Gagal", "Data gagal di-edit")

    def AddWindow(self):
        self.master.withdraw()
        app = Toplevel(self.master)
        self.currentWindow = AddWindow(app)

    def delete(self):
        id = self.id.get()
        if hapus_data(id):
            messagebox.showinfo("Berhasil", "Data berhasil dihapus")
        else:
            messagebox.showerror("Gagal", "Data gagal dihapus")


class AddWindow(Frame):
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("images\\sac_small_GG7_icon.ico")
        self.master.title("Add Document")

        self.canvas = Canvas(self.master, width=600, height=400, bg='white')
        self.canvas.place(x=0, y=0)

        #show window in center of the screen
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.master.geometry(str1)

        #disable resize of the window
        self.master.resizable(width=False, height=False)

        self.frame = Frame(self.master, height=300, width=450, bg='white')
        self.frame.place(x=80, y=50)


        self.judulAdd = Label(self.frame, text="Judul")
        self.judulAdd.config(font=("Courier", 12))
        self.judulAdd.place(x=30, y=20)

        self.judulEntry = Entry(self.frame, width=20)
        self.judulEntry.place(x=150, y=20)

        self.tahunAdd = Label(self.frame, text="Tahun")
        self.tahunAdd.config(font=("Courier", 12))
        self.tahunAdd.place(x=30, y=50)

        self.tahunEntry = Entry(self.frame, width=20)
        self.tahunEntry.place(x=150, y=50)

        self.abstrakAdd = Label(self.frame, text="abstrak")
        self.abstrakAdd.config(font=("Courier", 12))
        self.abstrakAdd.place(x=30, y=80)

        self.abstrakEntry = Text(self.frame, height=10, width=17)
        self.abstrakEntry.place(x=150, y=80)
            
        self.berkasAdd = Button(self.frame, text="Simpan Data", command=self.simpan)
        self.berkasAdd.config(font=("Courier", 12))
        self.berkasAdd.place(x=30, y=240)

    def simpan(self):
        judul = self.judulEntry.get()
        tahun = self.tahunEntry.get()
        abstrak = self.abstrakEntry.get('1.0', END)
        penulis = nama
        if simpan_data(judul, penulis, tahun, abstrak):
            messagebox.showinfo("Berhasil", "Data anda berhasil dimasukkan")
            self.master.withdraw()
            app = Toplevel(self.master)
            self.currentWindow = DashboardWindow(app)
        else:
            messagebox.showwarning("Gagal", "Data anda gagal dimasukkan. Coba Kembali.")