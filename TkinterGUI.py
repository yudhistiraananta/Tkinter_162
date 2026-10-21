import tkinter as tk
from tkinter import ttk

MAPEL = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Geografi", "Sejarah", "Sosiologi",
]

def hasil_prediksi():
    # Apapun input yang diberikan, hasilnya selalu Teknologi Informasi
    label_hasil.config(text="Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)

main = ttk.Frame(root, padding=20)
main.grid(row=0, column=0)

ttk.Label(
    main, text="Aplikasi Prediksi Prodi Pilihan",
    font=("Segoe UI", 16, "bold"), anchor="center",
).grid(row=0, column=0, columnspan=4, pady=(0, 15))

entries = []
for i, nama in enumerate(MAPEL):
    baris = i % 5 + 1
    kolom = (i // 5) * 2
    ttk.Label(main, text=nama + ":").grid(
        row=baris, column=kolom, sticky="e", padx=(10, 5), pady=5)
    entry = ttk.Entry(main, width=10, justify="center")
    entry.grid(row=baris, column=kolom + 1, sticky="w", padx=(0, 15), pady=5)
    entries.append(entry)

ttk.Button(main, text="Hasil Prediksi", command=hasil_prediksi).grid(
    row=6, column=0, columnspan=4, pady=(20, 10), ipadx=15, ipady=4)

label_hasil = ttk.Label(
     main, text="-", font=("Segoe UI", 14, "bold"),
    foreground="#1a5fb4", anchor="center",
)
label_hasil.grid(row=7, column=0, columnspan=4, pady=(5, 0))

root.update_idletasks()
w, h = root.winfo_width(), root.winfo_height()
x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"+{x}+{y}")