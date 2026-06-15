# 🚀 Path B — Space Cargo Trader

**The idea:** You're a space trader with a small ship and 100 credits. Fly between planets, buy goods where they're cheap, sell where they're pricey, dodge random space events, and try to reach **1,000 credits** before you run out of fuel or turns.

*This is the math-and-strategy path — great if you like money, planning, and "buy low, sell high."*

---

## 🧠 What you'll use
- **Dictionaries** for planets and prices
- A **`while` loop** for the main game (each turn = one decision)
- **`if`/`elif`/`else`** menus
- **`random`** for price changes and events
- **Functions** for travel, buy, sell

## 🪐 Suggested data

```python
credits = 100
fuel = 10
cargo = 0          # units of "space ore" you're carrying
current_planet = "Terra"

planets = {
    "Terra":  {"price": 20},
    "Mars":   {"price": 35},
    "Europa": {"price": 50},
}
```

## ✅ Feature checklist (your "must-haves")
- [ ] Show a **status bar** each turn: credits, fuel, cargo, current planet.
- [ ] A **menu**: `1) Buy ore  2) Sell ore  3) Travel  4) Quit`.
- [ ] **Buying** ore costs `price × amount` credits and adds to cargo.
- [ ] **Selling** ore gives you `price × amount` credits.
- [ ] **Traveling** to a planet uses 1 fuel and changes the current price.
- [ ] Each turn, prices **change a little** using `random` (so trades aren't always the same).
- [ ] **Win** at 1,000 credits. **Lose** if fuel hits 0 before then.

## 🛠️ Suggested build order
1. **Day 21:** Set up the variables and `planets` dictionary. Build the menu loop and a `show_status()` function.
2. **Day 22:** Make Buy, Sell, and Travel work. Add the win (1000 credits) and lose (0 fuel) checks.
3. **Day 23:** Add `random` price swings and a random event each travel ("Pirates! Lose 2 cargo." / "Lucky find! +15 credits"). Add ASCII + `time.sleep()`.
4. **Day 24:** Comment, guard against bad inputs (buying more than you can afford!), and present.

## 💡 Helpful snippets
Random price each visit:
```python
import random
price = random.randint(15, 55)
```

Don't let the player buy what they can't afford:
```python
cost = price * amount
if cost > credits:
    print("Not enough credits!")
else:
    credits = credits - cost
    cargo = cargo + amount
```

## 🌟 Stretch goals
- More planets with different price ranges (some risky, some safe).
- A cargo **hold limit** so you can't carry infinite ore.
- A "ship upgrade" you can buy that increases fuel capacity.

## 🆘 If you get stuck
- The trickiest bug is usually letting the player spend credits/cargo they don't have. Add an `if` check before **every** buy/sell/travel.
- Reread **Day 4 (math + int())**, **Day 16 (dictionaries)**, and **Day 15 (random)**.
