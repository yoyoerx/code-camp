# Day 4 — SOLUTION: Dog-to-Human Age Converter

print("=== Dog Age Calculator ===")

owner = input("What is your name? ")
dog = input("What is your dog's name? ")
dog_age = int(input("How old is " + dog + " in years? "))

human_years = dog_age * 7

print()
print("Hey " + owner + "!")
print(dog, "is", dog_age, "human years old...")
print("...but that's about", human_years, "in dog years! 🐶")
