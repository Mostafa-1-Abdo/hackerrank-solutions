def staircase(n: int) -> None:
    for i in range(1, n+1):
        print(("#" * i).rjust(n))


staircase(n=int(input().strip()))
