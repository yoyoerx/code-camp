# Day 16 — Dictionaries (Key–Value Matching)

> Week 4 · Day 16 of 24 · *Lists & Collections*

## 🎯 Today's Goal
Store information you can look up **by name** instead of by position, using a **dictionary**.

## 🧩 Warm-Up (with your mentor)
Look up a word in a real dictionary (or just think about it): you find the **word** (the *key*) to get its **definition** (the *value*). Python dictionaries work the exact same way.

## 🧠 Concept Quest
A **list** uses number positions. A **dictionary** uses *names* (called **keys**) to look up *values*. You write it with curly braces and `key: value` pairs:

```python
hero_stats = {"name": "Link", "health": 100, "defense": 15}
```

Look something up by its key (in square brackets):

```python
print(hero_stats["name"])      # Link
print(hero_stats["health"])    # 100
```

Change or add values:

```python
hero_stats["health"] = 90      # change an existing value
hero_stats["level"] = 5        # add a brand-new key
print(hero_stats)
```

> 🔑 **List vs Dictionary:** use a **list** for an ordered collection of similar things (`["sword","shield"]`). Use a **dictionary** when each piece of data has a *name* (`health`, `name`, `defense`). They team up great — a list *of* dictionaries is how real games store characters!

**📺 Watch/read:** [W3Schools: Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) · Video: [Kylie Ying — Lists, Tuples, Sets, Dictionaries (Lesson 4)](https://www.youtube.com/watch?v=RF26NjCUNvs) (the dictionaries half).

## ⌨️ Guided Practice — type along
Type the `hero_stats` example. Look up keys, change `health`, add a `level`, and print the whole dictionary.

## 🛠️ Build Block — Pokédex / Contact Book 📒
Build a mini database the user can search by name.

- [ ] Create **3** entries (Pokémon, heroes, or contacts). Each entry is a dictionary with keys like `name`, `type`, `power`
- [ ] Ask the user to type a name to look up
- [ ] If you find it, print its stats nicely; if not, say "not found"

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How should I store 3 creatures?</summary>

A dictionary where each key is a creature's name and each value is *another* dictionary of its stats:
```python
pokedex = {
    "pikachu": {"type": "Electric", "power": 55},
    "charmander": {"type": "Fire", "power": 52},
    "bulbasaur": {"type": "Grass", "power": 49},
}
```
</details>

<details><summary>Hint 2 — How do I check if their search exists?</summary>

Use `in` to check before looking up (avoids a crash):
```python
search = input("Search: ").lower()
if search in pokedex:
    print(pokedex[search])
else:
    print("Not found!")
```
</details>

<details><summary>Hint 3 — How do I print the stats nicely?</summary>

```python
creature = pokedex[search]
print("Type:", creature["type"])
print("Power:", creature["power"])
```
Full version: `solution/pokedex.py`.
</details>

## ⭐ Show & Tell
Let your mentor search your database — including a name that *isn't* in it, to show your "not found" message works (defensive coding!).

## 🧑‍🏫 Mentor note
A **dictionary inside a dictionary** is a real step up — totally optional. A flat single dictionary is a perfectly good Day-16 win. This concept is the backbone of the Virtual Pet capstone, so it's worth time. Week 4 done — functions next!
