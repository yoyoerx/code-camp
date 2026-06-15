# Day 9 — SOLUTION: Number Guessing Game (with hot/cold hints)

print("=== Guess My Number ===")

secret = 7
guess = int(input("Guess my number (1-10): "))

while guess != secret:
    if guess > secret:
        print("Too high! Try lower.")
    else:
        print("Too low! Try higher.")
    guess = int(input("Guess again: "))

print("🎉 You got it! The number was", secret)
