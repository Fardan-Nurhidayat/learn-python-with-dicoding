text : str = "Fardan"
text_number : str = text.zfill(10)  # Menambahkan leading zeros hingga panjang 10
print(text_number)  # Output: 00000Fardan

text_add_from_right : str = text.rjust(10, '*')  # Menambahkan karakter '*' di sebelah kanan hingga panjang 10
print(text_add_from_right)  # Output: Fardan*****

text_add_from_left : str = text.ljust(10, '*')  # Menambahkan karakter '*' di sebelah kiri hingga panjang 10
print(text_add_from_left)  # Output: *****Fardan

text_center : str = text.center(10, '*')  # Menambahkan karakter '*' di kedua sisi hingga panjang 10
print(text_center)  # Output: **Fardan***

friday = 'Jum\'at'
print(friday)  # Output: Jum'at

gretting : str = "Hello \n World"
print(gretting)

kendaraan = ["Mobil", "Motor", "Sepeda" , "Angkutan" , "bis"]
kendaraan.sort(key=str.lower)
print(kendaraan)