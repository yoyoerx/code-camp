# Day 17 — Intro to Functions (Reusable Spells)

> Week 5 · Day 17 of 24 · *Functions*

## 🎯 Today's Goal
Write your own **functions** — name a block of code once, then "cast" it anytime.

## 🧩 Warm-Up (with your mentor)
Think of a magic word that always does the same thing — "Abracadabra!" Every time you say it, *poof*, same effect. A function is your own custom magic word for code.

## 🧠 Concept Quest
A **function** is a named, reusable block of code. You **define** it once with `def`, then **call** it by name as many times as you want:

```python
def cast_fireball():
    print("=========================")
    print("🔥 A fireball flies out! 🔥")
    print("=========================")

cast_fireball()      # call it...
cast_fireball()      # ...and again! No retyping.
```

Two parts:
1. **Define** it: `def name():` followed by an indented block (the spell's instructions).
2. **Call** it: just write `name()` wherever you want it to run.

> 🔑 Defining a function does **not** run it — it just teaches Python the spell. Nothing happens until you *call* it. A super common first bug: writing a great function and forgetting to call it (so nothing prints).

Why bother? **Don't Repeat Yourself.** If you need the same fancy banner 5 times, write it once as a function and call it 5 times. Change it in one place, it updates everywhere.

**📺 Watch/read:** [W3Schools: Functions](https://www.w3schools.com/python/python_functions.asp) · Video: [Kylie Ying — Using Functions in Python](https://www.youtube.com/watch?v=WRI4fXDIXWM).

## ⌨️ Guided Practice — type along
Type the `cast_fireball` function and call it twice. Notice: the function block is *defined* at the top but only *runs* where you call it.

## 🛠️ Build Block — Custom Banner Drawer 🎌
Make reusable ASCII banners and use them to frame a little story scene.

- [ ] Write **3 different functions**, each printing a different stylized ASCII banner (sci-fi, pirate, starry…)
- [ ] In a "main" part at the bottom, **call** your functions in an order that tells a tiny story (banner, text, banner, text…)

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I define one banner?</summary>

```python
def pirate_banner():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("   🏴‍☠️ AHOY MATEY 🏴‍☠️   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
```
</details>

<details><summary>Hint 2 — Nothing prints when I run it!</summary>

You probably defined the functions but didn't **call** them. Add calls at the bottom:
```python
pirate_banner()
print("The ship sailed into the storm...")
```
</details>

<details><summary>Hint 3 — Show me the structure</summary>

```python
def scifi_banner():
    print("[============= SECTOR 7 =============]")

def pirate_banner():
    print("~~~~~~~~ AHOY MATEY ~~~~~~~~")

def star_banner():
    print("* . * . * . THE END . * . * . *")

# main story:
scifi_banner()
print("Our hero docked their ship.")
pirate_banner()
print("Pirates attacked!")
star_banner()
```
Full version: `solution/banner_drawer.py`.
</details>

## ⭐ Show & Tell
Run your framed story scene. Point out to your mentor how each banner is written **once** but could be reused anywhere.

## 🧑‍🏫 Mentor note
Functions are the week's big conceptual leap. The #1 stumble is *defining but not calling*. If "nothing happens," that's almost always it. Extra practice if they want it: [CodingBat Python](https://codingbat.com/python).
