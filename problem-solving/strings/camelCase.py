def camelcase(s):
    return sum(1 for char in s if char.isupper()) + 1


s = input().strip()
print(camelcase(s))
