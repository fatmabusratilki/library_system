from kütüphane import Kutuphane
from kitap import Kitap

# Örnek Kullanım
kutuphane = Kutuphane()

kitap1 = Kitap("1984", "George Orwell", 328, "1234567890")
kitap2 = Kitap("Hayvan Çiftliği", "George Orwell", 152, "0987654321")

try:
    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)
    kutuphane.kitap_ekle(kitap1)  # Aynı kitabı eklemeye çalışıyoruz
except ValueError as e:
    print(f"Hata: {e}")

kutuphane.kitaplari_goster()
kutuphane.kitap_sil("1234567890")
kutuphane.kitaplari_goster()
