# Demo konsep immutable numbers di Python

print("=== DEMO IMMUTABLE NUMBERS ===")
print()

# Contoh 1: Numbers adalah immutable
print("1. Contoh dengan integer:")
var = 10
print(f"var = {var}")
print(f"id(var) = {id(var)}")
print(f"Alamat memori object 10: {id(10)}")
print()

# Ketika kita "mengubah" var, sebenarnya kita membuat object baru
var = 11
print(f"Setelah var = 11:")
print(f"var = {var}")
print(f"id(var) = {id(var)}")
print(f"Alamat memori object 11: {id(11)}")
print()

print("PENJELASAN:")
print("- Object 10 masih ada di memori dengan alamat yang sama")
print("- Object 11 adalah object baru dengan alamat berbeda")
print("- Variabel 'var' hanya berganti menunjuk ke object yang berbeda")
print()

# Contoh 2: Membuktikan object 10 masih ada
print("2. Membuktikan object 10 masih ada:")
another_var = 10
print(f"another_var = {another_var}")
print(f"id(another_var) = {id(another_var)}")
print(f"id(10) = {id(10)}")
print("Lihat! Semua menunjuk ke object 10 yang sama")
print()

# Contoh 3: Bandingkan dengan list (mutable)
print("3. Bandingkan dengan list (mutable):")
my_list = [1, 2, 3]
print(f"my_list = {my_list}")
print(f"id(my_list) = {id(my_list)}")

# Mengubah isi list (object yang sama dimodifikasi)
my_list.append(4)
print(f"Setelah append(4):")
print(f"my_list = {my_list}")
print(f"id(my_list) = {id(my_list)}")
print("Alamat memori sama! Object list dimodifikasi, tidak diganti")
print()

# Contoh 4: Apa yang terjadi jika kita coba "modify" number
print("4. Kenapa numbers immutable?")
x = 10
y = x  # y menunjuk ke object yang sama dengan x
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

x = x + 1  # Ini membuat object baru!
print(f"Setelah x = x + 1:")
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print("y masih 10 karena object 10 tidak berubah!")