# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Description
The game is a number-guessing app where players try to guess a randomly generated secret number within a certain range based on their chosen difficulty level. The app tracks user history, scores, and provides higher/lower hints to guide the player toward the correct number.

### Bugs Found & Fixes Applied
* **Inverted / Broken Hints:** The original code string-cast the secret integer on even turns, forcing broken alphabetic comparisons and completely inverting the higher/lower directions. I fixed this by removing the type-mutation and enforcing accurate integer tracking.
* **Stale UI History List:** The debug logs were rendering before the guess submission block processed state changes, causing history to lag one turn behind. I rearranged the layout flow so state processing happens prior to UI rendering.
* **Soft-Lock New Game State:** Clicking "New Game" reset the user's attempts but failed to switch the game status back to "playing", leaving the UI frozen. I updated the reset routine to restore the active status and clear previous logs cleanly.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Configure Parameters:** Select a difficulty level (Easy, Normal, or Hard) in the sidebar to dynamically generate an allowed range and attempt counter.
2. **Submit a Guess:** Type an integer into the guess box and click "Submit Guess". The value immediately registers in your game log.
3. **Observe Feedback:** The live history log updates instantly without lag, your attempts remaining decrements, and an accurate high/low direction arrow displays.
4. **Trigger Game Over / Victory:** Reaching the solution prompts a balloon animation and victory card. Exhausting your turns cleanly freezes submissions and shows the actual answer.
5. **Reset Play Field:** Click "New Game" to completely wipe the history logs, regenerate a new target inside your current difficulty boundaries, and start fresh.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
=============== test session starts ================
platform win32 -- Python 3.14.5, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\Users\neera\Documents\CIS4301
plugins: anyio-4.14.0
collected 3 items                                    

tests\test_game_logic.py ...                   [100%]

================= 3 passed in 0.10s =================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
