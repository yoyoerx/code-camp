# Day 13 — Intro to Lists (Our First Digital Backpack)

> Week 4 · Day 13 of 24 · *Lists & Collections*

## 🎯 Today's Goal
Store **many** items in one variable using a **list**, and grab items by their position (index).

## 🧩 Warm-Up (with your mentor)
Empty a backpack or pencil case and lay the items in a row. Point to the **first** item — in programming that's position **0**, not 1! Count along the row: 0, 1, 2, 3… Get used to starting at zero.

## 🧠 Concept Quest
Instead of `item1`, `item2`, `item3` as separate variables, a **list** holds them all together in order:

```python
backpack = ["sword", "shield", "potion"]
```

You grab one item by its **index** (its position number) in square brackets. **Indexes start at 0:**

```python
print(backpack[0])   # sword  (the FIRST item)
print(backpack[1])   # shield
print(backpack[2])   # potion
```

Count how many items with **`len()`**:

```python
print(len(backpack))   # 3
```

> 🔑 Why start at 0? It's just how almost all programming languages count. The first item is index 0, so the *last* item of a 3-item list is index 2 (one less than the length). Asking for `backpack[3]` here gives an `IndexError` — there's no slot 3.

**📺 Watch/read:** [W3Schools: Lists](https://www.w3schools.com/python/python_lists.asp) · Video: [Kylie Ying — Lists, Tuples, Sets, Dictionaries (Lesson 4)](https://www.youtube.com/watch?v=RF26NjCUNvs) (watch the lists part now; dictionaries are for Day 16). Curious *why* we count from 0? [Sequences: Indexing (Lesson 3)](https://www.youtube.com/watch?v=gGukPkjBDdo).

## ⌨️ Guided Practice — type along
Type the inventory example. Print items by index, print the length, and try asking for an index that's too big to meet the `IndexError`.

## 🛠️ Build Block — RPG Inventory Manager 🎒
Show a player their backpack and let them inspect a slot.

- [ ] Make a list of 4–5 inventory items
- [ ] Print how many items they have using `len()`
- [ ] Ask which **slot number** (index) they want to inspect (convert with `int()`)
- [ ] Print a custom description for the item at that index

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I show the item they picked?</summary>

Use their number as the index:
```python
slot = int(input("Which slot? "))
print("You are holding:", inventory[slot])
```
</details>

<details><summary>Hint 2 — How do I count the items?</summary>

```python
print("You have", len(inventory), "items.")
```
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
inventory = ["torch", "compass", "gold coin", "map", "rope"]
print("You have", len(inventory), "items (slots 0 to 4).")
slot = int(input("Inspect which slot? "))
print("Slot", slot, "holds a", inventory[slot] + "!")
```
Full version: `solution/inventory_manager.py`.
</details>

## ⭐ Show & Tell
Inspect a few slots for your mentor. Then ask for a slot that doesn't exist (like 9) to show the `IndexError` — explain why it happened.

## 🧑‍🏫 Mentor note
"Start at 0" is genuinely counterintuitive — expect off-by-one confusion (asking for slot 1 to get the first item). It clicks with practice. Tomorrow they learn to *change* lists.
