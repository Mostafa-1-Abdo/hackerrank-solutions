def marsExploration(s):
    expected = "SOS"
    changed_count = 0

    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            changed_count += 1

    return changed_count


s = input().strip()
print(marsExploration(s))
