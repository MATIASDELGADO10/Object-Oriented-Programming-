from abc import ABC, abstractmethod

class Belge(ABC):
    def belge_isle(self):
        self.belge_ac()
        self.veri_oku()
        self.veri_isle()
        self.belge_kaydet()
        print(f"{self.dosya_adi} islendi")

    @abstractmethod
    def belge_ac(self):
        pass

    abstractmethod
    def veri_oku(self):
        pass

    @abstractmethod
    def veri_isle(self):
        pass

    @abstractmethod
    def belge_kaydet(self):
        pass



class PDF(Belge):
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
    
    def belge_ac(self):
        print(f"{self.dosya_adi} acildi")


class Word(Belge):
    def __init__(self,path):
        self.path = path





