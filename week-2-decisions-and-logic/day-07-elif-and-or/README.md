# Day 7 — Complex Decisions (`elif`, `and`, `or`)

> Week 2 · Day 7 of 24 · *Decisions & Logic*

## 🎯 Today's Goal
Handle **more than two** choices with `elif`, and combine conditions with `and` / `or`.

## 🧩 Warm-Up (with your mentor)
Decision game: "If it's raining AND cold, wear a coat. If it's raining OR snowing, take an umbrella." Notice how **AND** needs *both* true, but **OR** only needs *one*. You'll use both today.

## 🧠 Concept Quest
**`elif`** ("else if") lets you check several conditions in order. Python tries them top to bottom and runs the **first** one that's true:

```python
temp = int(input("Temperature in degrees? "))
if temp > 85:
    print("It's scorching hot! 🥵")
elif temp > 60:
    print("Perfect park weather! 🌳")
else:
    print("Brrr, wear a jacket! 🧥")
```

**Logical operators** combine conditions:
- **`and`** → *both* sides must be true: `age > 12 and age < 20` (a teenager)
- **`or`** → *at least one* side must be true: `day == "Sat" or day == "Sun"` (weekend)

```python
if temp > 60 and temp <= 85:
    print("Just right!")
```

> 🔑 Order matters with `elif`! Python stops at the **first** true branch and skips the rest. Put your most specific conditions first.

**📺 Watch/read:** [W3Schools: If...Elif...Else](https://www.w3schools.com/python/python_conditions.asp) · [Programiz: Logical operators](https://www.programiz.com/python-programming/operators#logical).

## ⌨️ Guided Practice — type along
Type the temperature example. Run it three times with hot, mild, and cold numbers to hit all three branches.

## 🛠️ Build Block — Choose-Your-Own-Adventure 🗺️
Build a branching text game with at least **3 different endings**.

- [ ] Set the scene (e.g., "You enter a dark cave...")
- [ ] Ask a first choice (e.g., go `left` or `right`)
- [ ] Based on that, ask a **second** choice
- [ ] Use nested `if`/`elif`/`else` to reach **3+ distinct endings** (treasure, trap, friendly dragon…)

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I ask a second question based on the first answer?</summary>

Put the second `input()` *inside* the first `if`, indented further:
```python
if choice == "left":
    choice2 = input("A door or a tunnel? ")
    if choice2 == "door":
        print("You find treasure!")
    else:
        print("You fall in a pit!")
```
</details>

<details><summary>Hint 2 — My deep indentation is confusing</summary>

Each time you go "inside" an `if`, add 4 more spaces. VS Code does this for you. If it gets messy, draw your story as a tree on paper first, then code each branch.
</details>

<details><summary>Hint 3 — Show me a 3-ending skeleton</summary>

```python
print("You reach a fork in the cave.")
path = input("Go left or right? ")
if path == "left":
    door = input("Open the gold door or the stone door? ")
    if door == "gold":
        print("Treasure! You win! 🏆")
    else:
        print("A trap! Game over. 💀")
else:
    print("A friendly dragon offers you tea. ☕ The end.")
```
Full version: `solution/adventure_game.py`.
</details>

## ⭐ Show & Tell
Walk your mentor through the branches. Let them play and try to find all 3 endings.

## 🧑‍🏫 Mentor note
Nested `if`s are a real step up. If the indentation gets tangled, the paper-tree approach (draw the story branches first) untangles it fast. Save this game — they'll refactor it on Day 20!
