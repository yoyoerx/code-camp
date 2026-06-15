# Day 10 — `for` Loops & `range()` (Counting Loops)

> Week 3 · Day 10 of 24 · *Loops*

## 🎯 Today's Goal
Repeat code a **specific number of times** with a `for` loop and `range()`.

## 🧩 Warm-Up (with your mentor)
Do 10 jumping jacks while counting out loud. You knew *exactly* how many — 10. A `for` loop is for when you know the count ahead of time (unlike `while`, which goes until something changes).

## 🧠 Concept Quest
A **`for` loop** repeats a set number of times. `range(start, stop)` makes the numbers to count through. Important: `range` **stops *before*** the stop number!

```python
for i in range(1, 11):     # counts 1, 2, 3, ... up to 10 (NOT 11)
    print("Step number:", i)
```

- `i` is a variable that holds the current number each time around (you can name it anything).
- `range(1, 11)` → 1 through 10. `range(1, 13)` → 1 through 12.
- The indented block runs once for each number.

> 🔑 `while` vs `for`: use **`while`** when you loop *until something happens* (Day 9's guessing game). Use **`for`** when you know *how many times* (counting, tables, a fixed list).

**📺 Watch/read:** [W3Schools: For Loops](https://www.w3schools.com/python/python_for_loops.asp).

## ⌨️ Guided Practice — type along
Type the `range(1, 11)` example. Then experiment: change it to `range(1, 6)`, then `range(0, 20)`. Predict the output before each run.

## 🛠️ Build Block — Multiplication Table Generator ✖️
Ask for a number and print its full times-table.

- [ ] Ask the user for a number (convert with `int()`)
- [ ] Use a `for` loop with `range(1, 13)` to go 1 through 12
- [ ] Each line should print like `5 x 1 = 5`, `5 x 2 = 10`, …
- [ ] (The math: `number * i`)

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I print "5 x 1 = 5"?</summary>

Use commas and do the math inside `print()`:
```python
print(number, "x", i, "=", number * i)
```
</details>

<details><summary>Hint 2 — What range gives 1 through 12?</summary>

`range(1, 13)` — remember it stops *before* 13.
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
number = int(input("Pick a number: "))
for i in range(1, 13):
    print(number, "x", i, "=", number * i)
```
Full version: `solution/times_table.py`.
</details>

## ⭐ Show & Tell
Generate the table for a big number like 99 and watch Python finish it instantly. Show your mentor the times-table you find hardest to memorize!

## 🧑‍🏫 Mentor note
The "stops before the stop number" rule of `range` surprises everyone at first. If their table only goes to 11, that's the clue — they need `range(1, 13)`.
