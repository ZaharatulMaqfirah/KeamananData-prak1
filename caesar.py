def enkripsi(plain_text, shift):
    cipher_text=""
    for char in plain_text:
        #Huruf besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65 ) % 25 + 65)
        #Huruf kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97 ) % 26 + 97)
        else:
        # karakter selain huruf tetap
            cipher_text += char
    return cipher_text


def deskripsi(cipher_text,shift):
    plain_text = ""
    for char in cipher_text:
        #huruf besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) %26 +65) 
        #huruf kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) %26 +97) 
        else:
            #karakter selain huruf tetap
            plain_text += char
    return plain_text
       

# interface pengguna

def main():
    print("Selamat datang di program kriptrografi caesar")
    plain_text = input("masukkan text asli (plaintext):")
    shift = int(input("masukkan nilai pergeseran (1-25):"))


    # panggil fungsi enkripsi 
    cipher_text = enkripsi(plain_text, shift)
    print("text terenkripsi:", cipher_text )

     # panggil fungsi deskripsi
    deskripsi_text = deskripsi(cipher_text, shift)
    print("text terdeskripsi:", deskripsi_text)

if __name__=="__main__":
    main()