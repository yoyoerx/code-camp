# 🐾 Path A — Virtual Pet (Tamagotchi)

**The idea:** You adopt a digital pet. It gets hungry, bored, and tired over time. Your job is to keep it alive and happy by feeding, playing, and resting it. If any stat hits zero, the pet gets sad (or "runs away"). Survive as many days as you can!

*This is the friendliest path — a great choice if you want to feel successful fast.*

---

## 🧠 What you'll use
- A **dictionary** to hold your pet's stats
- A **`while` loop** for the main game
- **`if`/`elif`/`else`** for the menu
- **Functions** for each action (feed, play, sleep)
- **`random`** for surprise events, **`time.sleep()`** for drama

## 🐱 Suggested pet data (a dictionary!)

```python
pet = {
    "name": "Pixel",
    "hunger": 5,     # 0 = starving, 10 = full
    "fun": 5,        # 0 = bored, 10 = happy
    "energy": 5,     # 0 = exhausted, 10 = rested
    "age": 0,        # how many turns survived
}
```

## ✅ Feature checklist (your "must-haves")
- [ ] Ask the player to **name** their pet at the start.
- [ ] Show a **status screen** each turn (the pet's stats, maybe an ASCII face that changes with mood).
- [ ] A **menu** each turn: `1) Feed  2) Play  3) Sleep  4) Check status  5) Quit`.
- [ ] **Feeding** raises hunger, **playing** raises fun (but lowers energy), **sleeping** raises energy.
- [ ] Every turn, stats slowly **drop** on their own (time passes!).
- [ ] If any stat hits **0**, the game ends with a sad message.
- [ ] Track **age** (turns survived) and show it as the final score.

## 🛠️ Suggested build order
1. **Day 21:** Make the `pet` dictionary and a `show_status()` function. Build the menu loop so options print (they don't have to *do* anything yet).
2. **Day 22:** Make the menu options actually change the stats. Add the "stats drop each turn" rule and the lose condition.
3. **Day 23:** Add ASCII pet faces for happy/sad/hungry. Add a `random` event ("Pixel found a snack! +2 hunger"). Add `time.sleep()` pauses.
4. **Day 24:** Comment your code, test that weird menu inputs don't crash it, and show it off.

## 💡 Helpful snippets
Keeping a stat between 0 and 10 so it never goes weird:
```python
pet["hunger"] = pet["hunger"] + 3
if pet["hunger"] > 10:
    pet["hunger"] = 10
```

A mood face based on a stat:
```python
def pet_face(pet):
    if pet["fun"] >= 7:
        return "(^_^)"
    elif pet["fun"] >= 3:
        return "(o_o)"
    else:
        return "(T_T)"
```

## 🌟 Stretch goals (only if you finish early)
- Multiple pet *types* (cat, dragon, robot) with different starting stats.
- A "shop" where playing earns coins to buy treats.
- Save the high score (longest age survived) in a variable across rounds.

## 🆘 If you get stuck
- Reread **Day 16 (dictionaries)** and **Day 17–18 (functions)** — this project is mostly those two ideas combined.
- ASCII faces to copy: search "text emoticons" or build your own from `( ) ^ _ o T`.
