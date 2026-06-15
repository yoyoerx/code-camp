# Day 2 — Variables (Digital Storage Boxes)

> Week 1 · Day 2 of 24 · *Variables & Input/Output*

## 🎯 Today's Goal
Learn to **store** information in named boxes called *variables*, and combine them in `print()`.

## 🧩 Warm-Up (with your mentor)
Grab a real box or cup and a sticky note. Write `name` on the note, stick it on the box, and put a slip of paper with your name inside. That box is now a **variable**. What if you swap the paper inside for a different name? The label stays the same; the value changes. That's exactly how variables work.

## 🧠 Concept Quest
A **variable** is a labeled box that stores a value so you can use it later:

```python
player_name = "Sonic"
gold_coins = 45
```

- The `=` means *"put the value on the right into the box on the left."* (It does **not** mean "equals" like in math.)
- `"Sonic"` is text (a **string**) — it has quotes.
- `45` is a **number** — no quotes, so you can do math on it.

> 🔑 Big idea: `"10"` (with quotes) is *text*. `10` (no quotes) is a *number you can add*. They look alike but behave very differently — you'll see why on Day 4.

You can print several things in one line by separating them with **commas** (Python adds spaces for you):

```python
print("Player:", player_name, "has", gold_coins, "coins")
```

**📺 Watch/read:** [W3Schools: Variables](https://www.w3schools.com/python/python_variables.asp) · Video: [Kylie Ying — How to Use Variables](https://www.youtube.com/watch?v=68YPgQE_zm4).

## ⌨️ Guided Practice — type along
In `starter.py`, type the GUIDED PRACTICE lines: make two variables, print each, then print them together with commas. Run it.

## 🛠️ Build Block — Mad Libs Generator 📖
Make a silly auto-story! Define **5–6 variables** at the top (like `adjective`, `animal`, `place`, `hero_name`, `food`), then print a wacky paragraph that uses all of them.

- [ ] Create at least 5 variables with funny values
- [ ] Print a story (2–4 sentences) that uses every variable
- [ ] After it works, **change the variable values** and re-run to see the whole story change!

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I put a variable inside a sentence?</summary>

Use commas inside `print()`:
```python
print("One day, a", adjective, animal, "went to", place)
```
</details>

<details><summary>Hint 2 — My variable name has an error</summary>

Variable names can't have spaces — use an underscore: `hero_name`, not `hero name`. And don't put quotes around the variable name when you use it (quotes make it text again!).
</details>

<details><summary>Hint 3 — Show me a starting shape</summary>

```python
adjective = "smelly"
animal = "llama"
place = "the moon"
print("Once upon a time, a", adjective, animal, "flew to", place + ".")
```
Full version: `solution/mad_libs.py`.
</details>

## ⭐ Show & Tell
Run your Mad Libs, then **change 3 variable values** in front of your mentor and re-run — show how one tiny change rewrites the whole story.

## 🧑‍🏫 Mentor note
Watch for quotes-around-variable-names (a super common mix-up). If they write `print("hero_name")` they'll see the words, not the value — a great teachable moment.
