class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, isbn):
        self.__ad = ad
        self.__yazar = yazar
        self.__sayfa_sayisi = sayfa_sayisi
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"Kitap: {self.__ad}, Yazar: {self.__yazar}, Sayfa Sayısı: {self.__sayfa_sayisi}, ISBN: {self.__isbn}"

class KitapZatenVarHatasi(Exception):
    pass

class Kutuphane:
    def __init__(self):
        self.__kitaplar = []  

    def kitap_ekle(self, kitap):
    
        for k in self.__kitaplar:
            if k.get_isbn() == kitap.get_isbn():
                raise KitapZatenVarHatasi(f"{kitap.get_isbn()} ISBN numaralı kitap zaten mevcut!")
        self.__kitaplar.append(kitap)
        print(f"{kitap.get_isbn()} ISBN'li kitap başarıyla eklendi.")

    def kitap_sil(self, isbn):
        for kitap in self.__kitaplar:
            if kitap.get_isbn() == isbn:
                self.__kitaplar.remove(kitap)
                print(f"{isbn} ISBN'li kitap başarıyla silindi.")
                return
        print(f"{isbn} ISBN'li kitap bulunamadı.")

    def kitaplari_goster(self):
        if not self.__kitaplar:
            print("Kütüphane boş!")
        else:
            for kitap in self.__kitaplar:
                print(kitap)

try:
    kutuphane = Kutuphane()

    kitap1 = Kitap("Python Programlama", "Guido van Rossum", 450, "12345")
    kitap2 = Kitap("Yapay Zeka", "John McCarthy", 300, "67890")
    kitap3 = Kitap("Python Programlama", "Guido van Rossum", 450, "12345")  # Aynı ISBN

    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)
    kutuphane.kitap_ekle(kitap3)  

except KitapZatenVarHatasi as e:
    print("Hata:", e)


kutuphane.kitaplari_goster()
