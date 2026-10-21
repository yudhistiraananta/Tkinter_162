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
