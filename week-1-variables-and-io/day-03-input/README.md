# Day 3 — `input()` (Making It Conversational)

> Week 1 · Day 3 of 24 · *Variables & Input/Output*

## 🎯 Today's Goal
Make your program **two-way**: ask the user a question and remember their answer.

## 🧩 Warm-Up (with your mentor)
Play 20 Questions for 2 minutes. Notice how each *answer* changes your next *question*. Programs do the same thing — they take input and react to it. Today you give your program ears.

## 🧠 Concept Quest
So far your programs only *talk*. The `input()` command lets them *listen*. When Python hits `input()`, it **pauses**, waits for the user to type and press **Enter**, and hands back whatever they typed:

```python
codename = input("What is your spy name? ")
print("Welcome, Agent " + codename + "!")
```

- The text inside `input("...")` is the **prompt** (the question shown to the user).
- Whatever they type gets **stored** in the variable (`codename` here).
- Notice the `+` signs: that's **string joining** (gluing text together). When you glue strings with `+`, *you* have to add spaces inside the quotes, like `"Agent "`.

> 🔑 Remember: `input()` always gives you back **text**, even if they type numbers. (That matters tomorrow!)

**📺 Watch/read:** [W3Schools: User Input](https://www.w3schools.com/python/python_user_input.asp).

## ⌨️ Guided Practice — type along
Type the GUIDED PRACTICE lines in `starter.py`. Run it, then **click inside the Terminal**, type your answer, and press Enter.

## 🛠️ Build Block — Interviewer Chatbot 🎤
Build a chatbot that interviews the user with **4–5 questions** and reacts to each answer.

- [ ] Ask their name, then greet them by it
- [ ] Ask at least 3 more questions (favorite food, dream superpower, favorite animal…)
- [ ] After **each** answer, print a unique, personalized reaction that uses what they typed
- [ ] End with a friendly sign-off

## 🆘 Stuck? Hints (open one at a time)
<details><summary>Hint 1 — How do I use their answer in a reaction?</summary>

Store it in a variable, then use that variable:
```python
food = input("What's your favorite food? ")
print("Ooh, I love", food, "too!")
```
</details>

<details><summary>Hint 2 — Commas vs. plus signs?</summary>

Both work to combine text. Commas auto-add spaces; `+` does not (you add your own). Commas are easier — start with those:
```python
print("Whoa,", name, "is a great name!")
```
</details>

<details><summary>Hint 3 — Show me the pattern to repeat</summary>

```python
name = input("What is your name? ")
print("Nice to meet you,", name + "!")

food = input("Favorite food? ")
print("Yum,", food, "is the best.")
```
Keep going for 2-3 more. Full version: `solution/interviewer_chatbot.py`.
</details>

## ⭐ Show & Tell
Have your **mentor take the interview** while you run it. Their answers should appear in the chatbot's reactions!

## 🧑‍🏫 Mentor note
If typing in the program "does nothing," they probably need to click *inside the Terminal panel* first, then type. Common and harmless.
