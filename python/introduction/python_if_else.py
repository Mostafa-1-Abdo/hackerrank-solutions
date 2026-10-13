n = int(input().strip())

if n == 0:
    print("Zero")

elif n % 2 != 0:
    print("Weird")

else:
    if n in (2, 4):
        print("Not Weird")

    elif n in range(6, 21, 2):
        print("Weird")

    else:
        print("Not Weird")
