def encrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    shift_amount = int(input("Enter the shift amount: "))

    encrypted = encrypt(plaintext, shift_amount)
    print("Ciphertext:", encrypted)

    decrypted = decrypt(encrypted, shift_amount)
    print("Decrypted:", decrypted)

