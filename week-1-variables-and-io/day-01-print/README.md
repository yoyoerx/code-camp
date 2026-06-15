# Day 1 — `print()` (Our First Words)

> Week 1 · Day 1 of 24 · *Variables & Input/Output*

## 🎯 Today's Goal
Make the computer say things on screen using `print()` — and meet your first error message (it's friendly, promise).

## 🧩 Warm-Up (with your mentor)
Give your mentor instructions to make a peanut-butter sandwich — but they must do **exactly** what you say, no guessing. ("Pick up bread." "Which?" 😅) That's what programming is: super-precise instructions for something that can't guess.

## 🧠 Concept Quest
A **program** is a recipe the computer follows *exactly*. Today's instruction is `print()` — it shows text on the screen.

Text you want to show must be wrapped in **quotes**. We call quoted text a **string**:

```python
print("Hello World!")
```

The quotes tell Python *"this is words to show, not a command to run."* If you forget a quote, Python stops and shows a **`SyntaxError`**. That's not Python being mean — it's Python pointing at the exact spot it got confused, like a helpful spell-checker. We **want** to see errors; they're clues.

**📺 Watch/read:** [W3Schools: print()](https://www.w3schools.com/python/ref_func_print.asp) · Video: [Kylie Ying — Basic Types and Operators (Lesson 1)](https://www.youtube.com/watch?v=GGdmIL85qos) (watch the first few minutes on text and printing).

## ⌨️ Guided Practice — type along
Open **`starter.py`**. Type the lines in the GUIDED PRACTICE section yourself (don't copy-paste — typing builds muscle memory). Click **▶ Run** and watch the Terminal.

Then **break it on purpose:** delete one `"` and run again. Read the `SyntaxError`. Put the quote back. You just debugged your first program! 🎉

## 🛠️ Build Block — The Comedy Robot 🤖
Your mission: write a script where a robot introduces itself, tells **three jokes**, and shows off some ASCII art.

Open `starter.py` and complete the `# TODO`s. Your robot should:
- [ ] Introduce itself with a name
- [ ] Tell 3 jokes (each on its own `print()`)
- [ ] Use a **blank** `print()` between jokes for spacing
- [ ] Finish with an ASCII art robot face

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I make an empty line?</summary>

Just call `print()` with nothing inside the parentheses:
```python
print()
```
</details>

<details><summary>Hint 2 — How do I draw a robot face?</summary>

Each line of the face is its own string. Backslashes need a partner to behave — use two `\\` if a line ends in a slash:
```python
print("  [ O _ O ]  ")
print("  |  ---  |  ")
```
</details>

<details><summary>Hint 3 — Show me the shape of the whole thing</summary>

```python
print("BEEP BOOP! I am Chuckle-Bot.")
print()
print("Why did the robot cross the road?")
print("To get to the other site! (get it? web-site)")
```
Keep going for jokes 2 and 3. Full version is in `solution/comedy_robot.py`.
</details>

## ⭐ Show & Tell
Run your comedy routine for your mentor. Bonus: read the jokes out loud in a robot voice. 🤖

## 🧑‍🏫 Mentor note
First day — the win is *"I typed code and made the computer do something."* If setup hiccups, that's normal; check `SETUP.md` together.
