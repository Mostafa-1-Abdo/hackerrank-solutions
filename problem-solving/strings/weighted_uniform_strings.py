import sys


def weightedUniformStrings(s, queries):
    weights = set()

    current_char = ''
    current_length = 0

    for char in s:
        if char == current_char:
            current_length += 1
        else:
            current_char = char
            current_length = 1

        char_weight = ord(char) - ord('a') + 1
        weights.add(char_weight * current_length)

    result = []
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result


def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return

    s = lines[0]
    n_queries = int(lines[1])
    queries = [int(x) for x in lines[2:2 + n_queries]]

    ans = weightedUniformStrings(s, queries)
    print('\n'.join(ans))


if __name__ == '__main__':
    solve()
