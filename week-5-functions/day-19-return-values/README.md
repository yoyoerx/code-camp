# Day 19 — Return Values (The Alchemist's Transmutation)

> Week 5 · Day 19 of 24 · *Functions*

## 🎯 Today's Goal
Make functions **compute an answer and hand it back** with `return`.

## 🧩 Warm-Up (with your mentor)
Put raw ingredients in an oven → get a cake back out. The oven *returns* a cake. So far your functions only *printed*; today they'll *give something back* you can use.

## 🧠 Concept Quest
**`print()` shows something on screen. `return` hands a value back to your code** so you can store it, do more math, or use it later. Big difference!

```python
def add_tax(price):
    total = price * 1.05
    return total            # hand the answer back

final_cost = add_tax(100)   # catch the returned value in a variable
print("Total with tax:", final_cost)   # 105.0
```

- `return total` sends `total` back to wherever the function was called.
- `final_cost = add_tax(100)` *catches* that returned value.

> 🔑 `print` vs `return`: a function that only `print`s shows you something but gives nothing back to use — `x = print("hi")` makes `x` empty (`None`). A function that `return`s gives you a value you can keep working with. For building tools, you usually want `return`.

**📺 Watch/read:** [W3Schools: Function Return Values](https://www.w3schools.com/python/python_functions.asp) · [CodingBat practice](https://codingbat.com/python) (these problems all use `return`).

## ⌨️ Guided Practice — type along
Type `add_tax`, catch its result in a variable, and print it. Then try printing `add_tax(100)` directly too — both work, but the variable version lets you reuse the answer.

## 🛠️ Build Block — Secret Cipher Tool 🔐
Build a tool that scrambles messages into "leet speak" and can unscramble them.

- [ ] Write `scramble_word(word)` that swaps some letters (a→@, e→3, o→0, etc.) and **returns** the scrambled string
- [ ] Ask the user for a message, scramble it, and print the secret
- [ ] Bonus: write `unscramble_word(secret)` that reverses the swaps and returns the original

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I swap letters in a word?</summary>

The string method `.replace(old, new)` returns a new string with swaps made:
```python
secret = word.replace("a", "@")
secret = secret.replace("e", "3")
```
</details>

<details><summary>Hint 2 — How do I return the result?</summary>

Build the scrambled string, then return it:
```python
def scramble_word(word):
    s = word.replace("a", "@").replace("e", "3").replace("o", "0")
    return s
```
(You can chain `.replace()` calls one after another.)
</details>

<details><summary>Hint 3 — Show me the shape</summary>

```python
def scramble_word(word):
    s = word.replace("a", "@").replace("e", "3").replace("o", "0").replace("i", "1")
    return s

message = input("Enter a secret message: ")
print("Encoded:", scramble_word(message))
```
Full version: `solution/cipher_tool.py`.
</details>

## ⭐ Show & Tell
Encode a secret message for your mentor and have them try to read it. Then unscramble it to reveal the original!

## 🧑‍🏫 Mentor note
The `print` vs `return` distinction is subtle but important — it's the difference between "shows me" and "gives me something to use." If their scramble "doesn't work," check they're *returning* the new string, not the original. Tomorrow: cleaning up code with functions.
