def diagonalDifference(matrix: list[list]) -> int:
    left_to_right_diagonal = 0
    right_to_right_diagonal = 0

    for i in range(len(matrix)):
        left_to_right_diagonal += matrix[i][i]
        right_to_right_diagonal += matrix[i][len(matrix) - 1 - i]

    return abs(left_to_right_diagonal-right_to_right_diagonal)


n = int(input().strip())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

print(diagonalDifference(matrix))
