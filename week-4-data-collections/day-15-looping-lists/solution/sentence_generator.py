# Day 15 — SOLUTION: Random Sentence Generator

import random

print("=== Wacky Sentence Machine ===")

adjectives = ["sparkly", "gigantic", "bubbly", "grumpy", "invisible"]
nouns = ["potato", "unicorn", "wizard", "robot", "noodle"]
verbs = ["dances", "floats", "giggles", "explodes", "sneezes"]

for i in range(5):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    print("The", adj, noun, verb, "happily across the room!")
