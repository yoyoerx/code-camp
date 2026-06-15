# Day 8 — Debugging & Defensive Coding

> Week 2 · Day 8 of 24 · *Decisions & Logic*

## 🎯 Today's Goal
Become a **bug detective**: read error messages, fix them calmly, and write code that doesn't crash when users type weird things.

## 🧩 Warm-Up (with your mentor)
"Spot the bug" out loud: your mentor reads these and you say what's wrong —
1. `print("Hello)` 2. `if score > 60 print("hi")` 3. `print(nmae)`
(Answers: missing quote · missing colon · misspelled variable.)

## 🧠 Concept Quest
Every programmer writes bugs *constantly*. The skill isn't avoiding them — it's **reading the clues** and fixing them. When Python breaks, it prints a red **traceback**. Read it bottom-up:

```
  File "trivia.py", line 5, in <module>
    score = score + 1
NameError: name 'score' is not defined
```

- **Last line** = the *type* of problem (`NameError` → a name Python doesn't recognize).
- **`line 5`** = exactly where to look.

Common error types:
| Error | Usually means |
|---|---|
| `SyntaxError` | a typo — missing `"`, `)`, or `:` |
| `IndentationError` | spacing at the start of a line is off |
| `NameError` | misspelled variable, or text missing quotes |
| `ValueError` | gave `int()` something that isn't a number |

**Defensive coding** = expecting weird input. If you ask "Python" but the user types "PYTHON" or "python", you can make them all match by lowercasing first with **`.lower()`**:

```python
answer = input("Best language? ").lower()   # "PYTHON" becomes "python"
if answer == "python":
    print("Correct!")
```

**📺 Watch/read:** [W3Schools: Try...Except (errors)](https://www.w3schools.com/python/python_try_except.asp).

## ⌨️ Guided Practice — type along
`starter.py` has a **BROKEN** section on purpose. Run it, read the traceback, fix the bug, run again. There are 3 bugs to squash. 🐛🔨

## 🛠️ Build Block — Ultimate Trivia Challenge ❓
Build a 3-question quiz that keeps score and accepts answers in any capitalization.

- [ ] Start a `score` variable at 0
- [ ] Ask 3 questions; use `.lower()` so "Paris", "paris", "PARIS" all count
- [ ] Add 1 to `score` for each correct answer
- [ ] At the end, print the final score out of 3

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I keep score?</summary>

Make a counter and add to it when they're right:
```python
score = 0
if answer == "paris":
    score = score + 1
```
</details>

<details><summary>Hint 2 — How do I accept any capitalization?</summary>

Lowercase the input, then compare to a lowercase answer:
```python
answer = input("Capital of France? ").lower()
if answer == "paris":
    ...
```
</details>

<details><summary>Hint 3 — Show me the shape of one question</summary>

```python
score = 0
a1 = input("Q1: Capital of France? ").lower()
if a1 == "paris":
    print("Correct!")
    score = score + 1
else:
    print("It was Paris.")
# ...repeat for Q2 and Q3...
print("Final score:", score, "out of 3")
```
Full version: `solution/trivia_challenge.py`.
</details>

## ⭐ Show & Tell
Run the quiz on your mentor — and have them **try to break it** by typing weird capitalization. Show that `.lower()` keeps it working!

## 🧑‍🏫 Mentor note
🔎 **Reading-errors day** — the second flagged "lean in" day. Sit in for the Concept Quest if you can. The big mindset win: *errors are clues, not failures.* Stay relaxed; your calm becomes their confidence.
