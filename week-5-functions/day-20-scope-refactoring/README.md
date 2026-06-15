# Day 20 — Scope & Refactoring

> Week 5 · Day 20 of 24 · *Functions*

## 🎯 Today's Goal
Learn where variables "live" (**scope**), and **refactor** an old messy program into clean functions. This is the perfect warm-up for the capstone!

## 🧩 Warm-Up (with your mentor)
Find one of your earlier programs (the Day 7 Adventure Game or the Day 11 Password Vault). Skim it. Today you'll give it a "glow-up" — same behavior, much cleaner code.

## 🧠 Concept Quest
**Scope** = where a variable can be seen. A variable made *inside* a function is **local** — it lives only inside that function and disappears when the function ends:

```python
def make_score():
    points = 10        # local: only exists inside make_score
    return points

print(make_score())    # 10
print(points)          # ERROR! 'points' doesn't exist out here
```

That's a *good* thing — functions stay tidy and don't accidentally mess with each other's variables. Pass data **in** with parameters and get results **out** with `return`.

**Refactoring** = rewriting code to be cleaner *without changing what it does*. The goal is code that's easy to read and reuse. A common refactor: take a long script and group each chunk into a well-named function, then a short "main" section that calls them in order:

```python
def show_intro():
    ...
def play_round():
    ...

# main:
show_intro()
play_round()
```

> 🔑 Refactoring is what real programmers do constantly. Working code is step one; *clean* working code is step two. Clean code is a gift to "future you."

**📺 Watch/read:** [W3Schools: Scope](https://www.w3schools.com/python/python_scope.asp) · search *"what is refactoring for beginners"*.

## ⌨️ Guided Practice — type along
Type the scope example and watch the `NameError` when you try to use a local variable outside its function. That error *is* the lesson — local means local.

## 🛠️ Build Block — Refactor Day 🧹
Pick one earlier game (Adventure Game or Password Vault) and reorganize it into functions.

- [ ] Copy your old program's code into `starter.py` (or rewrite it)
- [ ] Identify the natural "chunks" (intro, get input, decide outcome…)
- [ ] Wrap each chunk in a clearly named function (`show_intro()`, `get_guess()`, …)
- [ ] At the bottom, write a short "main" section that calls them in order
- [ ] Run it — it should behave **exactly the same**, just be cleaner!

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — Where do I even start?</summary>

Don't rewrite logic — just *wrap* existing chunks. Find a block that does one job, put `def do_that_thing():` above it, and indent the block under it. Then call `do_that_thing()` at the bottom.
</details>

<details><summary>Hint 2 — A variable broke after I moved it into a function</summary>

That's scope! If `play_round()` needs a value from `setup()`, have `setup()` **return** it, and pass it in:
```python
secret = setup()
play_round(secret)
```
</details>

<details><summary>Hint 3 — Show me a refactored skeleton</summary>

See `solution/refactored_vault.py` for the Day 11 Password Vault rewritten cleanly into `check_password()` and a main section. Compare it side-by-side with your Day 11 version.
</details>

## ⭐ Show & Tell
Open your **old** version and the **refactored** version side by side. Show your mentor how the new one reads like a clear list of steps. Same game, cleaner code!

## 🧑‍🏫 Mentor note
There's no single "right" refactor — any reasonable grouping into named functions is a win. The learning is in *recognizing chunks*. This is excellent practice for next week, where they'll structure a whole capstone from scratch. **Week 5 complete — onward to the capstone!** 🎉
