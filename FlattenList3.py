def flatten(s):
    if not s:
        return []
    if type(s[0]) == list:
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])






c = flatten([[[[9]]], [1, 2], [[8]]])
print(c)