import sqlite3
veritabani_yolu = 'veritabani.db'
connection = sqlite3.connect(veritabani_yolu)
cursor = connection.cursor()



class Employee():
    def __init__(self, pid, dep, position):
        self.pid = pid
        self.dep = dep
        self.position = position
        self.connection= None
        self.cursor= None

    def DBconnect(self):
        self.connection = sqlite3.connect(veritabani_yolu)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''create table if not exists Employ(Pid Text, Department Text, Position Text)''')
        self.connection.commit()

    def cut_connection(self):
        if self.connection:
            self.connection.close()
                          


    def add_staff(self):
        if self.connection and self.cursor:
            sorgu = "Insert Into Employ Values(?,?,?)"
            self.cursor.execute(sorgu, (self.pid, self.dep, self.position))
            self.connection.commit()
            print("Personel eklendi")
        else:
            print("Veritabanı ile bağlantı kurulamadı")


    def show_staff(self):
        if self.cursor:    
          self.cursor.execute("Select * from Employ")
          liste = self.cursor.fetchall()
        for p in liste:
            print("no",p[0],"bolum",p[1],"position",p[2])

     
if __name__ == "__main__":
    Mustafa = Employee('15','IK','Technician')
    Mustafa.DBconnect()
    Mustafa.add_staff()
    Mustafa.show_staff()