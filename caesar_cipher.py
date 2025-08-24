def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Example tests
print(caesar_cipher("abc", 3))          # Output: "def"
print(caesar_cipher("xyz", 2))          # Output: "zab"
print(caesar_cipher("Hello, World!", 5)) # Output: "Mjqqt, Btwqi!"