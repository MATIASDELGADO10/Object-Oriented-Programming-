import tkinter 
from tkinter import ttk
from tkinter.messagebox import showinfo

class Uygulama(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ana Pencere")
        self.geometry("300x200")
        self.label = ttk.Label(self, text="Hosgeldiniz")
        self.label.pack()
        self.button = ttk.Button(self, text="Tıkla", command=self.button_clicked)
        self.button.pack()
    def button_clicked(self):
        showinfo(title= "Bilgilendirme", message="bilgilendirme yapildi...")


if __name__=="__main__":
    u = Uygulama()
    u.mainloop()

        


