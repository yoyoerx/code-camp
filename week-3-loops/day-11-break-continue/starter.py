# Day 11 — break & continue
# ===================================================


# -------- GUIDED PRACTICE (type these, then Run) --------

# break: leave the loop entirely
while True:
    command = input("Type 'exit' to quit: ")
    if command == "exit":
        print("Goodbye!")
        break

# continue: skip just this one pass (predict which number is skipped!)
for number in range(1, 11):
    if number == 5:
        continue
    print(number)


# -------- BUILD BLOCK: Master Password Vault --------
# Give the user only 3 attempts to enter the master key.

print()
print("=== TOP SECRET VAULT ===")

# TODO 1: Store the correct master key in a variable.
pass

# TODO 2: Allow up to 3 attempts (loop with range(3)).
#         Inside: ask for a guess.
#         If correct -> print "Access granted" and break.
#         If wrong   -> tell them.
pass

# TODO 3: After the loop, if they never got in, print "SYSTEM LOCKED DOWN!"
#         (Hint: track success with a True/False variable.)
pass
