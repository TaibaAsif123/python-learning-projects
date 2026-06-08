
"""
This program creates a random substitution cipher to encrypt and decrypt messages 
by mapping characters to shuffled counterparts using a generated key
"""

import random
import string
chars=" "+string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#print(f"CHARS={chars}")
#print(f"KEY={key}")

#Encryption:
plain_text=input("Enter a message to encrypt:")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"Orginal message:{plain_text}")
print(f"Encrypted message:{cipher_text}")

#Decryption:
cipher_text=input("Enter a message to decrypt:")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f"Orginal message:{cipher_text}")
print(f"Encrypted message:{plain_text}")


