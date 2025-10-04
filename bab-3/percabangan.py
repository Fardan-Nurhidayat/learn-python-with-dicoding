# nilai = int(input("Masukkan nilai anda : "))

# if nilai >= 80:
#     print("Nilai A")
# elif nilai >= 70:      # Tidak perlu < 80 karena sudah dicek di atas
#     print("Nilai B")
# elif nilai >= 60:      # Tidak perlu < 70 karena sudah dicek di atas
#     print("Nilai C")
# elif nilai >= 50:      # Tidak perlu < 60 karena sudah dicek di atas
#     print("Nilai D")
# else:
#     print("Nilai E")

# lulus : bool = True 
# print("Selamat anda lulus") if lulus else print("Silakan coba lagi tahun depan")

lulus : bool = False
kelulusan = ("Perbaiki nilai kamu" , "Selamat anda lulus")[lulus]
print(kelulusan)