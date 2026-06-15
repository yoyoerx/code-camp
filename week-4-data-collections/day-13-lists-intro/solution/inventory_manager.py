# Day 13 — SOLUTION: RPG Inventory Manager

print("=== Adventurer's Backpack ===")

inventory = ["torch", "compass", "gold coin", "map", "rope"]

print("You have", len(inventory), "items in slots 0 to", len(inventory) - 1, ".")
print("Your backpack:", inventory)

slot = int(input("Which slot do you want to inspect? "))

print()
print("In slot", slot, "you find a shiny", inventory[slot] + "!")
print("It might come in handy on your quest.")
