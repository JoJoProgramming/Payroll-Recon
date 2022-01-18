import tkinter as tk

STANDARD_FONT = ("FS Elliot Pro", 12)

class AppFrame(tk.Tk):
    windowList = {}
    __init__(self, *arg, **kwarg):
        #initializing Tk to build the frame with arguments)
        tk.Tk.__init__(self, *arg, **kwarg)
        appContainer = tk.Frame(self)
        appContainer.pack(side = "top", fill = "both", expand = True)
        #stating the app window has priority
        appContainer.grid_rowconfigure(0, weight = 1)
        appContainer.grid_columnconfigure(0, weight = 1)
        appContainer.geometry("400x400")
        #empty list to contain windows of the app
        self.windows = {}
        #W is the variable each window is mapped to in the For loop
        for W in windowList:
            frame = W(appContainer, self)
            self.windows[W] = frame
            frame.grid(row=0, column=0, sticky = "nsew")
        #initializes program using window HomeWindow
        self.show_frame(HomeWindow)
    
    def show_frame(self, cont):
        #cont indicates that the self.frames is within the init method
        frame = self.windows[cont]
        frame.tkraise()

#adds page to window
class StartPage(tk.Frame):
    #init here requires 3 arguments as the parent init uses 3 arguments
    #parent here refers to the mainapp class
    #parent is seen as the argument, controller is seen as the keyword argument
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #STANDARD_FONT is a global variable
        label = tk.Label(self, text = "Start Page", font = STANDARD_FONT)
        label.pack(pady = 10, padx = 10)
        button1 = tk.Button(self, text = "Visit Page 1",
         command = lambda: controller.show_frame(PageOne))
        button1.pack()