from tkinter import *
from Welcome import WelcomeWindow, LoginWindow, RegisterWindow, DashboardWindow, AddWindow

class App:

    def __init__(self):
        self.master = Tk()
        self.master.iconbitmap("images\\sac_small_GG7_icon.ico")
        self.curretWindow = LoginWindow(self.master)

    def run(self):
        self.master.mainloop()
        

if __name__ == "__main__":
    app = App()
    app.run()