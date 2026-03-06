import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    return 1, 100  # Default for Normal and Hard

def parse_guess(raw: str):
    """Parse user input into an int guess."""
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            return False, None, "Please enter a whole number (no decimals)."
        guess = int(raw)
        return True, guess, None
    except ValueError:
        return False, None, "Invalid input. Please enter a number."

def check_guess(guess: int, secret: int):
    """Compare guess to secret and return (outcome, message)."""
    try:
        guess_int = int(guess)
        secret_int = int(secret)
        
        if guess_int == secret_int:
            return "Win", "✅ Correct!"
        elif guess_int > secret_int:
            return "Too High", "⬇️ Go LOWER!"
        else:
            return "Too Low", "⬆️ Go HIGHER!"
    except (ValueError, TypeError):
        return "Error", "Error comparing guess. Secret or guess is not a valid number."

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Award points: 100 - 10 points per attempt, minimum 10
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
    
    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5
    
    if outcome == "Too Low":
        return current_score - 5
    
    return current_score