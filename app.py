from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Fungsi Bubble Sort (Iteratif)
def bubble_sort(mahasiswa):
    n = len(mahasiswa)
    for i in range(n):
        for j in range(0, n-i-1):
            if mahasiswa[j]['nilai'] < mahasiswa[j+1]['nilai']:  # Urutkan dari yang tertinggi
                mahasiswa[j], mahasiswa[j+1] = mahasiswa[j+1], mahasiswa[j]
    return mahasiswa

# Fungsi Merge Sort (Rekursif)
def merge_sort(mahasiswa):
    if len(mahasiswa) > 1:
        mid = len(mahasiswa) // 2
        left_half = mahasiswa[:mid]
        right_half = mahasiswa[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['nilai'] > right_half[j]['nilai']:
                mahasiswa[k] = left_half[i]
                i += 1
            else:
                mahasiswa[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            mahasiswa[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            mahasiswa[k] = right_half[j]
            j += 1
            k += 1

    return mahasiswa

# Fungsi untuk menghitung efisiensi waktu eksekusi
def hitung_efisiensi(algoritma, mahasiswa):
    start_time = time.time()
    algoritma(mahasiswa)
    end_time = time.time()
    return end_time - start_time

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ambil data yang dikirimkan dari form
        mahasiswa_data = request.form["mahasiswa_data"].splitlines()

        # Parse data mahasiswa: setiap baris adalah "Nama, Nilai, Passing Grade"
        mahasiswa = []
        for data in mahasiswa_data:
            parts = data.split(",")
            if len(parts) == 3:
                nama, nilai, passing_grade = parts
                mahasiswa.append({
                    'nama': nama.strip(),
                    'nilai': float(nilai.strip()),  # Menggunakan float() untuk nilai desimal
                    'passing_grade': int(passing_grade.strip())  # Tetap menggunakan int() untuk passing grade
                })

        # Memfilter mahasiswa yang memenuhi passing grade
        mahasiswa_valid = [m for m in mahasiswa if m['nilai'] >= m['passing_grade']]

        # Menghitung waktu eksekusi Bubble Sort
        bubble_sort_mahasiswa = mahasiswa_valid.copy()
        bubble_sort_time = hitung_efisiensi(bubble_sort, bubble_sort_mahasiswa)

        # Menghitung waktu eksekusi Merge Sort
        merge_sort_mahasiswa = mahasiswa_valid.copy()
        merge_sort_time = hitung_efisiensi(merge_sort, merge_sort_mahasiswa)

        return render_template(
            "index.html",
            mahasiswa=mahasiswa_valid,
            bubble_sort_time=bubble_sort_time,
            merge_sort_time=merge_sort_time
        )

    return render_template("index.html", mahasiswa=[], bubble_sort_time=0, merge_sort_time=0)

if __name__ == "__main__":
    app.run(debug=True)
