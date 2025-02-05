class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, isbn):
        self.__ad = ad
        self.__yazar = yazar
        self.__sayfa_sayisi = sayfa_sayisi
        self.__isbn = isbn
    
    @property
    def ad(self):
        return self.__ad
    
    @property
    def yazar(self):
        return self.__yazar
    
    @property
    def sayfa_sayisi(self):
        return self.__sayfa_sayisi
    
    @property
    def isbn(self):
        return self.__isbn
    
    def __str__(self):
        return f"{self.ad} - {self.yazar} - {self.sayfa_sayisi} sayfa - ISBN: {self.isbn}"