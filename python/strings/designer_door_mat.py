def door_mat_designer(n: int, m: int) -> str:
    door_mat_design = ""

    for i in list(range(0, (n-1) // 2)) + ["Welcome"] + list(range((n-1) // 2 - 1, -1, -1)):
        if i == "Welcome":
            door_mat_design += "WELCOME".center(m, "-") + "\n"
            continue

        door_mat_design += (".|." * (1 + i*2)).center(m, "-") + "\n"

    return door_mat_design


n, m = map(int, input().split())
print(door_mat_designer(n, m), end="")
