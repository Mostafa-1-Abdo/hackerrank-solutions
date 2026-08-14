def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        return "Empty String"
    else:
        return "".join(stack)


s = input().strip()
if s:
    print(superReducedString(s))
