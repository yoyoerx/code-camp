# Day 21 — Modules & Project Blueprinting

> Week 6 · Day 21 of 24 · *Capstone* · 🏆 This is the big one!

## 🎯 Today's Goal
Choose your capstone, **plan it on paper**, learn two helpful modules, and build the skeleton (main menu loop + starting variables).

## 🧩 Kickoff (with your mentor — important today!)
Read all three blueprints in [`../../capstone-projects/`](../../capstone-projects/) together, then choose **one**. The most important question of the whole week:

> 🧑‍🏫 **"What is the *simplest version* of this that still works and is fun?"** Build THAT first. You can always add more later. Kids almost always pick something too big — your mentor's job today is to help you cut it down to something you can finish in 4 days.

## 🧠 Concept Quest
**Modules** are toolboxes other people wrote that you `import` and use. You've met `random`. Meet `time`:

```python
import random
import time

print("Dealing cards...")
time.sleep(2)            # pause for 2 dramatic seconds
print(random.randint(1, 6))
```

`time.sleep(seconds)` pauses your program — perfect for suspense ("Rolling the dice...⏳").

**Blueprinting = planning before building.** Real programmers don't just start typing. On paper, draw a **flowchart**: boxes for each step, arrows for what happens next. For a game: Start → Show menu → Player chooses → React → Check win/lose → back to menu.

## ✏️ Build Block — Plan + Scaffold

**Part 1 — On paper (do this first!):**
- [ ] Write your game's name and one-sentence goal at the top
- [ ] Draw a flowchart of the main loop (what repeats every turn?)
- [ ] List the variables you'll need to track (score? health? money? a list? a dictionary?)
- [ ] Circle the **simplest version** you'll build first

**Part 2 — In `my_capstone.py`:**
- [ ] Add your `import`s at the top
- [ ] Create your starting variables
- [ ] Build the **main menu loop** (it can just print options and read a choice for now — the options don't have to *work* yet)

> 💡 `my_capstone.py` in this folder is a **generic scaffold** to get you started. Read its comments and shape it to *your* chosen project. You'll keep building this same file on Days 22–24.

## 🆘 Stuck?
- Reread the blueprint for your chosen path — it has a suggested data setup and build order.
- Menu loop pattern is exactly the Day 14 Grocery List structure (`while True:` + `if`/`elif` on the choice + `break` to quit).
- **There's no `solution/` folder this week — you're the author now!** Your mentor and the blueprints are your support.

## ⭐ Show & Tell
Show your mentor your paper flowchart and run your menu skeleton (even if the options don't do anything yet). A clear plan is today's real win.

## 🧑‍🏫 Mentor note
**Scope-cutting is the whole job today.** Praise a small, finishable plan over an ambitious one. A working tiny game on Day 24 beats a broken big one. Make sure the flowchart exists *before* they code.
