# Day 14 — Modifying Lists (Adding/Removing Gear)

> Week 4 · Day 14 of 24 · *Lists & Collections*

## 🎯 Today's Goal
Change a list while the program runs — **add** items, **remove** items — and build your first menu app.

## 🧩 Warm-Up (with your mentor)
Back to the backpack: add an item ("pick up a snack") and remove one ("drop the rock"). Lists in Python change the same way while your program runs.

## 🧠 Concept Quest
Lists are **dynamic** — they can grow and shrink. The most useful **methods** (commands attached to the list with a dot):

```python
hobbies = ["gaming", "reading"]
hobbies.append("swimming")     # add to the END
print(hobbies)                 # ['gaming', 'reading', 'swimming']

hobbies.remove("reading")      # remove by VALUE (the word)
print(hobbies)                 # ['gaming', 'swimming']

hobbies.pop(0)                 # remove by INDEX (position 0)
print(hobbies)                 # ['swimming']
```

- `.append(x)` → adds `x` to the end
- `.remove("word")` → finds and removes that exact item (errors if it's not there)
- `.pop(i)` → removes the item at index `i`

> 🔑 `.remove()` needs the *value* ("reading"); `.pop()` needs the *position* (0). Pick whichever you know.

**📺 Watch/read:** [W3Schools: List Methods](https://www.w3schools.com/python/python_lists_methods.asp).

## ⌨️ Guided Practice — type along
Type the append/remove/pop examples. Print the list after each change so you can watch it transform.

## 🛠️ Build Block — Interactive Grocery List 🛒
A menu app that runs until the user quits, letting them manage a list.

- [ ] Start with a grocery list (can be empty or have a few items)
- [ ] Use a `while True:` loop showing a menu: `1) View  2) Add  3) Remove  4) Quit`
- [ ] **View** prints the current list
- [ ] **Add** asks for an item and `.append()`s it
- [ ] **Remove** asks for an item and `.remove()`s it
- [ ] **Quit** uses `break` to end

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I keep showing the menu?</summary>

Wrap it in `while True:` and ask for a choice each time:
```python
while True:
    print("1) View  2) Add  3) Remove  4) Quit")
    choice = input("Pick: ")
```
</details>

<details><summary>Hint 2 — How do I handle each choice?</summary>

Use `if`/`elif` on the choice:
```python
if choice == "1":
    print(groceries)
elif choice == "2":
    item = input("Add what? ")
    groceries.append(item)
```
</details>

<details><summary>Hint 3 — How do I quit safely?</summary>

```python
elif choice == "4":
    print("Bye!")
    break
```
Full version: `solution/grocery_list.py`.
</details>

## ⭐ Show & Tell
Add 5 items, remove 2, view the list, then quit — all without re-running the program. That "stays open and reacts" feeling is what real apps do!

## 🧑‍🏫 Mentor note
A common crash: `.remove()` an item that isn't in the list → `ValueError`. The solution shows a friendly `if item in groceries:` guard — a nice "defensive coding" callback to Day 8.
