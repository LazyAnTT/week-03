def is_email(text: str) -> bool:
    """Return True if text is a simple email containing one @ and a dot after it."""
    if not isinstance(text, str):
        return False

    if text.count("@") != 1:
        return False

    local_part, domain_part = text.split("@")

    if local_part == "" or domain_part == "":
        return False

    if "." not in domain_part:
        return False

    return True


def is_phone_number(text: str) -> bool:
    """Return True if text matches the Latvian phone format +371 XXXXXXXX."""
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):
        return False

    number_part = text[5:]

    if len(number_part) != 8:
        return False

    if not number_part.isdigit():
        return False

    return True


def is_valid_age(age: int) -> bool:
    """Return True if age is an integer between 0 and 150 inclusive."""
    if type(age) is not int:
        return False

    if 0 <= age <= 150:
        return True

    return False


def is_strong_password(text: str) -> bool:
    """Return True if password has at least 8 characters and contains letters and digits."""
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = False
    has_digit = False

    for char in text:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    return has_letter and has_digit


def is_valid_date(text: str) -> bool:
    """Return True if text matches basic YYYY-MM-DD format and month/day ranges."""
    if not isinstance(text, str):
        return False

    if len(text) != 10:
        return False

    if text[4] != "-" or text[7] != "-":
        return False

    year = text[0:4]
    month = text[5:7]
    day = text[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    month = int(month)
    day = int(day)

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    return True


if __name__ == "__main__":
    print("Email tests:")
    print("is_email('anna@inbox.lv') ->", is_email("anna@inbox.lv"))
    print("is_email('anna') ->", is_email("anna"))
    print("is_email('anna@') ->", is_email("anna@"))
    print("is_email('@inbox.lv') ->", is_email("@inbox.lv"))
    print()

    print("Phone number tests:")
    print("is_phone_number('+371 26123456') ->", is_phone_number("+371 26123456"))
    print("is_phone_number('26123456') ->", is_phone_number("26123456"))
    print("is_phone_number('+371 1234567') ->", is_phone_number("+371 1234567"))
    print("is_phone_number('+371 123456789') ->", is_phone_number("+371 123456789"))
    print()

    print("Age tests:")
    print("is_valid_age(0) ->", is_valid_age(0))
    print("is_valid_age(25) ->", is_valid_age(25))
    print("is_valid_age(150) ->", is_valid_age(150))
    print("is_valid_age(-1) ->", is_valid_age(-1))
    print("is_valid_age(151) ->", is_valid_age(151))
    print()

    print("Password tests:")
    print("is_strong_password('abc12345') ->", is_strong_password("abc12345"))
    print("is_strong_password('abcdefgh') ->", is_strong_password("abcdefgh"))
    print("is_strong_password('12345678') ->", is_strong_password("12345678"))
    print("is_strong_password('ab12') ->", is_strong_password("ab12"))
    print()

    print("Date tests:")
    print("is_valid_date('2025-12-31') ->", is_valid_date("2025-12-31"))
    print("is_valid_date('2025-01-01') ->", is_valid_date("2025-01-01"))
    print("is_valid_date('2025-13-10') ->", is_valid_date("2025-13-10"))
    print("is_valid_date('2025-12-32') ->", is_valid_date("2025-12-32"))
    print("is_valid_date('25-12-31') ->", is_valid_date("25-12-31"))
