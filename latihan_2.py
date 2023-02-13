'''
Buatlah progam menghitung luas bangun datar menggunakan fungsi.
- segitiga
- sersegi Panjang
'''

def luas_s(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print("luas segitiga adalah", luas)

luas_s(6,5)

def luas_pp(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang adalah", luas)

luas_pp(23,14)