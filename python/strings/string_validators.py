# def has_any_upper_letter(s: str) -> bool:
#    for char in s:
#        if char.isupper():
#            return True
#    return False


# def has_any_lower_letter(s: str) -> bool:
#    for char in s:
#        if char.islower():
#            return True
#    return False


# def has_any_alphabetical(s: str) -> bool:
#    for char in s:
#        if char.isalpha():
#            return True
#    return False


# def has_any_digit(s: str) -> bool:
#    for char in s:
#        if char.isdigit():
#            return True
#    return False


# def has_any_alphanumeric(s: str) -> bool:
#    for char in s:
#        if char.isalnum():
#            return True
#    return False
#

s = input()

print(any(char.isalnum() for char in s))
print(any(char.isalpha() for char in s))
print(any(char.isdigit() for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))
