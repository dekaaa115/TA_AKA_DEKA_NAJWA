import pandas as pd
import time
import matplotlib.pyplot as plt

# Fungsi Linear Search Iteratif
def linear_search_iterative(arr, key, value):
    result = []
    for item in arr:
        if item[key].lower() == value.lower():
            result.append(item)
    return result

# Fungsi Linear Search Rekursif
def linear_search_recursive(arr, n, key, value, result=None):
    if result is None:
        result = []
    if n == 0:
        return result
    if arr[n - 1][key].lower() == value.lower():
        result.append(arr[n - 1])
    return linear_search_recursive(arr, n - 1, key, value, result)

if __name__ == "__main__":
    # Data buku di perpustakaan
    books = [
        {"id": 101, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction"},
        {"id": 102, "title": "1984", "author": "George Orwell", "category": "Dystopian"},
        {"id": 103, "title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
        {"id": 104, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Fiction"},
        {"id": 105, "title": "Sapiens", "author": "Yuval Noah Harari", "category": "History"},
        {"id": 106, "title": "Educated", "author": "Tara Westover", "category": "Memoir"},
        {"id": 107, "title": "Becoming", "author": "Michelle Obama", "category": "Biography"},
        {"id": 108, "title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction"}
    ]

    # Gandakan data untuk mendapatkan ukuran data lebih besar
    books = books * 100

    # List untuk menyimpan hasil
    all_results = []

    # Loop pencarian sebanyak 5 kali
    for run in range(1, 6):
        print(f"\nRun {run} - Masukkan kriteria pencarian:")
        try:
            # Input kriteria pencarian
            key = input("Masukkan kriteria (title/author/category): ").strip().lower()
            if key not in ["title", "author", "category"]:
                print("Kriteria tidak valid! Pilih title, author, atau category.")
                continue

            value = input(f"Masukkan {key} yang ingin dicari: ").strip()
            n = int(input("Masukkan jumlah buku yang akan dicari (n): "))

            if n > len(books):
                print(f"Nilai n terlalu besar! Maksimal: {len(books)}")
                continue

            # Ambil data sesuai ukuran input (n)
            sample_data = books[:n]

            # Iterative
            start_time_iterative = time.perf_counter()
            iterative_result = linear_search_iterative(sample_data, key, value)
            exec_time_iterative = time.perf_counter() - start_time_iterative

            # Recursive
            start_time_recursive = time.perf_counter()
            recursive_result = linear_search_recursive(sample_data, len(sample_data), key, value)
            exec_time_recursive = time.perf_counter() - start_time_recursive

            # Simpan hasil untuk setiap run
            all_results.append((n, exec_time_recursive, exec_time_iterative))

            # Konversi hasil ke DataFrame
            df = pd.DataFrame(all_results, columns=['n', 'Recursive Time (s)', 'Iterative Time (s)'])

            # Tampilkan hasil pencarian
            print("\nHasil Pencarian (Iterative):", iterative_result)
            print("Hasil Pencarian (Recursive):", recursive_result)

            # Tampilkan hasil di terminal
            print(df.to_string(index=False))

            # Buat grafik
            plt.figure(figsize=(10, 6))

            # Plot Recursive
            plt.plot(df['n'], df['Recursive Time (s)'], label='Recursive', color='red', marker='o', linestyle='-', linewidth=2)

            # Plot Iterative
            plt.plot(df['n'], df['Iterative Time (s)'], label='Iterative', color='blue', marker='o', linestyle='-', linewidth=2)

            # Tambahkan label, judul, dan legenda
            plt.title('Perbandingan Waktu Eksekusi Linear Search')
            plt.xlabel('Ukuran Input (n)')
            plt.ylabel('Waktu Eksekusi (detik)')
            plt.legend()
            plt.grid(True)
            plt.tight_layout()

            # Tampilkan grafik
            plt.show()

        except ValueError:
            print("Masukkan angka yang valid!")

    print("\nProgram selesai!")
