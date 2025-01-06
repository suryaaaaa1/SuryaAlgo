def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan index dari elemen yang ditemukan
    return -1  # Jika elemen tidak ditemukan

# Contoh penggunaan
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = linear_search(arr, target)

print("Nama: Surya Handy")
print("Kelas : 03TPLP026")
print("--------------------------")
if result != -1:
    print(f"Elemen {target} ditemukan pada index {result}")
else:
    print(f"Elemen {target} tidak ditemukan")
