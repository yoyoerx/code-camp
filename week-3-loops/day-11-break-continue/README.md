# Day 11 — Loop Controls (`break` & `continue`)

> Week 3 · Day 11 of 24 · *Loops*

## 🎯 Today's Goal
Take control of loops: jump out early with `break`, and skip a single round with `continue`.

## 🧩 Warm-Up (with your mentor)
Imagine running laps. **`break`** = "I'm done, leave the track now." **`continue`** = "skip the rest of *this* lap and start the next one." Act them out — run in place, then "break" (stop) or "continue" (reset).

## 🧠 Concept Quest
- **`break`** immediately *exits* the loop — the emergency eject button.
- **`continue`** *skips the rest of this turn* and jumps to the next one.

```python
while True:                       # "while True" loops forever...
    command = input("Type 'exit' to quit: ")
    if command == "exit":
        print("Goodbye!")
        break                     # ...until break ejects us
```

`while True:` looks scary (infinite!) but it's a common, useful pattern *when paired with `break`*. The loop runs until something inside decides to `break`.

```python
for number in range(1, 11):
    if number == 5:
        continue                  # skip printing 5
    print(number)                 # prints 1 2 3 4 6 7 8 9 10
```

> 🔑 `break` leaves the whole loop. `continue` just skips to the next pass. Mixing them up is common — say which you want out loud before typing it.

**📺 Watch/read:** [W3Schools: For Loops](https://www.w3schools.com/python/python_for_loops.asp) (see the "Break" and "Continue" sections).

## ⌨️ Guided Practice — type along
Type both examples. For the `continue` one, predict which numbers get skipped before running.

## 🛠️ Build Block — Master Password Vault 🔐
A login system that gives only **3 attempts**.

- [ ] Set the correct master key in a variable
- [ ] Allow up to 3 tries (a `for` loop with `range(3)`, or a `while` with a counter)
- [ ] If they enter it correctly, print "Access granted" and `break`
- [ ] If they use up all 3 tries, print "System locked down!" *after* the loop

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I limit it to 3 tries?</summary>

A `for` loop runs a fixed number of times:
```python
for attempt in range(3):     # 3 tries: 0, 1, 2
    guess = input("Enter key: ")
```
</details>

<details><summary>Hint 2 — How do I stop early on success?</summary>

Use `break` when they're right:
```python
if guess == master_key:
    print("Access granted!")
    break
```
</details>

<details><summary>Hint 3 — How do I detect "ran out of tries"?</summary>

One clean way: track success in a variable, then check it after the loop:
```python
unlocked = False
for attempt in range(3):
    guess = input("Enter key: ")
    if guess == master_key:
        unlocked = True
        break
    else:
        print("Wrong!")
if not unlocked:
    print("SYSTEM LOCKED DOWN!")
```
Full version: `solution/password_vault.py`.
</details>

## ⭐ Show & Tell
Demo **both** endings: unlock it on the first try, then run it again and fail 3 times to trigger the lockdown.

## 🧑‍🏫 Mentor note
The "did they run out of tries?" logic (a success flag checked after the loop) is a genuinely useful pattern they'll reuse. If they're close, point them to Hint 3.
