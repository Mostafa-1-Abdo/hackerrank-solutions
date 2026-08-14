
def split_and_join(line: str, separator: str) -> str:
    return separator.join(line.split())


print(split_and_join(input(), "-"))
