def print_rangoli(size: int) -> None:
    width = 4 * size - 3

    for i in list(range(1, size+1)) + list(range(size-1, 0, -1)):
        row_chars = []
        for j in range(i):
            row_chars.append(chr(96+size-j))

        row_chars += row_chars[-2::-1]
        print("-".join(row_chars).center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
