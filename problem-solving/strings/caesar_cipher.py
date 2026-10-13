def caesarCipher(s, k):
    k = k % 26
    result = []

    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(ord('a') + (ord(char) - ord('a') + k) % 26)
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr(ord('A') + (ord(char) - ord('A') + k) % 26)
            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)


n = int(input().strip())
s = input().rstrip('\r\n')
k = int(input().strip())

print(caesarCipher(s, k))
