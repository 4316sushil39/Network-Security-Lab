def normalize_key(key):
    return "".join(ch.upper() for ch in key if ch.isalpha())


def encrypt(text, key):
    encrypted = ""
    key_letters = normalize_key(key)
    if not key_letters:
        raise ValueError("Key must contain at least one alphabetic character.")

    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key_letters[key_index % len(key_letters)]) - 65
            base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            encrypted += char

    return encrypted


def decrypt(text, key):
    decrypted = ""
    key_letters = normalize_key(key)
    if not key_letters:
        raise ValueError("Key must contain at least one alphabetic character.")

    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key_letters[key_index % len(key_letters)]) - 65
            base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            decrypted += char

    return decrypted


if __name__ == "__main__":
    message = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    secret = encrypt(message, key)
    original = decrypt(secret, key)

    print("Encrypted:", secret)
    print("Decrypted:", original)
