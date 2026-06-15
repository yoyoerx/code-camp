# Day 22 — Core Logic Engineering

> Week 6 · Day 22 of 24 · *Capstone*

## 🎯 Today's Goal
Make your game actually **work**. Get a rough, ugly, *playable* prototype running — including a way to win or lose.

> 📂 Keep building yesterday's `my_capstone.py` (in the `day-21-blueprinting` folder). Just keep it open and keep going — don't start a new file.

## 🧩 Kickoff (with your mentor)
Look at your flowchart from Day 21. Point to the part you're building today: the **core loop** — what happens every single turn.

## 🧠 Concept Quest — Pseudocode First
Pro move: before writing real Python, write your plan as **comments** in plain English. Then fill in the code under each comment.

```python
# ask the player how much to bet
# deal two cards to the player
# while the player wants to hit:
#     give them another card
#     if their total > 21: they bust, stop
# compare to the dealer and decide who wins
# update the player's money
```

Now each comment is a tiny to-do. Replace one comment at a time with real code. If you get stuck, the *unfinished* comments still describe exactly what's left.

> 🔑 "Working but ugly" is the goal today. No colors, no art, no polish — just the rules working. Polish is tomorrow's job. Resist the urge to make it pretty before it works.

## 🛠️ Build Block
- [ ] Turn each menu option into real working code (use your blueprint's snippets!)
- [ ] Write the **core turn logic** (the math/rules of your game)
- [ ] Add the **win condition** and the **lose condition** — and `break` the loop when the game ends
- [ ] Get a full game playable start-to-finish, even if it's plain

## 🆘 Stuck?
- **Build in tiny pieces.** Get ONE option working completely before starting the next. Run constantly.
- Reread your chosen blueprint in `../../capstone-projects/` — it has snippets for the trickiest parts.
- Reuse patterns you already know: menu loop (Day 14), keeping score (Day 8), `random` (Day 15), functions (Day 17–19).
- 🧑‍🏫 If a specific rule has you stuck for 15+ minutes, that's a perfect mentor moment — explain out loud what you *want* it to do.

## ⭐ Show & Tell
Play a full round of your prototype for your mentor — bugs and all. Reaching "I can play it start to finish" is a huge milestone. 🎉

## 🧑‍🏫 Mentor note
Encourage **frequent running** — small changes, run, repeat. The pseudocode-comments technique really helps kids who freeze at a blank section; if they're stuck, ask them to *write the plan as comments first*, then code one line at a time.
