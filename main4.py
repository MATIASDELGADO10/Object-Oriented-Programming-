import tkinter as tk

class Uygulama():
    def __init__(self):
        print("pencere")
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root,padx=20, pady=20, bg="red")
        
        self.frame.pack()
        self.root.mainloop()


if __name__ == "__main__":
    a = Uygulama()
    a.mainloop()
