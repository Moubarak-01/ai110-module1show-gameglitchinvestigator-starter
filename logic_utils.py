def get_range_for_difficulty(difficulty: str):
        """Return (low, high) inclusive range for a given difficulty."""
        if difficulty == "Easy":
            return 1, 20
        if difficulty == "Normal":
            return 1, 100
        if difficulty == "Hard": # Kept 1-100 as per original
            return 1, 100
        return 1, 100 # Default
    
    def parse_guess(raw: str):
        """Parse user input into an int guess."""
        if raw is None or raw == "":
            return False, None, "Enter a guess."
        
        try:
            if "." in raw:
                return False, None, "Please enter a whole number (no decimals)."
            guess = int(raw)
            return True, guess, None
        except ValueError:
            return False, None, "Invalid input. Please enter a number."
    
    def check_guess(guess: int, secret: int):
        """
        Compare guess to secret and return (outcome, message).
        Ensures both are integers for comparison.
        """
        try:
            guess_int = int(guess)
            secret_int = int(secret)
            
            if guess_int == secret_int:
                return "Win", "✅ Correct!"
            elif guess_int > secret_int:
                return "Too High", "⬆️ Go HIGHER!" # Message was wrong in original
            else:
                return "Too Low", "⬇️ Go LOWER!"   # Message was wrong in original
                
        except (ValueError, TypeError):
            # This handles cases where guess or secret couldn't be cleanly converted to int,
            # though parse_guess should catch bad 'guess' input.
            # We assume secret is intended to be int. If it's not, it's a bug in how it was set.
            return "Error", "Error comparing guess. Secret or guess is not a valid number."
    
    
    def update_score(current_score: int, outcome: str, attempt_number: int):
        """Update score based on outcome and attempt number."""
        if outcome == "Too High":
            if attempt_number % 2 == 0:
                return current_score + 5
            return current_score - 5
        
        if outcome == "Too Low":
            return current_score - 5
    
        return current_score
