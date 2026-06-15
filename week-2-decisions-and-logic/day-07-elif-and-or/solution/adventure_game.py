# Day 7 — SOLUTION: Choose-Your-Own-Adventure (4 endings)

print("=== The Cave of Mysteries ===")
print("You stand at the mouth of a dark, dripping cave...")

path = input("Do you go left or right? ").lower()

if path == "left":
    door = input("You see a GOLD door and a STONE door. Which? ").lower()
    if door == "gold":
        print("The gold door opens to a room full of treasure! YOU WIN! 🏆")
    else:
        print("The stone door hides a pit. Down you go... GAME OVER. 💀")
elif path == "right":
    sound = input("You hear a noise. Do you HIDE or SHOUT? ").lower()
    if sound == "shout":
        print("A friendly dragon answers and shares its tea. New friend! 🐉☕")
    else:
        print("You hide so well you fall asleep and wake up outside. The end. 😴")
else:
    print("You stand frozen with indecision until the cave closes. The end. 🪨")
