from abc import ABC, abstractmethod

class Arac(ABC):
    def __init__(self,marka,model,yıl,):
        self.marka = marka
        self.model = model
        self.yıl = yıl
       
        self.hız = 0
    
    @abstractmethod
    def hızlan(self,miktar):
        pass
    @abstractmethod   
    def yavasla(self,miktar):
        pass

    def arac_bılgılerı(self):
        print(f"This is a {self.marka} model is {self.model}, year is {self.yıl}, color of this car is {self.renk} and speed is {self.hız}")
    

class Otomobil(Arac):
    def __init__(self, marka, model, yıl,otomatik):
        super().__init__(marka, model, yıl)
        self.otomatik = otomatik
    

    def hızlan(self, miktar):
        self.hız += miktar
        print(f"{self.model} hizi {self.hız}km/sn")


    def arac_bılgılerı(self):
        return super().arac_bılgılerı()

if __name__== "__main__":
    pass