# Day 23 — Polish, Bugs & ASCII Art

> Week 6 · Day 23 of 24 · *Capstone*

## 🎯 Today's Goal
Turn your working-but-plain game into something that looks and feels **finished**.

> 📂 Still building the same `my_capstone.py`. Today it gets its glow-up. ✨

## 🧩 Kickoff (with your mentor)
Play your prototype together and write down 3 things that would make it feel more polished or fun. Pick the easiest 2 to do first.

## 🧠 Concept Quest — Game Feel
Small touches make a big difference:

- **Title splash screen:** big ASCII art at the start. Make one at [patorjk.com/software/taag](https://patorjk.com/software/taag/) — type your game's name and copy the art in.
- **Borders & spacing:** wrap important messages in lines like `print("=" * 30)` so they stand out.
- **Suspense with `time.sleep()`:** `print("Rolling...")` → `time.sleep(1.5)` → show the result. Drama!
- **Input safety (defensive coding!):** weird answers shouldn't crash your game. Guard against them:

```python
choice = input("Pick 1-4: ")
if choice not in ["1", "2", "3", "4"]:
    print("That's not an option!")
    continue          # skip back to the top of the loop
```

> 🔑 The #1 capstone crash is `int()` on something that isn't a number. If you ask for a number, either check it first or keep numbers as menu choices the player picks, not types.

## 🛠️ Build Block
- [ ] Add an ASCII **title splash screen**
- [ ] Add clear **instructions** so a new player knows how to play
- [ ] Add at least one `time.sleep()` for drama
- [ ] Make sure **weird inputs don't crash it** (test by typing nonsense on purpose!)
- [ ] Bonus: track a **high score** across rounds, or add a `random` surprise event

## 🆘 Stuck?
- Test like a villain: try to *break* your own game (empty input, huge numbers, letters where numbers go). Each crash you find and fix makes it stronger.
- ASCII art generators: [patorjk TAAG](https://patorjk.com/software/taag/) for big text titles.
- 🧑‍🏫 Stuck on a stubborn bug? Use the rubber-duck trick with your mentor: explain the broken part line by line out loud.

## ⭐ Show & Tell
Show off the *before vs after* — describe how it looked yesterday versus the polished version now. Let your mentor try to crash it!

## 🧑‍🏫 Mentor note
"Test like a villain" is genuinely how QA testers work — kids love trying to break things, and it teaches real defensive coding. Help them keep scope sane: a polished small game beats an unfinished big one. Tomorrow is the showcase — plan who to invite!
