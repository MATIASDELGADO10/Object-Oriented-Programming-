import sqlite3
class Kitap():
    def __init__(self,baslik,yazar):
        self.baslik = baslik
        self.yazar = yazar

class Uye():
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.kitaplar = list()
        self.aktifkitapsayi = 0
        self.favoriler = list()
    
    def odunc_al(self,kitap):
        if kitap in self.kitaplar:
            self.kitaplar.append(kitap)
            self.aktifkitapsayi += 1
    
    def teslim_et(self,kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
        else:
            print("Bu kitap listede yok")

    def favori_ekle():
        pass


class Kutuphane():
    def __init__(self):
        self.DBconnect()
    def DBconnect(self):
        self.baglanti = sqlite3.connect('.....')
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("create table if not exists Kitaplar(Baslik Text, Yazar Text)")
        self.baglanti.commit()
    
    def Baglanti_kes(self):
        pass

  
def kitap_ekle(self, kitap):
    # SQL sorgusunu tanımlıyoruz
    sorgu1 = "INSERT INTO Kitaplar (baslik, yazar) VALUES (?, ?)"
    
    # Kitap nesnesinin başlık ve yazar bilgilerini kullanarak sorguyu çalıştırıyoruz
    self.cursor.execute(sorgu1, (kitap.baslik, kitap.yazar))
    
    # Değişiklikleri kaydediyoruz
    self.cursor.connection.commit()  # commit() metodu connection üzerinden çağrılmalıdır


    def kitap_goster(self):
        aranan = input("kitap adını giriniz:")
        self.cursor.execute("Select * from Kitaplar Where Baslik = ?", aranan)
        print(self.cursor.fetchone())
        sonuc = self.cursor.fetchone()
        print(sonuc)
        if sonuc ==aranan:
            print("aranan kitap :(),()".format(kitap.baslik,kitap.yazar))
        else:
            print("kitap bulunamadı")


if __name__ == '__main__':
    k=Kitap("Python Ogren","Ali Yildiz")
    uye=Uye("Mustafa","Gök")
    uye.odunc_al(k)
    atu=Kutuphane()
    atu.kitap_ekle(k)



