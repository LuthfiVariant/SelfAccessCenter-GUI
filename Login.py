from tkinter import *
from tkinter import messagebox
import tkinter as Tk
import common.config



class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.grid(row=0, column=0)


        self.nimLabel = Label(self.root, text="NIM")
        self.nimLabel.grid(row=0, column=0, pady=20, padx=20)

        self.nimEntry = Entry(self.root)
        self.nimEntry.grid(row=0, column=1, pady=20, padx=20)

        self.passLabel = Label(self.root, text="Password")
        self.passLabel.grid(row=1, column=0, pady=20, padx=20)

        self.passEntry = Entry(self.root)
        self.passEntry.grid(row=1, column=1, pady=20, padx=20)

        submitButton = Button(self.root, text="Login", command=self.login)
        submitButton.grid(row=2, column=0, columnspan=2)

    def login(self):
        nim = self.nimEntry.get()
        passCandidate = self.passEntry.get()
        # validations
        if self.nimEntry.get() == "":
            messagebox.showinfo("Alert!","Enter Email First")
        elif self.passEntry.get() == "":
            messagebox.showinfo("Alert!", "Enter Password first")
        else:
            res = common.config.user_login(nim, passCandidate)
            if res:
                messagebox.showinfo("Message", "Login Successfully")
            else:
                messagebox.showinfo("ALert!", "Wrong username/password")
        
        

            
        

if __name__ == '__main__':
    root = Tk.Tk()
    root.geometry("400x400")
    app = MyApp(root)
    root.mainloop()