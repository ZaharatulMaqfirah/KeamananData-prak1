from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, END, filedialog, ttk
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

class DESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DES Encryption Application")
        self.root.geometry("600x400")
        
        # Menambahkan gaya tema
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#E8F5E9", foreground="#2E7D32")
        style.configure("TButton", font=("Helvetica", 10, "bold"), background="#A5D6A7", foreground="#1B5E20")
        style.configure("TEntry", font=("Helvetica", 12))

        self.root.configure(bg="#E8F5E9")  # Warna latar belakang hijau lembut

        # Key input
        ttk.Label(root, text="Key (8 characters):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.key_entry = ttk.Entry(root, width=30)
        self.key_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Plaintext input
        ttk.Label(root, text="Plaintext:").grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        self.plaintext = Text(root, height=5, width=50, font=("Helvetica", 12), bg="#C8E6C9", fg="#1B5E20")
        self.plaintext.grid(row=1, column=1, padx=10, pady=10)

        # Ciphertext output
        ttk.Label(root, text="Ciphertext:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.ciphertext = Text(root, height=5, width=50, font=("Helvetica", 12), bg="#C8E6C9", fg="#1B5E20")
        self.ciphertext.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=4, column=0, columnspan=2, pady=10)

    def pad_text(self, text):
        while len(text) % 8 != 0:
            text += ' '
        return text

    def encrypt(self):
        key = self.key_entry.get()
        if len(key) != 8:
            self.ciphertext.delete(1.0, END)
            self.ciphertext.insert(END, "Key must be 8 characters long!")
            return

        cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC)
        iv = cipher.iv
        plaintext = self.plaintext.get(1.0, END).strip()
        if not plaintext:
            self.ciphertext.delete(1.0, END)
            self.ciphertext.insert(END, "Plaintext is empty!")
            return

        padded_text = self.pad_text(plaintext)
        encrypted_text = cipher.encrypt(padded_text.encode('utf-8'))
        encoded_text = base64.b64encode(iv + encrypted_text).decode('utf-8')

        self.ciphertext.delete(1.0, END)
        self.ciphertext.insert(END, encoded_text)

    def decrypt(self):
        key = self.key_entry.get()
        if len(key) != 8:
            self.plaintext.delete(1.0, END)
            self.plaintext.insert(END, "Key must be 8 characters long!")
            return

        encoded_text = self.ciphertext.get(1.0, END).strip()
        if not encoded_text:
            self.plaintext.delete(1.0, END)
            self.plaintext.insert(END, "Ciphertext is empty!")
            return

        try:
            decoded_data = base64.b64decode(encoded_text)
            iv = decoded_data[:8]
            encrypted_text = decoded_data[8:]
            cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)
            decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8').strip()

            self.plaintext.delete(1.0, END)
            self.plaintext.insert(END, decrypted_text)
        except Exception as e:
            self.plaintext.delete(1.0, END)
            self.plaintext.insert(END, f"Error: {str(e)}")

    def clear_fields(self):
        self.key_entry.delete(0, END)
        self.plaintext.delete(1.0, END)
        self.ciphertext.delete(1.0, END)

if __name__ == "__main__":
    root = Tk()
    app = DESApp(root)
    root.mainloop()
