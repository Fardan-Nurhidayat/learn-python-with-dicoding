# for i in range(1 , 20, +2):
#     print("Perulangan ke-", i)

# i : int = 1
# while i < 10: 
#     print("Perulangan ke-", i)
#     i += 1

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 2:
            break  # Menghentikan perulangan dalam jika j = 1
"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""