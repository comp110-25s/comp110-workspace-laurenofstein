"Wordle Exercise 2"

__author__: str = "730710469"


def contains_char(search_string: str, char: str) -> bool:
    """
    Checks if a single character exists in a given string.

    Args:
        search_string (str): The string to search through.
        char (str): The single character to search for.

    Returns:
        bool: True if the character is found in the string, False otherwise.
    """
    # Ensure the second argument is a single character
    assert len(char) == 1, f"len('{char}') is not 1"

    index = 0
    while index < len(search_string):
        if search_string[index] == char:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """
    Compares a guess to a secret word and returns an emoji string representing the comparison.

    Args:
        guess (str): The user's guess.
        secret (str): The secret word.

    Returns:
        str: A string of emojis representing the comparison results.
    """
    # Ensure the guess and secret are the same length
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"  # White box for incorrect letters
    GREEN_BOX: str = (
        "\U0001F7E9"  # Green box for correct letters in the correct position
    )
    YELLOW_BOX: str = (
        "\U0001F7E8"  # Yellow box for correct letters in the wrong position
    )

    result = ""
    index = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            result += GREEN_BOX  # Green box for correct position
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX  # Yellow box for correct letter, wrong position
        else:
            result += WHITE_BOX  # White box for incorrect letter
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """
    Prompts the user for a guess and ensures it is the correct length.

    Args:
        expected_length (int): The expected length of the guess.

    Returns:
        str: The user's guess of the correct length.
    """
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} chars! Try again.")
        guess = input(f"Enter a {expected_length} character word: ")
    return guess


def main(secret: str) -> None:
    """
    Implements the Wordle game loop.

    Args:
        secret (str): The secret word to be guessed.
    """
    turns = 6
    current_turn = 1

    print(f"=== Turn {current_turn}/{turns} ===")
    guess = input_guess(len(secret))
    while current_turn < turns and guess != secret:
        print(emojified(guess, secret))
        current_turn += 1
        print(f"=== Turn {current_turn}/{turns} ===")
        guess = input_guess(len(secret))

    if guess == secret:
        print(emojified(guess, secret))
        print(f"You won in {current_turn}/{turns} turns!")
    else:
        print(emojified(guess, secret))
        print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
