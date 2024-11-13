import tkinter as tk
from tkinter import messagebox

# Fungsi enkripsi Caesar Cipher
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

# Fungsi dekripsi Caesar Cipher
def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Fungsi untuk tombol enkripsi
def handle_enkripsi():
    try:
        plain_text = entry_text.get()
        shift = int(entry_shift.get())
        cipher_text = enkripsi(plain_text, shift)
        result_label.config(text=f"Teks terenkripsi: {cipher_text}", fg="green")
    except ValueError:
        messagebox.showerror("Kesalahan", "Nilai shift harus berupa angka.")

# Fungsi untuk tombol dekripsi
def handle_deskripsi():
    try:
        cipher_text = entry_text.get()
        shift = int(entry_shift.get())
        plain_text = deskripsi(cipher_text, shift)
        result_label.config(text=f"Teks terdekripsi: {plain_text}", fg="blue")
    except ValueError:
        messagebox.showerror("Kesalahan", "Nilai shift harus berupa angka.")

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Caesar Cipher")
window.geometry("500x400")
window.configure(bg="#fce4ec")  # Background warna pink soft

# Frame judul
title_frame = tk.Frame(window, bg="#f8bbd0", pady=10)  # Warna pink yang lebih gelap untuk judul
title_frame.pack(fill="x")

title_label = tk.Label(title_frame, text="Aplikasi Kriptografi Caesar Cipher", font=("Arial", 16, "bold"), bg="#f8bbd0", fg="white")
title_label.pack()

# Frame untuk input
input_frame = tk.Frame(window, bg="#fce4ec", padx=20, pady=20)  # Background frame input pink soft
input_frame.pack(pady=20)

text_label = tk.Label(input_frame, text="Masukkan teks:", font=("Arial", 12), bg="#fce4ec")
text_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_text = tk.Entry(input_frame, width=40, font=("Arial", 12))
entry_text.grid(row=0, column=1, padx=5, pady=5)

shift_label = tk.Label(input_frame, text="Masukkan nilai pergeseran (1-25):", font=("Arial", 12), bg="#fce4ec")
shift_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_shift = tk.Entry(input_frame, width=5, font=("Arial", 12))
entry_shift.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Frame untuk tombol
button_frame = tk.Frame(window, bg="#fce4ec")
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Enkripsi", font=("Arial", 12, "bold"), bg="#f48fb1", fg="white", command=handle_enkripsi)
encrypt_button.grid(row=0, column=0, padx=10, pady=5)

decrypt_button = tk.Button(button_frame, text="Deskripsi", font=("Arial", 12, "bold"), bg="#f48fb1", fg="white", command=handle_deskripsi)
decrypt_button.grid(row=0, column=1, padx=10, pady=5)

# Label untuk menampilkan hasil
result_label = tk.Label(window, text="", font=("Arial", 12), bg="white", wraplength=400)
result_label.pack(pady=20)

# Menjalankan jendela utama
window.mainloop()
