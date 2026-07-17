# Playfair Cipher Encryption

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            matrix.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is omitted
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join([c for c in text if c.isalpha()])

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result


def encrypt(text, matrix):
    cipher = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        # Same column
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        # Rectangle rule
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


# Main Program
key = input("Enter the key: ")
plaintext = input("Enter the plain text: ")

matrix = generate_key_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

prepared = prepare_text(plaintext)
cipher = encrypt(prepared, matrix)

print("\nPrepared Text :", prepared)
print("Cipher Text   :", cipher)