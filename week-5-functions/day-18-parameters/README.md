# Day 18 — Parameters & Arguments (Customizing Spells)

> Week 5 · Day 18 of 24 · *Functions*

## 🎯 Today's Goal
Make one function do different things each time by feeding it **parameters**.

## 🧩 Warm-Up (with your mentor)
A waffle iron always makes a waffle — but you can pour in *different batter* (chocolate, plain) for a different result. Parameters are the batter you pour into a function.

## 🧠 Concept Quest
Yesterday's functions did the exact same thing every call. **Parameters** are placeholder variables in the parentheses that let you customize each call:

```python
def greet_user(username, time_of_day):
    print("Good " + time_of_day + ", Agent " + username + "!")

greet_user("Alex", "morning")    # Good morning, Agent Alex!
greet_user("Zelda", "night")     # Good night, Agent Zelda!
```

Vocabulary (don't stress the names, but here they are):
- **Parameter** = the placeholder in the definition (`username`, `time_of_day`).
- **Argument** = the real value you pass when calling (`"Alex"`, `"morning"`).

> 🔑 Order matters! The first argument fills the first parameter, the second fills the second. `greet_user("morning", "Alex")` would greet "Agent morning" — funny, but wrong.

**📺 Watch/read:** [W3Schools: Function Arguments](https://www.w3schools.com/python/python_functions.asp).

## ⌨️ Guided Practice — type along
Type `greet_user` and call it with a few different name/time combos. See how one function gives many different outputs.

## 🛠️ Build Block — Shape Drawer 📐
Build flexible drawing functions that take parameters.

- [ ] Write `draw_line(symbol, length)` that prints `symbol` repeated `length` times (remember `"*" * 5` from Day 12!)
- [ ] Write `draw_box(symbol, height, width)` that uses loops to draw a filled box of that size
- [ ] Call each function a few times with different symbols and sizes

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How does draw_line work?</summary>

```python
def draw_line(symbol, length):
    print(symbol * length)

draw_line("*", 10)    # **********
```
</details>

<details><summary>Hint 2 — How do I draw a box?</summary>

A box is just `height` rows, each `width` symbols wide:
```python
def draw_box(symbol, height, width):
    for row in range(height):
        print(symbol * width)
```
</details>

<details><summary>Hint 3 — Show me both, with calls</summary>

```python
def draw_line(symbol, length):
    print(symbol * length)

def draw_box(symbol, height, width):
    for row in range(height):
        print(symbol * width)

draw_line("=", 20)
draw_box("#", 3, 8)
draw_box("@", 5, 5)
```
Full version: `solution/shape_drawer.py`.
</details>

## ⭐ Show & Tell
Draw boxes of different characters and sizes for your mentor — all from the *same two functions*. That's the power of parameters!

## 🧑‍🏫 Mentor note
If a box comes out the wrong shape, check argument order (height vs width). It's a perfect, low-stakes example of "order matters." Tomorrow functions get even more powerful with `return`.
