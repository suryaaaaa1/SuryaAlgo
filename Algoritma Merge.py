def merge(arr1, arr2):
    # Array hasil gabungan
    result = []
    
    # Inisialisasi dua pointer untuk masing-masing array
    i, j = 0, 0
    
    # Proses penggabungan
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Jika masih ada elemen sisa di arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    # Jika masih ada elemen sisa di arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result


print("Nama: Surya Handy")
print("Kelas : 03TPLP026")
print("--------------------------")
# Contoh penggunaan
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = merge(arr1, arr2)
print("Array Gabungan:", result)
