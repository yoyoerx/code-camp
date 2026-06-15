# Day 12 — Loop Challenges & Visual Fun

> Week 3 · Day 12 of 24 · *Loops*

## 🎯 Today's Goal
Combine loops + decisions, meet the famous **FizzBuzz**, learn the **modulo** trick, and draw pictures with loops.

## 🧩 Warm-Up (with your mentor)
Count 1 to 20 out loud, but clap on every even number. How did you know which were even? They split into 2 evenly. That "leftover" idea is the **modulo** operator.

## 🧠 Concept Quest
**Modulo `%`** gives the *remainder* after division:
- `10 % 2` → `0` (10 splits evenly by 2, so it's **even**)
- `7 % 2` → `1` (leftover, so 7 is **odd**)
- `15 % 5` → `0` (15 splits evenly by 5)

So the even-check is: `if n % 2 == 0:`

**FizzBuzz** (a classic!): count 1→N, but for multiples of 3 print "Fizz", multiples of 5 print "Buzz", both print "FizzBuzz". Order matters — check "both" first!

**String multiplying** makes drawing easy:
```python
print("*" * 5)     # *****
print("#" * 3)     # ###
```
Combine with a loop to grow a shape:
```python
for i in range(1, 6):
    print("*" * i)   # a triangle!
```

**📺 Watch/read:** [Programiz: Arithmetic operators (`%`)](https://www.programiz.com/python-programming/operators#arithmetic) · search *"FizzBuzz explained for beginners"*.

## ⌨️ Guided Practice — type along
Type the FizzBuzz example (count to 20) and the triangle loop. Run and admire.

## 🛠️ Build Block — ASCII Art Generator 🎨
Ask for a character and a size, then draw a shape out of it.

- [ ] Ask for a symbol (like `*` or `#`) and a size number (`int()`)
- [ ] Use a loop with string-multiplying (`symbol * i`) to draw a **triangle** that grows
- [ ] Bonus: also draw a full square (`symbol * size` repeated `size` times)

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I make the triangle grow?</summary>

Multiply the symbol by the loop counter, which gets bigger each pass:
```python
for i in range(1, size + 1):
    print(symbol * i)
```
(`size + 1` so the last row has `size` symbols — remember range stops early.)
</details>

<details><summary>Hint 2 — How do I draw a square?</summary>

Every row is the same width, so print `symbol * size` once per row:
```python
for i in range(size):
    print(symbol * size)
```
</details>

<details><summary>Hint 3 — FizzBuzz order reminder</summary>

Check the "both" case FIRST, or it never runs:
```python
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
```
Full versions: `solution/ascii_art.py` and `solution/fizzbuzz.py`.
</details>

## ⭐ Show & Tell
Show your mentor a triangle, a square, and your FizzBuzz counting to 30. Try different symbols!

## 🧑‍🏫 Mentor note
Modulo `%` is new and a little abstract — the "even numbers split by 2 with no leftover" framing usually lands it. This is the last loops day before the big jump to Lists tomorrow.
