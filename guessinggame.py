import streamlit as st

# Function to run binary search for number guessing
def binary_search_game(low, high):
    # The app's binary search logic for guessing the number
    if low > high:
        return None  # This should not happen in a well-defined game
    
    guess = (low + high) // 2
    return guess

# Streamlit app
def main():
    # App title and instructions
    st.title('Binary Search Number Guessing Game')
    st.write("""
    Welcome to the Number Guessing Game!
    In this game, I'll guess the number you're thinking of using a binary search algorithm.
    I'll ask you if my guess is too high, too low, or correct.
    Let's get started!
    """)

    # Session state initialization
    if 'low' not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.guess = None
        st.session_state.attempts = 0

    # Display current state and guess
    st.write(f"**Range:** {st.session_state.low} to {st.session_state.high}")
    
    # Make a guess using binary search
    st.session_state.guess = binary_search_game(st.session_state.low, st.session_state.high)

    if st.session_state.guess is not None:
        st.write(f"My guess is: **{st.session_state.guess}**")
        st.session_state.attempts += 1

    # User feedback
    feedback = st.radio(
        "Is my guess too high, too low, or correct?",
        ('Too High', 'Too Low', 'Correct')
    )

    # Update the guess range based on user feedback
    if feedback == 'Too High':
        st.session_state.high = st.session_state.guess - 1
    elif feedback == 'Too Low':
        st.session_state.low = st.session_state.guess + 1
    elif feedback == 'Correct':
        st.success(f"Yay! I guessed the correct number {st.session_state.guess} in {st.session_state.attempts} attempts!")
   
 



if __name__ == '__main__':
    main()
