def solve(s: str) -> str | None:
    if s is None:
        return None

    words = s.split(" ")

    return " ".join(word.capitalize() for word in words)


print(solve(input()))
