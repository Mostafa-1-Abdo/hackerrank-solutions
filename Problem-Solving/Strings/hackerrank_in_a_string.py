def pangrams(s):
    s = s.lower()

    letters = set(char for char in s if 'a' <= char <= 'z')

    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"


s = input().strip()
print(pangrams(s))
