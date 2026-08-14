def compare_triplets(a: list, b: list) -> list:
    a_points = 0
    b_points = 0

    for i in range(3):
        if a[i] > b[i]:
            a_points += 1

        elif b[i] > a[i]:
            b_points += 1

    return [a_points, b_points]


a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
print(*compare_triplets(a, b))
