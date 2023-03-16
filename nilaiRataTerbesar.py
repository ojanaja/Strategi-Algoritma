import time

print ("\nProgram Mencari Nilai Rata-Rata dan Terbesar")
print ("\n============================================")
n = int(input("\nBanyak Data: "))

print()
data = []
jumlah = 0
waktuMulai = time.time()

for i in range(n):
    temp = int(input("Masukkan data ke-%d: "% (i+1)))
    data.append(temp)
    nilaiTerbesar = data[0]
    nilaiTerkecil = data[0]
    if (data[i] > nilaiTerbesar):
        nilaiTerbesar=data[i]
    elif (data[i] < nilaiTerbesar):
        nilaiTerkecil = data[i]
    jumlah += data[i]
    rata = jumlah / n
waktuAkhir = time.time()

print("\n============================================")
print("\nNilai Terbesar : ", nilaiTerbesar)
print("Nilai Terkecil : ", nilaiTerkecil)
print("Nilai Rata-rata  : " ,rata)

waktuMiliSekon = (waktuAkhir-waktuMulai)*1000
print("Waktu Eksekusi :",waktuMiliSekon, "milisekon")

