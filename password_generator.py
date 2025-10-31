import random


def generate_password(length, use_digits, use_special):
    """
    Generate a random password with customizable options.

    @param length (int): The length of the password. Default is 12.
    @param use_digits (bool): Whether to include digits (0-9)
    @param use_special (bool): Whether to include special characters

    @return (str): Randomly generated password.
    """

    # possible character strings
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "!@#$%^&*()_+"

    possible_characters = ""
    possible_characters = lower_letters + upper_letters

    if use_digits:
        possible_characters += digits

    if use_special:
        possible_characters += specials

    characters_list = list(possible_characters)

    password = ""
    for _ in range (length):
        password += random.choice(characters_list)

    return password


if __name__ == "__main__":
    print(generate_password(12, True, True))
    print(generate_password(14, True, False))
    print(generate_password(16, False, True))
    print(generate_password(18, False, False))
