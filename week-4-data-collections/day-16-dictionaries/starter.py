# Day 16 — Dictionaries
# ===================================================


# -------- GUIDED PRACTICE (type these, then Run) --------

hero_stats = {"name": "Link", "health": 100, "defense": 15}
print("Hero name:", hero_stats["name"])
print("Health:", hero_stats["health"])

hero_stats["health"] = 90      # change a value
hero_stats["level"] = 5        # add a new key
print(hero_stats)


# -------- BUILD BLOCK: Pokedex / Contact Book --------

print()
print("=== Pocket Pokedex ===")

# TODO 1: Create a dictionary with 3 creatures. Each value can itself be a
#         dictionary of stats (type, power). See Hint 1 if stuck.
pass

# TODO 2: Ask the user to type a name to look up (use .lower() to be safe).
pass

# TODO 3: If the name is in your dictionary, print its stats nicely.
#         Otherwise, print a "not found" message.
pass
