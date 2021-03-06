def merge_two_list(a, b):
    reslist = []
    n = len(a)
    m = len(b)
    while n > 0 and m > 0:
        if a[0] < b[0]:
            reslist.append(a[0])
            a.pop(0)
            n -= 1
        else:
            reslist.append(b[0])
            b.pop(0)
            m -= 1
    if n == 0:
        reslist.extend(b)
    else:
        reslist.extend(a)
    return reslist


def median(a,b):
    reslist = merge_two_list(a, b)
    length = len(reslist)
    if length % 2:
        return float(reslist[length // 2])
    return (reslist[length // 2 - 1] + reslist[length // 2]) / 2


a = []
b = [2]

print(median(a, b))
