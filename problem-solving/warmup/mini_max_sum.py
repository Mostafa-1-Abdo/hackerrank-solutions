def min_max_sum(numbers: list) -> list:
    numbers_sum = sum(numbers)
    min_number = min(numbers)
    max_number = max(numbers)

    return [numbers_sum-max_number, numbers_sum-min_number]


numbers = list(map(int, input().strip().split()))

print(*min_max_sum(numbers))
