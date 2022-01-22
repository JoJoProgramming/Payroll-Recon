import tkinter as tk
import string as str

LARGE_FONT = ("FS Elliot Pro", 12)
STANDARD_FONT = ("FS Elliot Pro Light", 8)
ALPHABET_LIST = str.ascii_lowercase
USER_ID = ""
USER_PASSWORD = ""

root = tk.Tk()
root.title = "Payroll Reconciliation"
root.iconbitmap("C:\Programs\Python\Payroll_Recon\Resources\PFG Logo.png")
root.geometry("400x400")

class MainApp:
    def __init__(self, root):
        self.loginFrame = tk.Frame(root)
        self.show_frame(LoginPage)
    
    def show_frame(self, root):


class LoginPage(tk.Frame):
    #initializes object
    def __init__(self, root):
    #intializes class tk.Frame
        tk.Frame.__init__(self, root)
        self.uidLabel = tk.Label(self, text = "User ID:", font = STANDARD_FONT)
        self.upwLabel = tk.Label(self, text = "User Password:", font = STANDARD_FONT)
        self.uidEntry = tk.Entry(self)
        self.upwEntry = tk.Entry(self)
        self.loginButton = tk.Button(self1, text="Login", font=STANDARD_FONT, command = ButtonFunctions.userLogin)
        self.uidLabel.grid(row = 1, column = 0)
        self.upwLabel.grid(row = 2, column = 0)
        self.uidEntry.grid(row = 1, column = 1)
        self.upwEntry.grid(row = 2, column = 1)
        self.loginButton.grid(row = 3, column = 0, columnspan = 2)

class ButtonFunctions:
    def userLogin():
        USER_ID = login.uidEntry.get()
        USER_PASSWORD = login.upwEntry.get()
        #return len(USER_ID) == 7 and USER_ID[0].lower() in ALPHABET_LIST and len(USER_PASSWORD) > 0 and len(USER_PASSWORD) <= 8
    



login = MainApp(root)
print(USER_ID)
print(USER_PASSWORD)
root.mainloop()