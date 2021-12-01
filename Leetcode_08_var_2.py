def myAtoi(s: str) -> int:
    if not s:
        return 0
    i = 0
    start = end = None
    sign = 1
    length = len(s)
    while i < length:
        if s[i] == " ":
            i += 1
        else: break
    if i >= length:
        return 0
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    if i < length and s[i] in '0123456789':
        start = i
        i += 1
        end = i
    else: return 0
    while i < length:
        if not s[i] in '0123456789':
            end = i
            break
        else: i += 1
    else: end = i
    if start is None:
        return 0
    else:
        num = int(s[start:end]) * sign
    if num < - 2 ** 31:
        return - 2 ** 31
    if num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return num


s = " "
print(myAtoi(s))
