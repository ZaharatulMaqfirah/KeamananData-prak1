from tkinter import Tk, Label, Button, filedialog, Text, messagebox, Frame, Scrollbar, VERTICAL
from PIL import Image
import numpy as np

# Fungsi untuk menyisipkan teks ke dalam gambar
def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    message_bin = ''.join(format(ord(char), '08b') for char in message)
    message_bin += '1111111111111110'  # Tanda akhir pesan

    idx = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB Channels
                if idx < len(message_bin):
                    img_array[i][j][k] = (img_array[i][j][k] & ~1) | int(message_bin[idx])
                    idx += 1

    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    messagebox.showinfo("Success", "Pesan berhasil disisipkan!")

# Fungsi untuk membaca teks tersembunyi dari gambar
def decode_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    bits = ''
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):
                bits += str(img_array[i][j][k] & 1)

    message = ''
    for i in range(0, len(bits), 8):
        char = chr(int(bits[i:i+8], 2))
        if char == '\x7e':  # Tanda akhir pesan
            break
        message += char

    messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {message}")

# Fungsi-fungsi antarmuka pengguna
def open_file(mode):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.bmp")])
    if mode == "encode":
        message = text_box.get("1.0", "end-1c")
        if not message:
            messagebox.showerror("Error", "Pesan tidak boleh kosong!")
        else:
            output_path = filedialog.asksaveasfilename(defaultextension=".png")
            if output_path:
                encode_image(file_path, message, output_path)
    elif mode == "decode":
        decode_image(file_path)

# GUI dengan Tkinter
root = Tk()
root.title("Aplikasi Steganografi")
root.configure(bg="#FFDEE9")  # Warna pink soft

# Header
header = Label(root, text="Aplikasi Steganografi", font=("Helvetica", 18, "bold"), bg="#FFDEE9", fg="#6A0572")
header.pack(pady=10)

# Frame utama
frame = Frame(root, bg="#FFDEE9")
frame.pack(pady=10)

# Area Input Pesan
Label(frame, text="Masukkan Pesan:", font=("Helvetica", 12), bg="#FFDEE9", fg="#6A0572").grid(row=0, column=0, sticky="w")

text_box = Text(frame, height=5, width=50, font=("Helvetica", 11), wrap="word", bg="#FFF5F7", fg="#6A0572", relief="flat", bd=2)
text_box.grid(row=1, column=0, columnspan=2, pady=5)

# Tombol Encode
btn_encode = Button(frame, text="Sisipkan Pesan (Encode)", command=lambda: open_file("encode"),
                    font=("Helvetica", 10), bg="#F8BBD0", fg="#6A0572", relief="flat", padx=10, pady=5)
btn_encode.grid(row=2, column=0, pady=10)

# Tombol Decode
btn_decode = Button(frame, text="Baca Pesan (Decode)", command=lambda: open_file("decode"),
                    font=("Helvetica", 10), bg="#F8BBD0", fg="#6A0572", relief="flat", padx=10, pady=5)
btn_decode.grid(row=2, column=1, pady=10, padx=10)

# Footer
footer = Label(root, text="Dibuat dengan ❤️ menggunakan Python", font=("Helvetica", 10), bg="#FFDEE9", fg="#6A0572")
footer.pack(pady=10)

root.mainloop()
