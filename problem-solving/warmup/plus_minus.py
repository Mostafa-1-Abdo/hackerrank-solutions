
def calculate_positive_negative_zero_ratios(numbers: list) -> list:
    positive_count = 0
    zero_count = 0
    negative_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1

        elif number == 0:
            zero_count += 1

        else:
            negative_count += 1

    return [positive_count / len(numbers), negative_count / len(numbers), zero_count / len(numbers)]


_ = int(input().strip())
numbers = list(map(int, input().rstrip().split()))

for i in calculate_positive_negative_zero_ratios(numbers):
    print(i)
