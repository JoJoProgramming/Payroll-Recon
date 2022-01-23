import tkinter as tk
import string as str
from tkinter import ttk

LARGE_FONT = ("FS Elliot Pro", 12)
STANDARD_FONT = ("FS Elliot Pro Light", 8)
ALPHABET_LIST = str.ascii_lowercase
USER_ID = ""
USER_PASSWORD = ""

class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.geometry("400x400")
        #self.title("Payroll Reconciliation")
        rootFrame = tk.Frame(self)
        rootFrame.grid(column = 0, row = 0, sticky = "nsew")
        rootFrame.grid_columnconfigure(0, weight = 1)
        rootFrame.grid_rowconfigure(0, weight = 1)
        self.frames = {}
        for F in (LoginPage, SearchCriteriaPage):
            frame = F(rootFrame, self)
            self.frames[F] = frame
        self.Show_Frame(LoginPage)

    def Show_Frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
        

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        loginLabel = ttk.Label(self, text = "Login Information", font = LARGE_FONT)
        loginLabel.grid(row = 0, column = 1)
        uidLabel = ttk.Label(self, text = "User ID:", font = STANDARD_FONT)
        upwLabel = ttk.Label(self, text = "User Password:", font = STANDARD_FONT)
        uidEntry = ttk.Entry(self)
        upwEntry = ttk.Entry(self)
        uidLabel.grid(row = 1, column = 0)
        uidEntry.grid(row = 1, column = 1)
        upwLabel.grid(row = 2, column = 0)
        upwEntry.grid(row = 2, column = 1)
        loginButton = ttk.Button(self, text = "Login",
         command = lambda: Root.Show_Frame(SearchCriteriaPage))
        loginButton.grid(row = 3, column = 1, columnspan = 2)

class SearchCriteriaPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight = 1)
        contractLabel = ttk.Label(self, text = "Contract Number:", font = STANDARD_FONT)
        contractEntry = ttk.Entry(self)
        contractEntry.insert(0, "6-digit Contract Number")
        contractEntry.grid_columnconfigure(0, weight = 1)
        contractLabel.grid(row = 1, column = 0)
        contractEntry.grid(row = 1, column = 0)
        logoutButton = ttk.Button(self, text = "Logout",
         command = lambda: Root.Show_Frame(LoginPage))
        logoutButton.grid(row = 3, column = 1)


mainApp = Root()
mainApp.mainloop()