# Hill Cipher (3x3)

# Encryption Key Matrix
encrypt_key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

# Inverse Key Matrix
decrypt_key = [
    [8, 5, 10],
    [21, 8, 21],
    [21, 12, 8]
]

# Read Plain Text
plain_text = input("Enter plain text (3 letters): ").upper()

# Convert letters to numbers (A=0, B=1, ..., Z=25)
plain = [ord(ch) - ord('A') for ch in plain_text]

# Encryption
cipher = []

for i in range(3):
    total = 0
    for j in range(3):
        total += encrypt_key[i][j] * plain[j]
    cipher.append(total % 26)

cipher_text = "".join(chr(num + ord('A')) for num in cipher)
print("Encrypted Cipher Text :", cipher_text)

# Decryption
decrypted = []

for i in range(3):
    total = 0
    for j in range(3):
        total += decrypt_key[i][j] * cipher[j]
    decrypted.append(total % 26)

decrypted_text = "".join(chr(num + ord('A')) for num in decrypted)
print("Decrypted Cipher Text :", decrypted_text)