def introTutorial(V: int, numbers: list) -> int:
    return numbers.index(V)


V = int(input().strip())
_ = int(input().strip())
numbers = list(map(int, input().strip().split()))
print(introTutorial(V, numbers))
