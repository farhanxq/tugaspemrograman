import random

print("Selamat Datang Di Program Ramalan Cupu")
print("+++++++++++++++++++++++++++++++++++++++")

print("Data Anda:")
print("♥♥♥♥♥♥♥♥♥♥♥♥")
nama_user = input("Masukkan Nama Anda: ")
umur_user = int(input("Masukkan Umur Anda: "))

print("\nData Pasangan Anda:")
print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
nama_pasangan = input("Masukkan Nama Pasangan Anda: ")
umur_pasangan = int(input("Masukkan Umur Pasangan Anda: "))

print("\n" + nama_user + " [" + str(umur_user) + "] Tahun")
print("         ♥♥♥\t\t♥♥♥")
print("\t    ♥♥♥♥♥♥♥__♥♥♥♥♥♥♥")
print("\t    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("\t     ♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
print("\t      ♥♥♥♥♥♥♥♥♥♥♥♥")
print("\t       ♥♥♥♥♥♥♥♥♥♥")
print("\t         ♥♥♥♥♥♥♥")
print("\t           ♥♥♥")
print("\t            ♥")


print("\n" + nama_pasangan + " [" + str(umur_pasangan) + "] Tahun")

input("\nTekan ENTER untuk melihat hasil ramalan")

kecocokan = random.randint(50, 100) / 1.1
print("\nKecocokan anda dengan pasangan anda adalah: {:.2f}%".format(kecocokan))

print("\nTerima Kasih karena anda telah menggunakan jasa Ramalan kami.. ^v^")
