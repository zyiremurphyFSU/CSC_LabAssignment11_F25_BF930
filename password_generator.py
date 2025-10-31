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
    # TODO: concat lower_letters and upper_letters into 'possible_characters'

    # TODO: if 'use_digits' is True, concat 'digits' to 'possible_characters'

    # TODO: if 'use_special' is True, concat 'specials' to 'possible_characters'

    # TODO: build a list from 'possible_characters' so that each character is a list item

    password = ""
    # TODO: use loop to generate the random password

    return password


if __name__ == "__main__":
    print(generate_password(12, True, True))
    print(generate_password(14, True, False))
    print(generate_password(16, False, True))
    print(generate_password(18, False, False))
