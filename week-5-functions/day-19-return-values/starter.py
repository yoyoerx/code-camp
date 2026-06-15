# Day 19 — Return Values
# ===================================================
# print() SHOWS something. return HANDS A VALUE BACK to your code.
# ===================================================


# -------- GUIDED PRACTICE (type these, then Run) --------

def add_tax(price):
    total = price * 1.05
    return total

final_cost = add_tax(100)        # catch the returned value
print("Your total with tax is:", final_cost)


# -------- BUILD BLOCK: Secret Cipher Tool --------

print()
print("=== Secret Cipher Tool ===")

# TODO 1: Write scramble_word(word) that swaps some letters
#         (a->@, e->3, o->0, i->1 ...) and RETURNS the scrambled string.
#         Hint: use word.replace("a", "@")
pass

# TODO 2: Ask the user for a message, scramble it, and print the secret.
pass

# TODO 3 (bonus): Write unscramble_word(secret) that reverses the swaps
#         and returns the original word.
pass
