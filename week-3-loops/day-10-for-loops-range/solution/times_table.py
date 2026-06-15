# Day 10 — SOLUTION: Multiplication Table Generator

print("=== Times Table Machine ===")

number = int(input("Pick a number to see its table: "))

print()
print("--- The", number, "Times Table ---")
for i in range(1, 13):
    print(number, "x", i, "=", number * i)
