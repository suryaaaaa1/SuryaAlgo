def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Mengembalikan index dari elemen yang ditemukan
        elif arr[mid] < target:
            low = mid + 1  # Pencarian di sisi kanan
        else:
            high = mid - 1  # Pencarian di sisi kiri
    return -1  # Jika elemen tidak ditemukan

# Contoh penggunaan
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(arr, target)

print("Nama: Surya Handy")
print("Kelas : 03TPLP026")
print("--------------------------")
if result != -1:
    print(f"Elemen {target} ditemukan pada index {result}")
else:
    print(f"Elemen {target} tidak ditemukan")
