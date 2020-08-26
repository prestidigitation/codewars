# Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, and it shifts the letters of the message for the value of the key.

# Your task
# Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

# Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, numbers, spaces, and so on should remain the same.

# Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!

# Examples
# A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.
# A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.


# naive solution
def encryptor(key, message):
    upper_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lower_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    encrypted = ''
    for char in message:
        if char in upper_chars:
            encrypted += upper_chars[(upper_chars.index(char) + key) % 26]
        elif char in lower_chars:
            encrypted += lower_chars[(lower_chars.index(char) + key) % 26]
        else:
            encrypted += char
    return encrypted


# refactor using Python string constants
from string import ascii_uppercase as uc, ascii_lowercase as lc

def encryptor_two(key, message):
    encrypted = ''
    for char in message:
        if char in uc:
            encrypted += uc[(uc.index(char) + key) % 26]
        elif char in lc:
            encrypted += lc[(lc.index(char) + key) % 26]
        else:
            encrypted += char
    return encrypted
