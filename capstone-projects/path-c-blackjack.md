# 🃏 Path C — Blackjack Casino

**The idea:** Play the classic card game against the computer "dealer." You bet pretend money, get dealt cards, and choose to **hit** (take another card) or **stand** (stop). Get as close to **21** as you can without going over. Beat the dealer to win your bet!

*This is the spiciest path — the most logic and rules. Choose it if you love puzzles and card games.*

---

## 🧠 What you'll use
- A **list** to represent the deck/cards
- **`random`** to draw cards
- A **`while` loop** for hitting, and another for playing multiple rounds
- **`if`/`elif`/`else`** for the rules
- **Functions** for drawing a card and scoring a hand

## 🎴 Suggested data

```python
import random

money = 100
# A simple deck: numbers 2-11. (We'll treat face cards as 10 and Ace as 11 to start.)
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
```

## ✅ Feature checklist (your "must-haves")
- [ ] Ask the player how much to **bet** each round.
- [ ] Deal the player **2 cards** and the dealer **2 cards** (show only 1 dealer card).
- [ ] Let the player **hit or stand** in a loop, adding card values to their total.
- [ ] **Bust** (over 21) = player loses the bet immediately.
- [ ] After the player stands, the **dealer draws** until reaching at least 17.
- [ ] Compare totals: closer to 21 (without busting) **wins**.
- [ ] Update **money**; the game ends when the player quits or runs out of money.

## 🛠️ Suggested build order
1. **Day 21:** Set up `money` and the `card_values` list. Write a `draw_card()` function using `random.choice()`. Build the round loop.
2. **Day 22:** Code the player's hit/stand loop and the bust check. Then the dealer's "draw until 17" loop. Decide the winner and adjust money.
3. **Day 23:** Add a `time.sleep()` "dealing…" pause, show cards nicely, and make betting reject amounts bigger than your money.
4. **Day 24:** Comment, test edge cases (bet of 0? bust on first hit?), and present.

## 💡 Helpful snippets
Draw a card:
```python
def draw_card():
    return random.choice(card_values)
```

The dealer's auto-play loop:
```python
while dealer_total < 17:
    dealer_total = dealer_total + draw_card()
```

Deciding the winner:
```python
if player_total > 21:
    print("Bust! You lose.")
elif dealer_total > 21 or player_total > dealer_total:
    print("You win!")
    money = money + bet
elif player_total == dealer_total:
    print("Push (tie).")
else:
    print("Dealer wins.")
    money = money - bet
```

## 🌟 Stretch goals
- Make Aces count as 1 *or* 11 (whichever keeps you under 21) — this is a real challenge!
- Show cards as suits/faces (`A♠`, `K♥`) instead of just numbers.
- A "double down" option that doubles your bet for one extra card.

## 🆘 If you get stuck
- Build it in pieces: first just *draw and total* cards. Add betting last.
- The Ace-as-1-or-11 rule is genuinely tricky — it's a great stretch goal, but **don't** start there. Get the basic version working first.
- Reread **Day 13–15 (lists + random)** and **Day 19 (return values)** — `draw_card()` returning a number is the heart of this game.
