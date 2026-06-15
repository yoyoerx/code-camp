# Day 16 — SOLUTION: Pokedex

print("=== Pocket Pokedex ===")

pokedex = {
    "pikachu": {"type": "Electric", "power": 55},
    "charmander": {"type": "Fire", "power": 52},
    "bulbasaur": {"type": "Grass", "power": 49},
}

print("Available:", "pikachu, charmander, bulbasaur")
search = input("Which one do you want to look up? ").lower()

if search in pokedex:
    creature = pokedex[search]
    print()
    print("=== " + search.title() + " ===")
    print("Type: ", creature["type"])
    print("Power:", creature["power"])
else:
    print("Sorry, '" + search + "' is not in the Pokedex.")
