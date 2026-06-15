# Day 20 — SOLUTION (example): Day 11 Password Vault, REFACTORED into functions.
# Compare this with your original Day 11 password_vault.py.
# Same behavior -- but now it reads like a clear list of steps.

def show_intro():
    print("=== TOP SECRET VAULT ===")

def check_password(master_key, max_tries):
    """Returns True if the user unlocks the vault, False if they run out of tries."""
    for attempt in range(max_tries):
        guess = input("Enter the master key: ")
        if guess == master_key:
            return True                       # success exits the function early
        tries_left = max_tries - 1 - attempt
        print("Wrong key.", tries_left, "tries left.")
    return False                              # ran out of tries

def report_result(unlocked):
    if unlocked:
        print("✅ ACCESS GRANTED. Welcome, Commander.")
    else:
        print("🔒 SYSTEM LOCKED DOWN!")

# ---- main: short and easy to read ----
show_intro()
unlocked = check_password("dragon42", 3)
report_result(unlocked)
