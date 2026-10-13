def swap_case(s: str):
    # Approach 1: Using built-in method (Most Efficient)
    # return s.swapcase()

    # Approach 2: Manual conversion
    new_s = ""

    for char in s:
        new_s += (char.lower() if char.isupper() else char.upper())

    return new_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
