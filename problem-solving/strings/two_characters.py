from itertools import combinations


def alternate(s):
    unique_chars = list(set(s))
    max_len = 0

    for c1, c2 in combinations(unique_chars, 2):
        filtered = [char for char in s if char == c1 or char == c2]

        is_valid = True
        for i in range(len(filtered) - 1):
            if filtered[i] == filtered[i + 1]:
                is_valid = False
                break

        if is_valid:
            max_len = max(max_len, len(filtered))

    return max_len


n = int(input().strip())
s = input().strip()

print(alternate(s))
