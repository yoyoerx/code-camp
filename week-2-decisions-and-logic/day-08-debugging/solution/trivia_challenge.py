# Day 8 — SOLUTION
# Part 1: the three guided-practice bugs, fixed.

secret_number = 7
if secret_number == 7:                 # FIX 1: added the missing colon ":"
    print("Lucky seven!")

player_name = "Alex"
print("Welcome, " + player_name)       # FIX 2: corrected spelling playr -> player

if secret_number > 0:
    print("Positive!")                 # FIX 3: indented this line under the if


# Part 2: Ultimate Trivia Challenge

print()
print("=== Ultimate Trivia Challenge ===")

score = 0

a1 = input("Q1: What is the capital of France? ").lower()
if a1 == "paris":
    print("Correct!")
    score = score + 1
else:
    print("The answer was Paris.")

a2 = input("Q2: What planet do we live on? ").lower()
if a2 == "earth":
    print("Correct!")
    score = score + 1
else:
    print("The answer was Earth.")

a3 = input("Q3: What language are we learning? ").lower()
if a3 == "python":
    print("Correct!")
    score = score + 1
else:
    print("The answer was Python.")

print()
print("Final score:", score, "out of 3")
