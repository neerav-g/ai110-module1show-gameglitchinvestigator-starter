# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time the game ran, it looked like a standard Streamlit setup, but basic interactions caused chaotic behaviors. The game threw counter-intuitive hints because of hidden string-type evaluations inside the guess comparisons. 
- List at least two concrete bugs you noticed at the start  
  the hints were backwards.
  trying to see your historical tracker proved useless because items registered an entire turn late. 
  using the "New Game" mechanism permanently locked the app into an unplayable state if you had previously lost a game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 5     | go higher         | go lower        | none    |
| 79    | history list should update immediately          |  history list is updating after the next input with the previous input      | none|
| 69| go lower | i had lost previous game, and started new but hint not updating past game over | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Gemini
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Gemini correctly identified that Streamlit scripts execute from top to bottom every time a widget updates. It suggested processing user submissions before rendering the tracking blocks to make history updates instant, which perfectly resolved the stale UI bug.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
In a previous implementation loop, an AI suggestion tried to clean up the type comparison issue in check_guess by suggesting str(guess) == str(secret) globally. I verified this was a poor fix because alphabetic string checking causes errors like "100" being evaluated as smaller than "2"
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I determined bugs were resolved by pairing structural inspection of the session state data with manual gameplay simulations across all three difficulty states.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I tested the "Hard" difficulty setup manually. By inspecting the Developer Expander tool, I checked that the secret integer fell strictly inside the 1 to 50 scope. I input a high value like 45 against a secret of 20, confirming it properly threw a "Go LOWER!" warning on both even and odd attempts.
- Did AI help you design or understand any tests? How?
he AI helped by detailing how code logic isolated within pure functions in logic_utils.py interacts with testing frameworks like pytest. It made it easy to see how eliminating Streamlit mutations from pure logic simplifies unit testing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit code acts like a flipbook that redraws itself from the very first line down to the last whenever you interact with an input, dropdown, or button on the screen. Because variables normally wipe clean and start over during these redraws, st.session_state acts like a small, long-term memory vault for your app. It stores records like scores and historical user values safely behind the scenes so they don't get erased during those top-to-bottom script refreshes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to consistently apply the strategy of separating functional logic (like computational updates and math checking) from UI presentation scripts. It makes the codebase significantly easier to debug and test
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will avoid assuming that an AI's code handles edge cases or types smoothly. I will explicitly request strict type hinting and inspect how values are mutated through data streams right out of the gate.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated scripts can easily look flawless and clean on the outside while harboring messy architecture and logical fallacies internally. It reinforced that code reviews and structural testing are essential requirements, no matter who wrote the code.
