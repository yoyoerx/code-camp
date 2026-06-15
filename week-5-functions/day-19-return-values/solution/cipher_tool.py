# Day 19 — SOLUTION: Secret Cipher Tool

print("=== Secret Cipher Tool ===")

def scramble_word(word):
    s = word.replace("a", "@").replace("e", "3").replace("o", "0").replace("i", "1")
    return s

def unscramble_word(secret):
    s = secret.replace("@", "a").replace("3", "e").replace("0", "o").replace("1", "i")
    return s

message = input("Enter a secret message: ")

encoded = scramble_word(message)
print("Encoded message:", encoded)

decoded = unscramble_word(encoded)
print("Decoded again:  ", decoded)
