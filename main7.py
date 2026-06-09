from abc import ABC, abstractmethod

class Arac(ABC):
    def seyahat_et(self,mesafe,marka):
        self.marka = marka
        self.hızlan()
        self.yavasla()
        self.yol_gidisi(mesafe)
        print (f"{self.marka} yol katteti")
     
    @abstractmethod
    def hızlan(self,miktar):
        pass
    @abstractmethod   
    def yavasla(self,miktar):
        pass
    @abstractmethod
    def yol_gidisi(self,mesafe):
        print(f"Araba yolunda {mesafe} km kattetti")


class Otomobil(Arac):
    def __init__(self,marka,model,yıl,):
        self.marka = marka
        self.model = model
        self.yıl = yıl
        self.hız = 0
    
    def hızlan(self, vites):
        self.hız += vites
        print(f"{self.model} hizi {self.hız}km/sn")


class Motor(Arac):
    def __init__(self,marka,model,silindir_hacmi):
        self.marka = marka
        self.model = model
        self.silindir_hacmi = silindir_hacmi

    def hızlan(self, miktar,silindir_hacmi):
        self.hız += miktar * silindir_hacmi
        print(f"{self.model} hizi {self.hız}km/sn")


if __name__ == "__main__":
    otomobil = Otomobil("Toyota","Corolla",2020)
   





     
       





 
    