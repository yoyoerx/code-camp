# Day 6 — `if` / `else` & Indentation (Choosing Paths)

> Week 2 · Day 6 of 24 · *Decisions & Logic*

## 🎯 Today's Goal
Make your program **do different things** depending on the answer — and master Python's famous **indentation**.

## 🧩 Warm-Up (with your mentor)
Draw a fork in the road on paper. Left path: "score ≥ 60 → You passed!" Right path: "otherwise → Try again." Programs are full of these forks. Today you build them.

## 🧠 Concept Quest
`if` runs code **only when** a condition is `True`. `else` runs when it's `False`:

```python
score = int(input("What was your test score? "))
if score >= 60:
    print("You passed! Great job!")
else:
    print("Let's study more. You can do it!")
```

**The two rules that trip everyone up:**
1. **The colon `:`** goes at the end of the `if` line and the `else` line.
2. **Indentation** (the spaces at the start of a line) is how Python knows what's *inside* the `if`. Indented lines run only when the condition is true. VS Code adds the indent automatically when you type the colon and press Enter — let it help you.

> 🔑 If your indenting is off, Python says `IndentationError`. It's the most common beginner error — and it's just Python saying "your spacing doesn't line up." Make every line in a block start with the *same* number of spaces (4 is standard).

**📺 Watch/read:** [W3Schools: If...Else](https://www.w3schools.com/python/python_conditions.asp) · Video: [Kylie Ying — Conditionals: if, elif, else (Lesson 5)](https://www.youtube.com/watch?v=iO1nQMPIuMs).

## ⌨️ Guided Practice — type along
Type the GUIDED PRACTICE `if`/`else`. Watch how VS Code auto-indents after the colon. Run it with a high score and a low score.

## 🛠️ Build Block — Secret Passcode Door 🚪
Build a digital vault that only opens with the right password.

- [ ] Ask the user for the secret password
- [ ] If they type it correctly (you pick the password, e.g. `"open-sesame"`), print treasure/victory art
- [ ] Otherwise (`else`), print an alarm/warning
- [ ] Use `==` to compare!

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I check if the password matches?</summary>

Compare the input to the secret with `==`:
```python
if guess == "open-sesame":
    print("The door opens!")
else:
    print("ALARM! Wrong password!")
```
</details>

<details><summary>Hint 2 — I get an IndentationError</summary>

Every line *inside* the `if` or `else` must be indented the same amount (4 spaces). Lines *outside* the if go back to the left margin. Let VS Code auto-indent after you type `:` and press Enter.
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
secret = "open-sesame"
guess = input("Speak the secret password: ")
if guess == secret:
    print("💰 The vault swings open! Treasure is yours! 💰")
else:
    print("🚨 INTRUDER ALERT! 🚨")
```
Full version: `solution/passcode_door.py`.
</details>

## ⭐ Show & Tell
Demo **both** outcomes for your mentor: open it with the right password, then trigger the alarm with a wrong one.

## 🧑‍🏫 Mentor note
⚠️ **Indentation day** — one of the two flagged "lean in" days. Consider sitting in for the Concept Quest. Turning on VS Code's *render whitespace* (View → Appearance, or `editor.renderWhitespace`) makes spacing visible and helps a lot.
