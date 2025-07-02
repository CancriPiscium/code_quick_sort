def quick_sort_interactive(arr, depth=0):
    indent = "  " * depth  # buat indentasi agar rapi di console

    # Tampilkan array saat ini
    print(f"{indent}Array saat ini: {arr}")
    input(f"{indent}Tekan Enter untuk lanjut...")

    # Basis: jika panjang array <= 1, return langsung
    if len(arr) <= 1:
        print(f"{indent}=> Tidak perlu diurutkan (panjang <= 1)")
        input(f"{indent}Tekan Enter untuk kembali...\n")
        return arr

    pivot = arr[-1]
    print(f"{indent}Pivot dipilih: {pivot}")

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    print(f"{indent}Kiri (≤ {pivot}): {left}")
    print(f"{indent}Kanan (> {pivot}): {right}")
    input(f"{indent}Tekan Enter untuk rekursi ke kiri...\n")

    sorted_left = quick_sort_interactive(left, depth + 1)

    input(f"{indent}Tekan Enter untuk rekursi ke kanan...\n")
    sorted_right = quick_sort_interactive(right, depth + 1)

    result = sorted_left + [pivot] + sorted_right
    print(f"{indent}Gabung: {sorted_left} + [{pivot}] + {sorted_right} => {result}")
    input(f"{indent}Tekan Enter untuk kembali...\n")
    return result

# Data awal
data = [7, 2, 1, 6, 8, 5, 3, 4]

print("=== Quick Sort Interaktif ===")
print("Data awal:", data)
print("\nMulai pengurutan...\n")

# Jalankan quick sort
sorted_data = quick_sort_interactive(data)

print("\n=== HASIL AKHIR ===")
print("Data terurut:", sorted_data)

