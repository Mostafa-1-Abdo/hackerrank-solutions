def get_runner_up(scores: set) -> int:
    return sorted(scores)[-2]


n = int(input())
scores = set(map(int, input().split()))

print(get_runner_up(scores))
