### 1. What was broken when I started?

During my initial testing of the Glitchy Guesser app, I identified the following bugs:

* **Logic Bug: Reversed High/Low Hints**
    * **What happened:** When I entered a guess higher than the secret number, the game told me to "Go HIGHER!" When I guessed lower, it told me to "Go LOWER!"
    * **Expected behavior:** A guess higher than the secret should return a "Too High / Go LOWER" hint, and a guess lower should return "Too Low / Go HIGHER."

* **UI/State Bug: Score and History Not Resetting**
    * **What happened:** Clicking the "New Game 🔁" button refreshed the secret number, but the player's Score and the Guess History remained from the previous session.
    * **Expected behavior:** Starting a new game should wipe the history clean and reset the score to 0.

* **Logic Bug: Invalid Inputs Penalized**
    * **What happened:** Entering non-numeric text (like "abc") or leaving the guess blank still counted as a valid attempt, reducing the "Attempts left" counter and negatively affecting the score.
    * **Expected behavior:** The app should validate that the input is a whole number before processing it as an attempt.

* **UI Bug: Difficulty Sync Issue**
    * **What happened:** Changing the difficulty in the sidebar (e.g., from Normal to Hard) updated the "Attempts allowed" text in the sidebar, but the main game area still showed the old attempt limit until a manual reset or a guess was made.
    * **Expected behavior:** The game state and UI should immediately reflect the parameters of the newly selected difficulty level.

* **Logic Bug: Inconsistent Attempt Counting**
    * **What happened:** Occasionally, the "Attempts left" counter in the blue info box failed to decrease after a valid numeric guess was submitted.
    * **Expected behavior:** Every valid submission should decrement the remaining attempts by exactly one.