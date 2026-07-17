# Caesar Cipher - Encryption and Decryption

plain_text = input("Enter the plain text: ")
key = int(input("Enter the key value: "))

cipher_text = ""

# Encryption
for ch in plain_text:
    if ch.isupper():
        cipher_text += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    elif ch.islower():
        cipher_text += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    else:
        cipher_text += ch

print("\nPlain Text     :", plain_text)
print("Encrypted Text :", cipher_text)

# Decryption
decrypted_text = ""

for ch in cipher_text:
    if ch.isupper():
        decrypted_text += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
    elif ch.islower():
        decrypted_text += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
    else:
        decrypted_text += ch

print("Decrypted Text :", decrypted_text)