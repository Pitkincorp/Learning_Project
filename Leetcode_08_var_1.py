from re import search, match

def myAtoi(s: str) -> int:

    s = s.lstrip(' ')
    if not s:
        return 0
    if match(r'[0-9+-]', s[0]):
        if s[0] == '-':
            sign = -1
        else: sign = 1
        num = search(r'[0-9]+', s)
        if num and num.start() in (0,1):
            num = int(num.group()) * sign
        else:
            return 0
        if num < - 2 ** 31:
            return - 2 ** 31
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return num
    else:
        return 0



s = ""
print(myAtoi(s))

# match(r' *([+-]?)([0-9]+).*', "    -2+37 as").group(1,2)
