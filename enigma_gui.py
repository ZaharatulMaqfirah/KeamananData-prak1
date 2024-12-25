import tkinter as tk
from tkinter import messagebox

# Fungsi Enkripsi/Deskripsi sederhana def simulate Enigma logic
def enigma_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Fungsi saat tombol ditekan
def process_text():
    try:
        input_text = input_textbox.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())

        if mode_var.get() == "encrypt":
            output_text = enigma_cipher(input_text, shift)
        else:
            output_text = enigma_cipher(input_text, -shift)

        output_textbox.delete("1.0", tk.END)
        output_textbox.insert(tk.END, output_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the shift.")

# GUI setup
root = tk.Tk()
root.title("Simple Enigma Cipher")
root.configure(bg="#d0f0c0")  # Background warna hijau aesthetic

# Input Textbox
tk.Label(root, text="Input Text:", bg="#d0f0c0", fg="#004d00", font=("Arial", 12)).pack(anchor="w", pady=5)
input_textbox = tk.Text(root, height=5, width=50, bg="#e8f5e9", fg="#004d00", font=("Arial", 10))
input_textbox.pack(pady=5)

# Shift Entry
tk.Label(root, text="Shift (Number):", bg="#d0f0c0", fg="#004d00", font=("Arial", 12)).pack(anchor="w", pady=5)
shift_entry = tk.Entry(root, bg="#e8f5e9", fg="#004d00", font=("Arial", 10))
shift_entry.pack(pady=5)

# Mode Selection
mode_var = tk.StringVar(value="encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt", bg="#d0f0c0", fg="#004d00", font=("Arial", 12)).pack(anchor="w", pady=2)
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt", bg="#d0f0c0", fg="#004d00", font=("Arial", 12)).pack(anchor="w", pady=2)

# Process Button
tk.Button(root, text="Process", command=process_text, bg="#a5d6a7", fg="#004d00", font=("Arial", 12), relief="raised").pack(pady=10)

# Output Textbox
tk.Label(root, text="Output Text:", bg="#d0f0c0", fg="#004d00", font=("Arial", 12)).pack(anchor="w", pady=5)
output_textbox = tk.Text(root, height=5, width=50, bg="#e8f5e9", fg="#004d00", font=("Arial", 10))
output_textbox.pack(pady=5)

# Run the app
root.mainloop()
