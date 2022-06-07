from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Hack NF", "12")
        self.primeiroContainer = Frame(master, background="red")
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.terceiroContainer = Frame(master, background="red")
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master, background="red")
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="YouTube MP3 Converter", background="red")
        self.titulo["font"] = ("Hack NF", "16", "bold")
        self.titulo.pack()
    
        self.senhaLabel = Label(self.terceiroContainer, text="Link:", font=self.fontePadrao, background="red")
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Baixar .mp3"
        self.autenticar["font"] = ("Hack NF", "12")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao, background="red")
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
Application(root)
root.configure(background="red")
root.mainloop()