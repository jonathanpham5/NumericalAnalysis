import time
from Tkinter import *
from ttk import *

class App(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.s = Style()
        self.root.s.theme_use("clam")
        self.root.title("Numerical Analysis - Project 2")
        
        Frame.__init__(self, self.root)
        self.createWidgets()
        self.pack()

    def wait(self):
        while not w.can_make_request():
            time.sleep(1)

    def createWidgets(self):
        self.grid()

        # Application Widgets
        self.testLabel = Label(self, text = "Numerical Analysis")

        # Grid placement of Widgets
        self.testLabel.grid(row = 0, column = 0)
    
    def start(self):
        self.root.mainloop()

        
# create the application
gui = App()

# start the program
gui.start()
