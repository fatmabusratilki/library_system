from kitap import Kitap
class Kutuphane:
    def __init__(self):
        self.__kitaplar = {}
    
    def kitap_ekle(self, kitap: Kitap):
        if kitap.isbn in self.__kitaplar:
            raise ValueError(f"{kitap.ad} isimli kitap zaten kütüphanede mevcut!")
        self.__kitaplar[kitap.isbn] = kitap
        print(f"{kitap.ad} kütüphaneye eklendi.")
    
    def kitap_sil(self, isbn):
        if isbn in self.__kitaplar:
            silinen_kitap = self.__kitaplar.pop(isbn)
            print(f"{silinen_kitap.ad} kütüphaneden kaldırıldı.")
        else:
            print("Bu ISBN numarasına sahip kitap bulunamadı.")
    
    def kitaplari_goster(self):
        if not self.__kitaplar:
            print("Kütüphanede kitap bulunmamaktadır.")
        else:
            print("Kütüphanedeki Kitaplar: \n")
            for kitap in self.__kitaplar.values():
                print(kitap)
