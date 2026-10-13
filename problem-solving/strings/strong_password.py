import sys


def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_digit = any(char in numbers for char in password)
    has_lower = any(char in lower_case for char in password)
    has_upper = any(char in upper_case for char in password)
    has_special = any(char in special_characters for char in password)

    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1

    return max(missing_types, 6 - n)


n = int(input().strip())
password = input().rstrip('\r\n')

print(minimumNumber(n, password))
