from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES requires an 8-byte key
key = input("Enter 8-character key: ").encode()

if len(key) != 8:
    print("Key must be exactly 8 characters long.")
    exit()

plaintext = input("Enter the plain text: ")

# Create DES cipher
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt
encrypted = cipher.encrypt(pad(plaintext.encode(), DES.block_size))

print("\nEncrypted Text (Hex):", encrypted.hex())

# Decrypt
decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)

print("Decrypted Text:", decrypted.decode())python