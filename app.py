import streamlit as st
import random
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.title("🎮 Game Glitch Investigator")

# Sidebar settings
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"])
low, high = get_range_for_difficulty(difficulty)

# Initialize Session State
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.history = []
    st.session_state.status = "playing"

# UI Logic
st.write(f"Guess a number between {low} and {high}.")
raw_guess = st.text_input("Enter your guess:")
submit = st.button("Submit Guess 🚀")
new_game = st.button("New Game 🔁")

# FIX 2: Handle New Game Reset
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.history = []
    st.session_state.status = "playing"
    st.success("New game started!")
    st.rerun()

if submit and st.session_state.status == "playing":
    # Use logic_utils to parse
    ok, guess_int, err = parse_guess(raw_guess)
    
    if not ok:
        # FIX 3: Invalid inputs no longer increase attempts
        st.error(err)
    else:
        # Valid guess: update state
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)
        
        # Check guess
        outcome, message = check_guess(guess_int, st.session_state.secret)
        st.session_state.score = update_score(st.session_state.score, outcome, st.session_state.attempts)
        
        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
            st.success(message)
        else:
            st.info(message)

# Display Stats
st.write(f"**Score:** {st.session_state.score} | **Attempts:** {st.session_state.attempts}")
st.write(f"**History:** {st.session_state.history}")