def shift_char(c, shift):
    if c.islower():
        return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
    elif c.isupper():
        return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
    return c

def encrypt(text, n, m):
    encrypted = ''
    for c in text:
        if c.islower():
            if 'a' <= c <= 'm':
                encrypted += shift_char(c, n * m)
            else:
                encrypted += shift_char(c, -(n + m))
        elif c.isupper():
            if 'A' <= c <= 'M':
                encrypted += shift_char(c, -n)
            else:
                encrypted += shift_char(c, m**2)
        else:
            encrypted += c
    return encrypted

def decrypt(text, n, m):
    decrypted = ''
    for c in text:
        if c.islower():
            if 'a' <= c <= 'm':
                decrypted += shift_char(c, -(n * m))
            else:
                decrypted += shift_char(c, n + m)
        elif c.isupper():
            if 'A' <= c <= 'M':
                decrypted += shift_char(c, n)
            else:
                decrypted += shift_char(c, -(m**2))
        else:
            decrypted += c
    return decrypted

def check_correctness(original, decrypted):
    return original == decrypted

def main():
    # Taking user input for n and m
    try:
        n = int(input("Enter value for n: "))
        m = int(input("Enter value for m: "))
    except ValueError:
        print("Please enter valid integers for n and m.")
        return

    # Read original text
    try:
        with open('raw_text.txt', 'r') as file:
            raw_text = file.read()
    except FileNotFoundError:
        print("File 'raw_text.txt' not found.")
        return

    # Encrypt and write to file
    encrypted_text = encrypt(raw_text, n, m)
    with open('encrypted_text.txt', 'w') as file:
        file.write(encrypted_text)
    print("Encrypted text written to 'encrypted_text.txt'.")
    print("\nEncrypted Text:\n", encrypted_text)

    # Decrypt and check
    decrypted_text = decrypt(encrypted_text, n, m)
    is_correct = check_correctness(raw_text, decrypted_text)

    print("Decryption successful:", is_correct)

if __name__ == "__main__":
    main()
