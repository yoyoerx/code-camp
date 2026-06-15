# Day 12 — Loop Challenges & Visual Fun
# ===================================================


# -------- GUIDED PRACTICE (type these, then Run) --------

# FizzBuzz up to 20
for n in range(1, 21):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# A growing triangle using string-multiplying
for i in range(1, 6):
    print("*" * i)


# -------- BUILD BLOCK: ASCII Art Generator --------

print()
print("=== ASCII Art Generator ===")

# TODO 1: Ask for a symbol (like * or #) and a size number (use int() on the size).
pass

# TODO 2: Draw a triangle that grows from 1 symbol up to 'size' symbols.
pass

# TODO 3 (bonus): Draw a full square that is 'size' wide and 'size' tall.
pass
