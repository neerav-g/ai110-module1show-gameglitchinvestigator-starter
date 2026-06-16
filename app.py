import random
import streamlit as st
import logic_utils as lu

st.set_page_config(page_title="Glitchy Guesser Fixed", page_icon="🎮")

st.title("🎮 Game Glitch Investigator (Patched)")
st.caption("The AI glitches have been resolved.")

# 1. Sidebar Configuration
st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)

attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
attempt_limit = attempt_limit_map[difficulty]
low, high = lu.get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# 2. Session State Initialization
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "status" not in st.session_state:
    st.session_state.status = "playing"
if "history" not in st.session_state:
    st.session_state.history = []
if "last_feedback" not in st.session_state:
    st.session_state.last_feedback = ""

# 3. Handle Game Logic processing FIRST before rendering UI lists
raw_guess = st.text_input("Enter your guess:", key=f"guess_input_{difficulty}")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀", disabled=(st.session_state.status != "playing"))
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# Fix New Game Action
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high) # Uses correct range now
    st.session_state.status = "playing"                # Reset status!
    st.session_state.history = []                       # Wipe out history
    st.session_state.last_feedback = ""
    st.success("New game started.")
    st.rerun()

# Process Submission
if submit and raw_guess:
    ok, guess_int, err = lu.parse_guess(raw_guess)

    if not ok:
        st.error(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)
        
        outcome, message = lu.check_guess(guess_int, st.session_state.secret)
        st.session_state.last_feedback = message

        st.session_state.score = lu.update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"

# 4. Render Game Status & Context Blocks AFTER state mutations occur
st.subheader("Game Dashboard")
st.info(f"Guess a number between {low} and {high}. Attempts left: {attempt_limit - st.session_state.attempts}")

if show_hint and st.session_state.last_feedback:
    st.warning(st.session_state.last_feedback)

if st.session_state.status == "won":
    st.success(f"You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
elif st.session_state.status == "lost":
    st.error(f"Out of attempts! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")

with st.expander("Developer Debug Info (Now Live!)"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts Used:", st.session_state.attempts)
    st.write("Current Score:", st.session_state.score)
    st.write("History:", st.session_state.history) # Updates instantly now!

st.divider()