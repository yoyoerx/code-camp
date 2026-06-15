# Day 12 — SOLUTION: ASCII Art Generator

print("=== ASCII Art Generator ===")

symbol = input("Pick a symbol (like * or #): ")
size = int(input("Pick a size: "))

print()
print("--- Triangle ---")
for i in range(1, size + 1):
    print(symbol * i)

print()
print("--- Square ---")
for i in range(size):
    print(symbol * size)
