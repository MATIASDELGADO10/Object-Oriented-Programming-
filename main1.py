import sqlite3

class Kitap:
    def __init__(self, baslik, yazar):
        self.baslik = baslik
        self.yazar = yazar


class Uye:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.kitaplar = []  # Ödünç alınan kitaplar
        self.favoriler = []  # Favori kitaplar

    def odunc_al(self, kutuphane, kitap):
        if kutuphane.kitap_var_mi(kitap):
            if kitap not in self.kitaplar:
                self.kitaplar.append(kitap)
                kutuphane.kitap_odunc_ver(kitap)
                print(f"{kitap.baslik} ödünç alındı.")
            else:
                print("Bu kitabı zaten ödünç aldınız.")
        else:
            print(f"{kitap.baslik} kütüphanede yok veya ödünç alınmış.")

    def teslim_et(self, kutuphane, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            kutuphane.kitap_teslim_al(kitap)
            print(f"{kitap.baslik} teslim edildi.")
        else:
            print("Bu kitap size ait değil.")

    def favorilere_ekle(self, kitap):
        if kitap not in self.favoriler:
            self.favoriler.append(kitap)
            print(f"{kitap.baslik} favorilere eklendi.")
        else:
            print("Bu kitap zaten favorilerde.")

    def favorileri_goster(self):
        if self.favoriler:
            print("Favori Kitaplarınız:")
            for kitap in self.favoriler:
                print(f"- {kitap.baslik} ({kitap.yazar})")
        else:
            print("Favoriler listeniz boş.")


class Kutuphane:
    def __init__(self):
        self.db_baglan()

    def db_baglan(self):
        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Kitaplar (
            Baslik TEXT,
            Yazar TEXT,
            Durum TEXT DEFAULT 'Mevcut'
        )
        """)
        self.baglanti.commit()

    def kitap_ekle(self, kitap):
        self.cursor.execute("INSERT INTO Kitaplar (Baslik, Yazar) VALUES (?, ?)", (kitap.baslik, kitap.yazar))
        self.baglanti.commit()
        print(f"{kitap.baslik} kütüphaneye eklendi.")

    def kitap_sil(self, baslik):
        self.cursor.execute("DELETE FROM Kitaplar WHERE Baslik = ?", (baslik,))
        self.baglanti.commit()
        print(f"{baslik} kütüphaneden silindi.")

    def kitap_var_mi(self, kitap):
        self.cursor.execute("SELECT * FROM Kitaplar WHERE Baslik = ? AND Durum = 'Mevcut'", (kitap.baslik,))
        return self.cursor.fetchone() is not None

    def kitap_odunc_ver(self, kitap):
        self.cursor.execute("UPDATE Kitaplar SET Durum = 'Ödünç Verildi' WHERE Baslik = ?", (kitap.baslik,))
        self.baglanti.commit()

    def kitap_teslim_al(self, kitap):
        self.cursor.execute("UPDATE Kitaplar SET Durum = 'Mevcut' WHERE Baslik = ?", (kitap.baslik,))
        self.baglanti.commit()

    def kitap_goster(self, baslik):
        self.cursor.execute("SELECT * FROM Kitaplar WHERE Baslik = ?", (baslik,))
        sonuc = self.cursor.fetchone()
        if sonuc:
            print(f"Kitap: {sonuc[0]}, Yazar: {sonuc[1]}, Durum: {sonuc[2]}")
        else:
            print(f"{baslik} kütüphanede bulunamadı.")

    def tum_kitaplari_listele(self):
        self.cursor.execute("SELECT * FROM Kitaplar")
        kitaplar = self.cursor.fetchall()
        if kitaplar:
            print("Kütüphanedeki Tüm Kitaplar:")
            for kitap in kitaplar:
                print(f"- {kitap[0]} ({kitap[1]}) - {kitap[2]}")
        else:
            print("Kütüphanede hiç kitap yok.")

    def baglanti_kapat(self):
        self.baglanti.close()


if __name__ == "__main__":
    kutuphane = Kutuphane()

    kitap1 = Kitap("Kırmızı Kuşlar", "Osman")
    kitap2 = Kitap("Atesten Gomlek", "Tunahan")
    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)

    uye = Uye("Kaya", "Deniz    ")
    kutuphane.kitap_goster("Kırmızı Kuşlar")
    uye.odunc_al(kutuphane, kitap1)
    uye.favorilere_ekle(kitap2)
    uye.favorileri_goster()
    uye.teslim_et(kutuphane, kitap1)

    kutuphane.tum_kitaplari_listele()
    kutuphane.kitap_sil("Atesten Gomlek")
    kutuphane.tum_kitaplari_listele()

    kutuphane.baglanti_kapat()
