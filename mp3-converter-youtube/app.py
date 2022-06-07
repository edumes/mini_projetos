from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Youtube MP3 Converter")
        self.msg["font"] = ("Hack NF", "16", "bold")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Baixar .mp3"
        self.sair["font"] = ("Hack NF", "16")
        self.sair["width"] = 12
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

root = Tk()
Application(root)
root.mainloop()