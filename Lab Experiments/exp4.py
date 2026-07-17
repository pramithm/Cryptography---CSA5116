# Vigenere Cipher - Encryption and Decryption

def generate_key(text, key):
    key = key.upper()
    while len(key) < len(text):
        key += key
    return key[:len(text)]


def encrypt(text, key):
    cipher = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i].upper()) - ord('A') +
                 ord(key[i]) - ord('A')) % 26
            cipher += chr(x + ord('A'))
        else:
            cipher += text[i]

    return cipher


def decrypt(cipher, key):
    text = ""

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            x = (ord(cipher[i]) - ord('A') -
                 (ord(key[i]) - ord('A'))) % 26
            text += chr(x + ord('A'))
        else:
            text += cipher[i]

    return text


# Main Program
plain_text = input("Enter Plain Text: ").upper()
key = input("Enter Key: ").upper()

key = generate_key(plain_text, key)

cipher_text = encrypt(plain_text, key)
decrypted_text = decrypt(cipher_text, key)

print("\nGenerated Key :", key)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)