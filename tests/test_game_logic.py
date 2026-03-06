
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score
import pytest

# ============ Tests for get_range_for_difficulty ============
def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_invalid_difficulty_defaults():
    low, high = get_range_for_difficulty("Extreme")
    assert low == 1
    assert high == 100

# ============ Tests for parse_guess ============
def test_parse_valid_guess():
    ok, guess, error = parse_guess("50")
    assert ok is True
    assert guess == 50
    assert error is None

def test_parse_negative_number():
    ok, guess, error = parse_guess("-5")
    assert ok is True
    assert guess == -5
    assert error is None

def test_parse_zero():
    ok, guess, error = parse_guess("0")
    assert ok is True
    assert guess == 0
    assert error is None

def test_parse_large_number():
    ok, guess, error = parse_guess("9999")
    assert ok is True
    assert guess == 9999
    assert error is None

def test_parse_decimal_rejected():
    ok, guess, error = parse_guess("50.5")
    assert ok is False
    assert guess is None
    assert error == "Please enter a whole number (no decimals)."

def test_parse_empty_string():
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."

def test_parse_none_input():
    ok, guess, error = parse_guess(None)
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."

def test_parse_invalid_input():
    ok, guess, error = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert error == "Invalid input. Please enter a number."

def test_parse_special_characters():
    ok, guess, error = parse_guess("!@#$")
    assert ok is False
    assert guess is None
    assert error == "Invalid input. Please enter a number."

def test_parse_whitespace():
    ok, guess, error = parse_guess("   ")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."

# ============ Tests for check_guess ============
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "✅ Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "⬇️ Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "⬆️ Go HIGHER!"

def test_check_guess_boundary_one_higher():
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"

def test_check_guess_boundary_one_lower():
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"

def test_check_guess_with_negative():
    outcome, message = check_guess(-10, -5)
    assert outcome == "Too Low"

def test_check_guess_with_zero():
    outcome, message = check_guess(0, 5)
    assert outcome == "Too Low"
    
def test_check_guess_both_zero():
    outcome, message = check_guess(0, 0)
    assert outcome == "Win"

def test_check_guess_string_conversion():
    # Test that string secret is handled (the app does this on even attempts)
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_string_guess():
    # Test that string guess is converted properly
    outcome, message = check_guess("60", 50)
    assert outcome == "Too High"

# ============ Tests for update_score ============
def test_update_score_win_first_attempt():
    score = update_score(0, "Win", 1)
    assert score == 80  # 100 - 10 * (1 + 1) = 80

def test_update_score_win_second_attempt():
    score = update_score(0, "Win", 2)
    assert score == 70  # 100 - 10 * (2 + 1) = 70

def test_update_score_win_tenth_attempt():
    score = update_score(0, "Win", 10)
    assert score == 10  # min is 10

def test_update_score_too_high_even_attempt():
    score = update_score(100, "Too High", 2)
    assert score == 105  # +5 on even attempts (attempt 2 is even)

def test_update_score_too_high_odd_attempt():
    score = update_score(100, "Too High", 1)
    assert score == 95  # -5 on odd attempts (attempt 1 is odd)

def test_update_score_too_low_any_attempt():
    score = update_score(100, "Too Low", 1)
    assert score == 95  # -5 always

def test_update_score_too_low_even_attempt():
    score = update_score(100, "Too Low", 2)
    assert score == 95  # -5 always

def test_update_score_unknown_outcome():
    score = update_score(100, "Unknown", 1)
    assert score == 100  # No change for unknown outcome
