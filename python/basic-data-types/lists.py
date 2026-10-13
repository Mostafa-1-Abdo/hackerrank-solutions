N = int(input())

numbers = []
for _ in range(N):
    operation = input().strip().split()

    match operation:
        case ["append", e]:
            numbers.append(int(e))

        case ["insert", i, e]:
            numbers.insert(int(i), int(e))

        case ["pop"]:
            numbers.pop()

        case ["remove", e]:
            numbers.remove(int(e))

        case ["sort"]:
            numbers.sort()

        case ["reverse"]:
            numbers.reverse()

        case ["print"]:
            print(numbers)
