#1.Mengitung rata-rata
print("--Menghitung rata-rata nilai--")
a=3
b=7
c=5
d=2
e=9
rerata=(a+b+c+d+e)/5
print("Nilai masukan: ",a,b,c,d,e)
print("Hasil rata-rata nilai: ",rerata)
print()

#2.Menghitung luas dan keliling bangun datar
print("--Menghitung luas dan keliling segitiga--")
a=float(input("Masukkan alas segitiga: "))
t=float(input("Masukkan tinggi segitiga: "))
b=float(input("Masukkan sisi b: "))
c=float(input("Masukkan sisi c: "))
luas=0.5*a*t
keliling=a+b+c
print("Hasil luas segitiga: ",luas)
print("Hasil keliling segitiga: ",keliling)
print()

#3.Menghitung BMI
print("--Menghitung index massa tubuh/BMI--")
tinggi=float(input("Masukkan tinggi badan anda(meter): "))
berat=float(input("Masukkan berat badan anda: "))
bmi=berat/(tinggi)**2
print("Hasil BMI anda adalah: ",bmi)
if bmi < 18.5:
    print("Berat badan anda kurang, perbaiki pola makan ya")
elif bmi >= 18.5 and bmi < 22.5:
    print("Berat badan anda normal")
elif bmi >= 23 and bmi < 29.9:
    print("Berat badan anda berlebih(kecenderungan obesitas)")
else:
    print("Obesitas, hidup lebih sehat yuk")
print()

#4.Menentukan nilai maksimal dan minimal
print("--Menentukan nilai maksimal dan minimal--")
def maximum(nilai1):
    max=0
    for x in nilai1:
        if x > max:
            max=x
    return max
def minimum(nilai2):
    min=999
    for y in nilai2:
        if y < min:
            min=y
    return min

banyaknilai=[]
nilai=int(input("Banyaknya nilai: "))
for z in range(nilai):
    angka=int(input("Masukkan nilai: "))
    banyaknilai.append(angka)
print("Nilai maksimal: ",maximum(banyaknilai))
print("Nilai minimal: ",minimum(banyaknilai))
print()

#5.Menentukan validasi username dan password
print("--Menentukan validasi username dan password--")
username="pemdesk"
password="online"
for x in range(3):
    uname=input("Masukkan username: ")
    pwd=input("Masukkan password: ")
    y=3
    if (uname==username) and (pwd==password):
        print("Anda berhasil masuk")
        break
    else:
        print("Maaf, username/password anda salah. Coba lagi, sisa",y-x)
        continue
print("\n Coba lagi lain kali")
