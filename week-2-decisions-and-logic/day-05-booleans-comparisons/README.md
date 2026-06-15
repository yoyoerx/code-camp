# Day 5 — Booleans & Comparisons (True vs. False)

> Week 2 · Day 5 of 24 · *Decisions & Logic*

## 🎯 Today's Goal
Teach the computer to **compare** things and answer with `True` or `False`.

## 🧩 Warm-Up (with your mentor)
Mentor says statements; you shout "TRUE!" or "FALSE!": *"A week has 7 days." "You are 40 feet tall." "Ice cream is cold."* Every comparison a computer makes ends in exactly one of those two answers.

## 🧠 Concept Quest
A **Boolean** is a value that is either `True` or `False` — nothing else. Computers make decisions by asking yes/no questions.

**Comparison operators** ask those questions:

| Operator | Asks | Example | Result |
|---|---|---|---|
| `>` | greater than? | `10 > 5` | `True` |
| `<` | less than? | `10 < 5` | `False` |
| `>=` | greater or equal? | `5 >= 5` | `True` |
| `<=` | less or equal? | `4 <= 3` | `False` |
| `==` | **equal?** | `7 == 7` | `True` |
| `!=` | not equal? | `7 != 8` | `True` |

> 🔑 The biggest trap: **`==` (two equals) asks a question; `=` (one equals) stores a value.** `age = 11` puts 11 in the box. `age == 11` asks "is age 11?" Mixing these up is the #1 beginner bug — circle it in your mind!

```python
my_age = 11
print(my_age > 10)   # True
print(my_age == 20)  # False
```

**📺 Watch/read:** [W3Schools: Booleans](https://www.w3schools.com/python/python_booleans.asp).

## ⌨️ Guided Practice — type along
Type the GUIDED PRACTICE comparisons and run them. Predict each answer *before* you run — then check if you were right!

## 🛠️ Build Block — Rollercoaster Ticket Booth 🎢
Many rides require riders to be at least **48 inches** tall. Build the height-check.

- [ ] Ask for the rider's height in inches (convert with `int()`!)
- [ ] Compare it to 48 using `>=` and store the `True`/`False` in a variable
- [ ] Print the rider's height and whether they're tall enough (the Boolean)

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I store a True/False answer?</summary>

A comparison *is* a value, so you can store it:
```python
tall_enough = height >= 48
print(tall_enough)
```
</details>

<details><summary>Hint 2 — Remember the int()!</summary>

Height comes from `input()`, so it's text. Convert it:
```python
height = int(input("Height in inches? "))
```
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
height = int(input("How tall are you in inches? "))
can_ride = height >= 48
print("Your height:", height)
print("Tall enough to ride?", can_ride)
```
Full version: `solution/ticket_booth.py`.
</details>

## ⭐ Show & Tell
Test with three heights: one clearly tall enough, one too short, and exactly 48. Explain why 48 gives `True` (because `>=` includes "equal to").

## 🧑‍🏫 Mentor note
If you see `=` where `==` belongs, Python gives a `SyntaxError` — a good, safe way to learn the difference. Tomorrow these Booleans become real decisions with `if`.
