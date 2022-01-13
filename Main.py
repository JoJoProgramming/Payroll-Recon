import tkinter as tk

#----Windows----#
payrollWindow = tk.Tk()
#----Titles----#
payrollWindow.title("Payroll Reconciliation")
#----Labels----#
loginLabel = tk.Label(payrollWindow,text="Login Credentials",width=13,height=3,font=("FS Elliot Pro",12))
uidLabel = tk.Label(payrollWindow,text="User ID:",width=10,height=2,font=("FS Elliot Pro Light",8))
upwLabel = tk.Label(payrollWindow,text="Pasword:",width=10,height=2,font=("FS Elliot Pro Light",8))
#----Entry----#
uidEntry = tk.Entry(payrollWindow)
upwEntry = tk.Entry(payrollWindow)
#----Grid----#
loginLabel.grid(column=0,row=0,columnspan=3)
uidLabel.grid(column=0,row=1)
uidEntry.grid(column=1,row=1)
upwLabel.grid(column=0,row=2)
upwEntry.grid(column=1,row=2)
#---Mainloop----#
payrollWindow.mainloop()
