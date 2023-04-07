import re


def is_valid_email(email):
    email_regex = r'^[\w]+[\.\w-]*@[\w]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_letters_only(input_string):
    return bool(re.match('^[a-zA-Z]+$', input_string))


def is_digits_only(input_string):
    return input_string.isdigit()


def contains_substring(input_string, substring):
    return substring in input_string


def char_length(string: str, number_of_characters: int = 3):
    if len(string) < number_of_characters:
        return True
    else:
        return False


def password_match(passwordOne: str, passwordTwo: str):
    return passwordOne == passwordTwo
