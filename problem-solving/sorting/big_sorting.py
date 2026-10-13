def big_sorting(numbers: list) -> list:
    numbers.sort(key=lambda x: (len(x), x))
    return numbers


n = int(input().strip())

numbers = []

for _ in range(n):
    numbers.append(input())

sorted_numbers = big_sorting(numbers)
for number in sorted_numbers:
    print(number)
