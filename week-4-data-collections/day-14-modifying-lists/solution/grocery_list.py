# Day 14 — SOLUTION: Interactive Grocery List

print("=== Grocery List Manager ===")

groceries = ["milk", "eggs"]

while True:
    print()
    print("1) View list   2) Add item   3) Remove item   4) Quit")
    choice = input("What would you like to do? ")

    if choice == "1":
        print("Your list:", groceries)
    elif choice == "2":
        item = input("Add what? ")
        groceries.append(item)
        print(item, "added!")
    elif choice == "3":
        item = input("Remove what? ")
        if item in groceries:                # defensive coding (Day 8!)
            groceries.remove(item)
            print(item, "removed!")
        else:
            print(item, "isn't on the list.")
    elif choice == "4":
        print("Happy shopping! 🛒")
        break
    else:
        print("Please pick 1, 2, 3, or 4.")
