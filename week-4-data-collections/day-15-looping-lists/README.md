# Day 15 — Looping Through Lists (The Inventory Checker)

> Week 4 · Day 15 of 24 · *Lists & Collections*

## 🎯 Today's Goal
Visit **every item** in a list automatically with a `for` loop, and add randomness with the `random` module.

## 🧩 Warm-Up (with your mentor)
Roll a die a few times (or pick a random card). The computer can do that too — and today you'll teach it to make random choices, which is the secret behind almost every game.

## 🧠 Concept Quest
You already used `for` with `range()`. You can also loop **directly over a list** — it hands you each item one at a time:

```python
party_members = ["Alex", "Zelda", "Mario"]
for hero in party_members:
    print(hero + " is ready for battle!")
```

`hero` becomes each item in turn: first "Alex", then "Zelda", then "Mario". No index numbers needed!

**The `random` module** lets Python make random choices. First you **import** it (load the tool), then use it:

```python
import random
colors = ["red", "blue", "green"]
print(random.choice(colors))     # picks one at random each run!
print(random.randint(1, 6))      # a random number 1-6 (like a die)
```

> 🔑 `import random` goes at the **very top** of your file. You only import once, then you can use `random.choice()` and `random.randint()` as many times as you like.

**📺 Watch/read:** [W3Schools: For Loops](https://www.w3schools.com/python/python_for_loops.asp) · [W3Schools: Random Module](https://www.w3schools.com/python/module_random.asp).

## ⌨️ Guided Practice — type along
Type the party-members loop and the random examples. **Run the random one several times** — different output each time!

## 🛠️ Build Block — Random Sentence Generator 🎲
Make a machine that builds silly random sentences.

- [ ] `import random` at the top
- [ ] Make 3 lists: `adjectives`, `nouns`, `verbs` (3+ words each)
- [ ] Use `random.choice()` to pick one from each
- [ ] Combine them into a wacky sentence and print it
- [ ] Use a loop to print **5** random sentences

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I pick a random word?</summary>

```python
word = random.choice(adjectives)
```
</details>

<details><summary>Hint 2 — How do I print 5 sentences?</summary>

Wrap the sentence-making in a `for` loop that runs 5 times:
```python
for i in range(5):
    # pick words and print a sentence
```
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
import random
adjectives = ["sparkly", "gigantic", "bubbly"]
nouns = ["potato", "unicorn", "wizard"]
verbs = ["dances", "floats", "giggles"]

for i in range(5):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    print("The", adj, noun, verb, "happily!")
```
Full version: `solution/sentence_generator.py`.
</details>

## ⭐ Show & Tell
Run it a few times so your mentor sees the sentences change every time. Which random combo is the funniest?

## 🧑‍🏫 Mentor note
`random` is a big "wow" moment — and it powers all three capstone projects. If they loved this, that's a great sign for Week 6. Tomorrow: dictionaries, the last new collection.
