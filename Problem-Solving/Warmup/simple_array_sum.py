def array_sum(numbers: list) -> int:
    return sum(numbers)


_ = int(input().strip())
numbers = list(map(int, input().strip().split()))
print(array_sum(numbers))
