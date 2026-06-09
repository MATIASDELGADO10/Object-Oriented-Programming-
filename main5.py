import tkinter as tk
from tkinter.messagebox import showinfo

class Uygulama():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2 Frameli Pencere")
        self.root.geometry("800x600")  # Pencere boyutunu belirle

        # Frame'leri oluştur ve değişkenlere ata
        self.frame1 = tk.Frame(self.root, bg="black", padx=20, pady=20)
        self.frame1.pack(side="left", fill="both", expand=True)

        self.frame2 = tk.Frame(self.root, bg="red", padx=20, pady=20)
        self.frame2.pack(side="right", fill="both", expand=True)
        
        self.button1 = tk.Button(self.frame1, text="Button 1", command=self.button1_clicked)
        self.button1.pack()
        self.label1 = tk.Label(self.frame1, text="Frame 1 Label", bg="black", fg="white")
        self.label1.pack()


        self.button2 = tk.Button(self.frame2,text="Button2" , command=self.button2_clicked)
        self.button2.pack()
        self.label2 = tk.Label(self.frame2, text="Frame 2 Label", bg="red", fg="white")
        self.label2.pack()
        
        self.root.mainloop()
    def button1_clicked(self):
        showinfo(title= "Buton1", message="Buton 1'e basıldı")
    def button2_clicked(self):
        showinfo(title= "Buton2", message="Buton 2'ye basıldı")


if __name__ == "__main__":
    a = Uygulama()









