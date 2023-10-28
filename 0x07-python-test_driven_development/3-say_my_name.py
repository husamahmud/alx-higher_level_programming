# !/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints `My name is <first name> <last name>`.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Returns:
        None

    Raises:
        TypeError: If the first name or the last name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print('My name is {:s} {:s}'.format(first_name, last_name))


if __name__ == '__main__':
    say_my_name(1, "Smith")
    say_my_name("Alice", "White")
    say_my_name("Bob")
