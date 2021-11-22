from re import search, match

def myAtoi(s: str) -> int:

    s = s.lstrip(' ')
    if match(r'[0-9+-]', s[0]):
        if s[0] == '-':
            sign = -1
        else: sign = 1

    else:
        return 0



s = "   -42"
print(myAtoi(s))
