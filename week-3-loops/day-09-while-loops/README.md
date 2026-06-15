# Day 9 — `while` Loops (Do It Until…)

> Week 3 · Day 9 of 24 · *Loops*

## 🎯 Today's Goal
Make code **repeat** automatically with a `while` loop — and learn how to stop a runaway loop.

## 🧩 Warm-Up (with your mentor)
Remember the "Repeat" block in Scratch? Today's `while` loop is the text version. Mentor counts down from 5 out loud and "blasts off" — you'll make Python do exactly that.

## 🧠 Concept Quest
A **`while` loop** repeats a block of code *as long as* a condition stays `True`. It's like an `if` that keeps going:

```python
count = 5
while count > 0:
    print(count)
    count = count - 1     # <-- this MUST be here!
print("Blast off!")
```

How it runs: check `count > 0` → if true, run the indented block → check again → repeat. When `count` hits 0, the condition is false and the loop stops.

> ⚠️ **The infinite loop trap:** if you forget `count = count - 1`, `count` stays 5 forever and the loop **never ends**. Your program freezes. To escape: click inside the Terminal and press **Ctrl + C**. *Every* `while` loop needs something inside it that eventually makes the condition false.

**📺 Watch/read:** [W3Schools: While Loops](https://www.w3schools.com/python/python_while_loops.asp) · Video: [Kylie Ying — For Loops and While Loops](https://www.youtube.com/watch?v=zXaQ-ift74A) (covers both; great for this whole week).

## ⌨️ Guided Practice — type along
Type the countdown loop and run it. Then **try the trap on purpose**: comment out the `count = count - 1` line, run it, watch it spam forever, and stop it with **Ctrl + C**. Now you know how to escape! Put the line back.

## 🛠️ Build Block — Number Guessing Game 🔢
The computer "thinks" of a secret number and you keep guessing until you get it.

- [ ] Set a secret number in a variable (hardcode it, e.g. `secret = 7`)
- [ ] Use a `while` loop that keeps asking for a guess
- [ ] The loop should keep going **while** the guess is not equal to the secret
- [ ] When they finally match, print a congrats message *after* the loop

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I keep asking until they're right?</summary>

Get a first guess before the loop, then loop while it's wrong:
```python
guess = int(input("Guess: "))
while guess != secret:
    guess = int(input("Try again: "))
```
</details>

<details><summary>Hint 2 — How do I avoid an infinite loop here?</summary>

The `input()` inside the loop is what changes `guess` each time — that's what eventually makes the condition false. Make sure you ask for a *new* guess inside the loop!
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
secret = 7
guess = int(input("Guess my number (1-10): "))
while guess != secret:
    print("Nope! Guess again.")
    guess = int(input("Guess my number (1-10): "))
print("You got it! The number was", secret)
```
Full version: `solution/guessing_game.py`.
</details>

## ⭐ Show & Tell
Let your mentor play. Bonus: add hints like "too high!" / "too low!" inside the loop (peek at the solution for how).

## 🧑‍🏫 Mentor note
If the screen floods with output, that's an infinite loop — calmly press **Ctrl + C** in the Terminal. It's a normal rite of passage, not a disaster. Today's secret is hardcoded; on Day 15 they'll learn `random` to make it pick its own number.
