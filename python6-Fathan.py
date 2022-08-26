print("1. persegi")
s = int(input("masukan nilai sisi: "))
luas_p = s * s
print("luas persegi adalah", luas_p)

print("2. persegi panjang")
p = int(input("masukan nilai panjang: "))
l = int(input("masukan nilai lebar: "))
luas_pj = p * l
print("luas persegi panjang adalah", luas_pj)

print("3. segitiga")
a = int(input("masukan nilai alas: "))
t = int(input("masukan nilai tinggi: "))
luas_s = a * t / 2
print("luas segitiga adalah", luas_s)

print("4. jajargenjang")
a = int(input("masukan nilai alas: "))
t = int(input("masukan nilai tinggi: "))
luas_jg = a * t
print("luas jajargenjang adalah", luas_jg)

print("5. lingkaran")
r = int(input("masukan nilai jari jari lingkaran: "))
luas_l = r * r * 3.14
print("luas lingkaran adalah", luas_l)