def capitalize_text(text: str) -> str:
    capitalizedText = text.capitalize()
    return capitalizedText


def my_capitalize(text: str) -> str:
    return text[0].upper() + text[1:]


def truncate(text: str, max_len=20) -> str:
    return text[:max_len]


def count_words(text: str) -> int:
    return len(text.split())


def clamp(number: int, min_val: int = 0, max_val: int = 10) -> int:
    """clamp function restrict int to stay in certain range."""
    if number < min_val:
        return min_val
    if number > max_val:
        return max_val
    return number


## to check docstring use this commands
# print(clamp.__doc__)
# help(clamp)


def is_prime_number(number: int) -> bool:
    """Check if a number is prime."""
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """Return n! (factorial). n must be >= 0."""

    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def sum_number_list(numbers: list[int]) -> int:

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")

    sum = 0
    for number in numbers:
        sum += number
    return sum


def average(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("List cannot be empty")

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)
