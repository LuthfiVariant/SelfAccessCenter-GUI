from tkinter import *
from Welcome import WelcomeWindow, LoginWindow, RegisterWindow

class App:

    def __init__(self):
        self.master = Tk()
        self.curretWindow = WelcomeWindow(self.master)

    def run(self):
        self.master.mainloop()
        

if __name__ == "__main__":
    app = App()
    app.run()