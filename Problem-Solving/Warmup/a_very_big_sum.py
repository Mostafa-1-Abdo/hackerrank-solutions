def very_big_sum(numbers: list):
    return sum(numbers)


_ = int(input().strip())
numbers = list(map(int, input().rstrip().split()))
print(very_big_sum(numbers))
