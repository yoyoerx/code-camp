# Day 6 — SOLUTION: Secret Passcode Door

print("=== The Vault of Wonders ===")

secret = "open-sesame"
guess = input("Speak the secret password: ")

if guess == secret:
    print("=============================")
    print("💰 The vault swings open! 💰")
    print("   You found the treasure!   ")
    print("=============================")
else:
    print("🚨🚨🚨 INTRUDER ALERT! 🚨🚨🚨")
    print("The vault stays locked tight.")
