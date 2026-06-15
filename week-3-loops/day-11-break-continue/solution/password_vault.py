# Day 11 — SOLUTION: Master Password Vault

print("=== TOP SECRET VAULT ===")

master_key = "dragon42"
unlocked = False

for attempt in range(3):
    guess = input("Enter the master key: ")
    if guess == master_key:
        unlocked = True
        print("✅ ACCESS GRANTED. Welcome, Commander.")
        break
    else:
        tries_left = 2 - attempt
        print("❌ Wrong key.", tries_left, "tries left.")

if not unlocked:
    print("🔒 SYSTEM LOCKED DOWN! Too many failed attempts.")
