# Day 4 — Numbers & Simple Math (The Calculator Brain)

> Week 1 · Day 4 of 24 · *Variables & Input/Output*

## 🎯 Today's Goal
Do math in Python, and learn the **most important gotcha for beginners**: turning text into numbers with `int()`.

## 🧩 Warm-Up (with your mentor)
Quick mental math race: mentor calls out "7 × 8", "100 − 37", "12 ÷ 4". Computers do this *instantly* and never get tired. Today you build a calculator.

## 🧠 Concept Quest
Python's math operators:

| Symbol | Means | Example |
|---|---|---|
| `+` | add | `5 + 3` → `8` |
| `-` | subtract | `5 - 3` → `2` |
| `*` | multiply | `5 * 3` → `15` |
| `/` | divide | `6 / 2` → `3.0` |

**The big gotcha:** `input()` always gives back **text**, even if the user types `5`. You can't multiply text! So you must **convert** it to a number with `int()` (short for *integer*, a whole number):

```python
user_num = input("Enter a number: ")   # this is the TEXT "5"
num = int(user_num)                     # now it's the NUMBER 5
print("Times ten is:", num * 10)
```

If you skip `int()` and try math on text, Python throws a `TypeError` or does something weird (`"5" * 3` gives `"555"`!). Whenever you want math, `int()` it first.

**📺 Watch/read:** [W3Schools: Casting (int/str)](https://www.w3schools.com/python/python_casting.asp).

## ⌨️ Guided Practice — type along
Type the GUIDED PRACTICE lines. **Then experiment:** try removing `int()` and see what `"5" * 10` does. Errors and surprises are how you learn!

## 🛠️ Build Block — Dog-to-Human Age Converter 🐶
Dogs age about **7× faster** than humans. Build a calculator that personalizes the result.

- [ ] Ask for the user's **name**
- [ ] Ask for their **dog's name**
- [ ] Ask for the dog's age (a number) — and **convert it with `int()`**
- [ ] Multiply the age by 7
- [ ] Print a fun, personalized message with the result

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — My math gives a weird answer like "333333"</summary>

You forgot `int()`! The age is still text. Convert it:
```python
dog_age = int(input("Dog's age? "))
```
</details>

<details><summary>Hint 2 — Can I convert right inside input()?</summary>

Yes — wrap `input()` in `int()` in one step (read it inside-out: input first, then int):
```python
dog_age = int(input("How old is your dog? "))
```
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
owner = input("Your name? ")
dog = input("Your dog's name? ")
dog_age = int(input("Dog's age in years? "))
human_years = dog_age * 7
print(owner + ",", dog, "is", human_years, "in dog years!")
```
Full version: `solution/dog_age.py`.
</details>

## ⭐ Show & Tell
Run it with different dog ages. Bonus: what's *your* age in dog years? 😄

## 🧑‍🏫 Mentor note
The `int()` rule is the single most important idea this week — it comes back constantly. If they hit a `ValueError`, it means they (or you) typed letters where a number was expected. That's expected; just type a number.
