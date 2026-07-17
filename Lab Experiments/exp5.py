# Rail Fence Cipher - Encryption and Decryption

plain_text = input("Enter the plain text: ")

# Encryption
cipher_text = ""

# Even index characters
for i in range(0, len(plain_text), 2):
    cipher_text += plain_text[i]

# Odd index characters
for i in range(1, len(plain_text), 2):
    cipher_text += plain_text[i]

print("\nEncrypted Text:", cipher_text)

# Decryption
length = len(cipher_text)

if length % 2 == 0:
    mid = length // 2
else:
    mid = (length // 2) + 1

first = cipher_text[:mid]
second = cipher_text[mid:]

decrypted_text = ""

i = j = 0

while i < len(first) or j < len(second):
    if i < len(first):
        decrypted_text += first[i]
        i += 1
    if j < len(second):
        decrypted_text += second[j]
        j += 1

print("Decrypted Text:", decrypted_text)