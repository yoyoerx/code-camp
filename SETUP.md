# 🛠️ One-Time Computer Setup (Do This With an Adult)

> 🧑‍🏫 **Grown-ups: this is the single most important place to help.** Installing Python and configuring VS Code is fiddly, and a wrong step here causes confusing errors all week. Plan to sit down together for **45–60 minutes** the weekend before Week 1. You do **not** need to know how to code — just follow these steps carefully. This guide is for **Windows 11**.

When you finish every step, the student should be able to open a file, click ▶ Run, and see text appear. That's the goal.

---

## Step 1 — Install Python (the language)

1. Go to **[python.org/downloads](https://www.python.org/downloads/)**.
2. Click the big yellow **"Download Python 3.x"** button.
3. Open the downloaded installer.
4. **⚠️ VERY IMPORTANT:** On the first screen, check the box at the bottom that says **"Add python.exe to PATH"** before clicking Install. This one checkbox prevents most setup headaches.
5. Click **"Install Now"** and wait. Click **Close** when done.

**Verify it worked:** Open the Start menu, type `PowerShell`, open it, and type:

```powershell
python --version
```

You should see something like `Python 3.12.4`. If you see an error or a Microsoft Store window opens instead, the PATH box probably wasn't checked — re-run the installer and choose **Modify**, or see Troubleshooting below.

---

## Step 2 — Install VS Code (the editor)

1. Go to **[code.visualstudio.com](https://code.visualstudio.com/)**.
2. Click **"Download for Windows"**.
3. Run the installer. Accept the agreement, keep clicking **Next**.
4. On the "Select Additional Tasks" screen, it's helpful to check **"Add 'Open with Code' action"** boxes. Then **Install**.

---

## Step 3 — Install the Python extension inside VS Code

1. Open **VS Code**.
2. On the left edge, click the **Extensions** icon (it looks like four squares 🧩).
3. In the search box type **`Python`**.
4. Install the one published by **Microsoft** (it has a blue check and millions of downloads). Click **Install**.

---

## Step 4 — Open the camp folder

1. In VS Code, click **File → Open Folder…**
2. Navigate to and select the **`python-summer-camp`** folder.
3. Click **Select Folder**. You should now see all the week folders on the left.

> 💡 Always open the **whole `python-summer-camp` folder**, not a single file. This keeps the Terminal pointed at the right place.

---

## Step 5 — The "Hello, it works!" test

1. In the left file list, open `week-1-variables-and-io/day-01-print/starter.py`.
2. Look at the **top-right** of the window for a **▶ (Run) triangle**. Click it → choose **"Run Python File"**.
3. A **Terminal** panel opens at the bottom and shows the program's output.

If you see text appear with no red errors — **you're done! 🎉** The student is ready for Day 1.

If VS Code asks you to **"Select Interpreter"**, click that message and pick the Python 3.x version you installed. (You can also press `Ctrl+Shift+P`, type `Python: Select Interpreter`, and choose it.)

---

## 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| `python` opens the Microsoft Store | The PATH box wasn't checked. Re-run the python.org installer → **Modify** → ensure "Add to PATH" / `py launcher` is on. Restart VS Code. |
| "Python is not installed" in VS Code | Run **Python: Select Interpreter** (`Ctrl+Shift+P`) and pick your Python 3.x. |
| Run button is missing | Make sure the Microsoft **Python extension** (Step 3) is installed and the file ends in `.py`. |
| Terminal shows red errors when running | That's often a code error, not a setup error — read the line number it names. For setup, confirm `python --version` works in PowerShell. |
| Typing in the program does nothing | Click **inside the Terminal panel** first, then type and press Enter. |

Official backup guide (very good, with pictures): **[VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)**.

---

## Step 6 — How to READ the lessons (important!)

Every lesson is a `README.md` file. If you just open one, you'll see the raw text with `#` and `*` symbols everywhere — readable, but not pretty, and the **hint drop-downs won't open.** Use VS Code's built-in **Markdown Preview** instead (no extension needed):

1. Click a `README.md` file to open it.
2. Press **`Ctrl + Shift + V`** → it opens a clean, formatted **Preview** in a new tab. ✨

**Best setup for camp** — lesson on one side, code on the other:
1. Open the day's `README.md`, then press **`Ctrl + K`** and let go, then press **`V`**. This opens the preview **side-by-side** (lesson on the right, file on the left).
2. Open that day's `starter.py` on the left side and code while you read. 📖➡️⌨️

In Preview mode the tables, emojis, and the **▸ click-to-open hint boxes** all work. (The little `[ ]` checkboxes show up too — you can't click those in preview, but you *can* edit and check them off in the main `README.md` text view if you like.)

> 💡 Built-in Preview is all you need. If you ever want more (like clickable checkboxes), the free **"Markdown All in One"** extension adds them — but it's totally optional.

---

## Optional but recommended

- **Typing practice:** [TypingClub.com](https://www.typingclub.com/) — 10 minutes/day makes coding much less frustrating.
- **A comfy color theme:** `Ctrl+K Ctrl+T` in VS Code to pick light or dark mode.
- **Bigger font:** `Ctrl + =` zooms the editor in for easier reading.
