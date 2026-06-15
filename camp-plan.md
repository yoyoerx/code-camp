# "Code Catalyst" — Python Summer Program

**A 6-Week, Day-by-Day Curriculum & Planning Document for a Rising 6th Grader**

- **Target Age:** 11–12 years old (rising 6th grader)
- **Pacing:** 6 weeks · 4 days/week (e.g., Mon–Thu) · 2 hours/day
- **Total Program Hours:** ~48 hours
- **Learning Model:** *Independent, self-guided* — the student drives each day using the day's `README.md`. A mentor (parent/guardian) checks in **~15–30 minutes per day** at two fixed moments: the **Kickoff** (start) and the **Show & Tell** (end).
- **Pedagogical Strategy:** Project-driven, kinesthetic learning. Minimizes abstract syntax drilling; maximizes physical metaphors (storage boxes, backpacks, spellcasting) and immediate interactive feedback. Every day ends with something that *runs* and is fun to show off.

> **What changed in this revision (v2):** The original draft was written for a teacher leading the room. This version is rewritten for **independent learning**. Each day now has a student-facing `README.md`, a starter file with `TODO`s, graduated hints, and a full answer key. The instructor's live actions become **🧑‍🏫 Mentor Checkpoints**. Editor changed from Mu to **VS Code** (per family preference). A **Resources** library and a **"When to Get Outside Help"** guide were added.

---

## How This Repository Is Organized

```
python-summer-camp/
├── camp-plan.md            ← you are here (the master plan)
├── README.md               ← START HERE: how the student uses each day
├── SETUP.md                ← one-time computer setup (do WITH an adult)
├── RESOURCES.md            ← curated videos & websites, grouped by topic
├── MENTOR-GUIDE.md         ← the 15-min/day playbook for the check-in adult
├── certificate-of-completion.md
├── capstone-projects/      ← 3 final-project blueprints (Week 6)
├── week-1-variables-and-io/
│   ├── day-01-print/
│   │   ├── README.md       ← the day's lesson, written to the student
│   │   ├── starter.py      ← type-along examples + the build challenge (TODOs)
│   │   └── solution/       ← the full answer key (open only after trying!)
│   ├── day-02-variables/ ...
├── week-2-decisions-and-logic/ ...
├── week-3-loops/ ...
├── week-4-data-collections/ ...
├── week-5-functions/ ...
└── week-6-capstone/        ← project days (blueprint + build, no answer key)
```

**The golden rule for the student:** Open the day's folder, read `README.md` top to bottom, and do what it says. Everything you need for the day is in that one folder.

---

## The Daily 2-Hour Rhythm

To keep focus and energy across a 2-hour block, each day follows the same five beats. The student runs all of these; the mentor only joins for the ⭐ moments.

| Beat | Time | What happens |
|---|---|---|
| ⭐ **Kickoff** | 10 min | Mentor + student read the day's *Goal* together and do the **Warm-Up** puzzle. |
| **Concept Quest** | 25 min | Student reads the README's concept section + watches the linked video. Draws/says the analogy out loud. |
| **Guided Practice** | 30 min | Student types along with the examples in `starter.py` and runs them, fixing errors as they appear. |
| **Build Block** | 40 min | Student completes the `TODO`s in `starter.py` to build the day's project. Uses **Hints** if stuck. |
| ⭐ **Show & Tell** | 15 min | Student runs the finished project for the mentor and explains *what they changed*. Mentor uses the checklist. |

> **Pacing is a guide, not a law.** A great day where the student is in flow can blow past these times. A hard day might only reach the Guided Practice — that is fine. **Finishing every `TODO` is never the goal; understanding is.**

---

## One-Time Setup (Before Week 1) — Do This With an Adult

Full step-by-step instructions live in **[SETUP.md](SETUP.md)**. Summary:

1. **Install Python** (the language itself) from [python.org/downloads](https://www.python.org/downloads/). ✅ Check "Add Python to PATH" during install.
2. **Install VS Code** (the editor) from [code.visualstudio.com](https://code.visualstudio.com/).
3. **Install the Microsoft "Python" extension** inside VS Code.
4. **Open the `python-summer-camp` folder** in VS Code and confirm you can run a `print("hello")` file.
5. **Typing warm-up (optional, recommended):** 10 minutes/day at [TypingClub.com](https://www.typingclub.com/) builds keyboard comfort.

> 🧑‍🏫 **This setup is the #1 place an adult is required.** Installing Python, setting PATH, and picking the interpreter in VS Code are fiddly and frustrating for an 11-year-old alone. Budget 45–60 minutes the weekend before camp starts. See the "When to Get Outside Help" section below.

---

# Week 1 — Talking to the Computer & Storage (Variables & I/O)

**Goal:** Bridge the gap from visual block-coding to writing text code. Learn how computers store and recall basic text and numbers.

### Day 1 — `print()` (Our First Words)
- **Concept:** Programming is writing a recipe a computer follows exactly. Text must be wrapped in quotes (a *string*) so the computer doesn't think it's a command. A `SyntaxError` is a *helpful hint*, not a failure.
- **Guided Practice:** Create `day1.py`, type and run `print("Hello World!")`. Remove a quote on purpose to meet the `SyntaxError`.
- **Build Block — The Comedy Robot:** A script that introduces a robot, tells three jokes, uses blank `print()` lines for spacing, and prints ASCII art.
- **Show & Tell:** Run the comedy routine.

### Day 2 — Variables (Digital Storage Boxes)
- **Concept:** A variable is a labeled box that holds a value: `name = "Alex"`. Difference between *text* (`"10"`) and *math numbers* (`10`).
- **Guided Practice:** Make variables, print them, and combine them in one `print()` using commas.
- **Build Block — Mad Libs Generator:** Define 5–6 variables, then print a wacky paragraph that uses them. Swap values to change the whole story.
- **Show & Tell:** Change the variable values live.

### Day 3 — `input()` (Making It Conversational)
- **Concept:** `input()` pauses the program, waits for Enter, and stores what the user typed into a variable.
- **Guided Practice:** Ask for a "spy name" and greet the user with it.
- **Build Block — Interviewer Chatbot:** Ask 4–5 questions and print a unique reaction to each answer.
- **Show & Tell:** The mentor takes the interview.

### Day 4 — Numbers & Simple Math (The Calculator Brain)
- **Concept:** Operators `+ - * /`. **`input()` always returns text**, so convert with `int()` before doing math.
- **Guided Practice:** Read a number, convert with `int()`, multiply, print.
- **Build Block — Dog-to-Human Age Converter:** Ask for names and a dog's age, multiply by 7, print a personalized result.
- **Show & Tell:** Test with different numbers.

---

# Week 2 — Making Decisions (Conditionals & Logic)

**Goal:** Direct the flow of a program based on input. Give the computer a decision-making brain.

### Day 5 — Booleans & Comparisons (True vs. False)
- **Concept:** Comparison operators `>`, `<`, `==` (note the **double** equals). They always produce a Boolean: `True` or `False`.
- **Build Block — Rollercoaster Ticket Booth:** Ask for height in inches and print whether it clears the 48-inch bar (a Boolean).

### Day 6 — `if` / `else` & Indentation (Choosing Paths)
- **Concept:** `if`/`else` choose an action. **Indentation is what tells Python which code belongs to the branch.** Use the "fork in the road" picture.
- **Build Block — Secret Passcode Door:** Right password → treasure; wrong password → alarm.

### Day 7 — Complex Decisions (`elif`, `and`, `or`)
- **Concept:** `elif` for more than two choices; `and` (both true) and `or` (at least one true).
- **Build Block — Choose-Your-Own-Adventure:** A 3-step branching text game with at least 3 distinct endings.

### Day 8 — Debugging & Defensive Coding
- **Concept:** Programs break when users do unexpected things. Read a *traceback* like a detective: find the line number and the error type. Compare text safely with `.lower()`.
- **Build Block — Ultimate Trivia Challenge:** A 3-question quiz that keeps score and accepts answers in any capitalization.

---

# Week 3 — Automation & Repetition (Loops)

**Goal:** Run a block of code many times without rewriting it. This is the text version of Scratch's "Repeat" block.

### Day 9 — `while` Loops (Do It Until…)
- **Concept:** A `while` loop repeats as long as its condition is `True`. Beware **infinite loops** — escape one in the terminal with **Ctrl + C**. Always change the loop variable inside the loop.
- **Build Block — Number Guessing Game:** Secret number is hardcoded; loop until the guess matches.

### Day 10 — `for` Loops & `range()` (Counting Loops)
- **Concept:** A `for` loop repeats a *specific number of times*. `range(start, stop)`.
- **Build Block — Multiplication Table Generator:** Ask for a number, print its full times-table with a `for` loop.

### Day 11 — Loop Controls (`break` & `continue`)
- **Concept:** `break` = emergency eject from the loop; `continue` = skip the rest of this round.
- **Build Block — Master Password Vault:** 3 attempts only; `break` on success, lock out after 3 misses.

### Day 12 — Loop Challenges & Visual Fun
- **Concept:** Combine loops + conditionals. **FizzBuzz** and the modulo operator `%` (even check: `n % 2 == 0`). String multiplying: `"*" * n`.
- **Build Block — ASCII Art Generator:** Ask for a character and size; use loops to draw triangles/squares/patterns.

---

# Week 4 — Organizing Data (Lists & Collections)

**Goal:** Move from single variables to whole collections of items.

### Day 13 — Intro to Lists (Our First Digital Backpack)
- **Concept:** One list instead of many variables: `backpack = ["sword", "shield", "potion"]`. *Indexes start at 0.* `len()` counts items.
- **Build Block — RPG Inventory Manager:** Show a backpack; ask which index to inspect; print a custom description.

### Day 14 — Modifying Lists (Adding/Removing Gear)
- **Concept:** Lists are dynamic: `.append()` adds, `.remove()` / `.pop()` take away.
- **Build Block — Interactive Grocery List:** A menu app (View / Add / Delete / Exit) running in a `while` loop.

### Day 15 — Looping Through Lists (The Inventory Checker)
- **Concept:** `for item in my_list:` visits every element. Introduce `import random` and `random.choice()`.
- **Build Block — Random Sentence Generator:** Lists of adjectives/nouns/verbs combined into wacky random sentences.

### Day 16 — Dictionaries (Key–Value Matching)
- **Concept:** Look things up by name instead of by index: `{"name": "Link", "health": 100}`. Like a real dictionary: word (key) → definition (value).
- **Build Block — Pokédex / Contact Book:** Store 3 entities with key–value stats; user types a name to see its stats.

---

# Week 5 — Modular Coding (Functions)

**Goal:** Write clean, reusable code. Stop repeating yourself.

### Day 17 — Intro to Functions (Reusable Spells)
- **Concept:** `def` defines a "spell" once; call it by name anytime.
- **Build Block — Custom Banner Drawer:** 3 functions that each print a different ASCII banner; a main script that calls them to frame a scene.

### Day 18 — Parameters & Arguments (Customizing Spells)
- **Concept:** Parameters are placeholders in the parentheses that let one function behave differently each call.
- **Build Block — Shape Drawer:** `draw_line(symbol, length)` and `draw_box(symbol, height, width)`.

### Day 19 — Return Values (The Alchemist's Transmutation)
- **Concept:** Functions can *compute and hand back* a result with `return`. Raw ingredients in → baked cake out.
- **Build Block — Secret Cipher Tool:** `scramble_word(word)` swaps letters (a→@, e→3) and **returns** the secret; a second function unscrambles.

### Day 20 — Scope & Refactoring
- **Concept:** Variables made inside a function are *local* — they vanish when it ends. **Refactoring** = rewriting messy code into clean functions without changing what it does.
- **Build Block — Refactor Day:** Take an earlier game (Adventure Game or Password Vault) and reorganize it into functions.

---

# Week 6 — The Capstone Showcase

**Goal:** Combine everything — variables, math, loops, lists, dictionaries, functions — into one complete, polished, text-based program. The student **designs and builds this from scratch** (no answer key), choosing one of three blueprints in [`capstone-projects/`](capstone-projects/).

### Day 21 — Modules & Project Blueprinting
- **Concept:** External modules: `import random`, `import time` (`time.sleep()` for dramatic pauses). Choose a capstone path and **draw a flowchart on paper first.**
- **Build:** Scaffold the main menu loop and setup variables.
- **The three paths** (full design docs in `capstone-projects/`):
  - **Path A — Virtual Pet (Tamagotchi):** Keep a digital pet alive by feeding, playing, and resting; track stats in a dictionary. *(Most beginner-friendly.)*
  - **Path B — Space Cargo Trader:** Travel between planets, buy low/sell high, survive random events, reach 1,000 credits. *(Most math-heavy.)*
  - **Path C — Blackjack Casino:** Deal from a deck list, total scores, hit/stand, bet currency. *(Most algorithm-heavy.)*

### Day 22 — Core Logic Engineering
- **Concept:** Write **pseudocode comments first**, then fill in real Python under each comment.
- **Build:** Code the core loop and win/lose conditions; get a crude prototype running.

### Day 23 — Polish, Bugs & ASCII Art
- **Concept:** Make it feel finished: borders, clear messages, suspenseful `time.sleep()` pauses, and inputs that don't crash the game.
- **Build:** Add a title splash screen, instructions, and input safety.

### Day 24 — Final Showcase & Code Review
- **Concept:** What real programmers do — a **code review**. Read the code block by block; add `#` comments so others understand it.
- **Build / Celebrate:** A 5-minute presentation (what it is, hardest bug + how it was solved, what's next), a **Launch Party** where family playtests the game, and a printed **Certificate of Completion**.

---

## When to Get Outside Help (Key Support Areas)

Independent does **not** mean alone. These are the moments to pull in the daily check-in adult, a knowledgeable friend, or an online community. Each daily `README.md` repeats the relevant one as a **🧑‍🏫 Mentor Checkpoint** or **🆘 Stuck?** box.

| Where help matters most | Why | Who/where to ask |
|---|---|---|
| **Initial computer setup (pre–Week 1)** | Installing Python, PATH, and choosing the VS Code interpreter are error-prone and demoralizing to debug alone. | An adult, following `SETUP.md`. Backup: the official [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial). |
| **Day 8 — reading tracebacks** | Learning to *read* an error is a skill; the first few are best done with someone. | Mentor sits in for the Concept Quest. |
| **Day 6 — indentation errors** | `IndentationError` is the #1 beginner frustration and hard to "see." | Mentor checkpoint; VS Code's auto-indent + the "render whitespace" setting. |
| **"My code won't run and I don't know why"** | Every coder hits this. Knowing *how to ask for help* is a core skill. | First: re-read the error's line number. Then mentor. Then a trusted adult/older student. |
| **Capstone scope (Week 6)** | Kids often pick something too big. An adult helps cut scope to something finishable. | Mentor, during Day 21 blueprinting. |
| **Genuinely stuck > 15 min on a Build Block** | Productive struggle is good; spinning out is not. | Use the README's graduated **Hints**, then peek at the `solution/` file, then ask the mentor. |

> **A healthy rule:** *"Try for 15 minutes. Use the hints. If still stuck, it's not cheating to look — read the solution, understand it, then close it and retype it yourself."*

**Beyond the household**, good places for an 11-year-old (with adult awareness) to find help: a local library coding club, a parent who codes, or asking the mentor to post a question on [Stack Overflow](https://stackoverflow.com/) on the student's behalf. Avoid unsupervised chat communities.

---

## Curated Resources (Quick Reference)

The full, topic-by-topic list with specific video links lives in **[RESOURCES.md](RESOURCES.md)**. Highlights:

- **Editor & setup:** [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- **All-around beginner course (video):** [freeCodeCamp — Learn Python (Full Course)](https://www.youtube.com/watch?v=rfscVS0vtbw) — use in small clips, not all at once. Per-topic picks are pinned in [RESOURCES.md](RESOURCES.md).
- **Kid-friendly written reference:** [W3Schools Python](https://www.w3schools.com/python/) and the official [Python Tutorial](https://docs.python.org/3/tutorial/).
- **Practice problems:** [CodingBat Python](https://codingbat.com/python) (great for functions in Week 5).
- **Typing:** [TypingClub](https://www.typingclub.com/).

---

## Mentor Quick-Start

The check-in adult does **not** need to know Python. Their job is encouragement, accountability, and the two daily ⭐ moments. The 15-minute-a-day playbook — including "what to say when they're stuck" and the Show & Tell question checklist — is in **[MENTOR-GUIDE.md](MENTOR-GUIDE.md)**.

---

## Glossary (Kid-Friendly)

- **String** — text wrapped in quotes, like `"hello"`.
- **Variable** — a labeled box that stores a value.
- **Boolean** — a value that is either `True` or `False`.
- **Loop** — code that repeats.
- **List** — an ordered collection of items in one variable.
- **Dictionary** — a collection that looks values up by name (key).
- **Function** — a reusable, named block of code (a "spell").
- **Argument / Parameter** — the extra info you hand a function.
- **Return** — the answer a function hands back.
- **Traceback** — the red error message Python prints when something breaks (it tells you the line and the problem).
- **Refactor** — clean up code without changing what it does.
