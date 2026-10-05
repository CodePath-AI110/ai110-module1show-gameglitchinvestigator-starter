from logic_utils import check_guess, parse_guess, record_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_blank_guess_is_rejected():
    result = parse_guess(" ")
    assert result == (False, None, "Enter a guess.")


def test_non_numeric_guess_is_rejected():
    result = parse_guess("not a number")
    assert result == (False, None, "That is not a number.")


def test_valid_guess_is_parsed_as_an_integer():
    result = parse_guess("42")
    assert result == (True, 42, None)


def test_record_guess_updates_attempts_and_history_together():
    attempts, history = record_guess([25], 1, 50)
    assert attempts == 2
    assert history == [25, 50]


def test_record_guess_does_not_mutate_previous_history():
    previous_history = [25]
    record_guess(previous_history, 1, 50)
    assert previous_history == [25]


def test_wrong_guesses_reduce_score_consistently():
    assert update_score(10, "Too High", 1) == 5
    assert update_score(10, "Too Low", 1) == 5


def test_first_attempt_win_awards_full_score():
    assert update_score(0, "Win", 1) == 100
