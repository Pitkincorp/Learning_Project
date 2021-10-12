def is_parent(parent, exception):
    if parent == exception:
        return True
    if exception in inh:
        if parent in inh[exception]:
            return True
        elif inh[exception] != "object":
            for parents in inh[exception]:  # Здесь с тупиковой ветки наследования возвращаемся \
                # к следующему родителю, чтобы проверить другую ветку наследования
                if is_parent(parent, parents):
                    return True


inh = {}
query = []
n = int(input())
for i in range(n):
    c_data = input().split()
    if len(c_data) > 1:
        inh[c_data[0]] = c_data[2:]
    else:
        inh[c_data[0]] = "object"

q = int(input())
for i in range(q):
    query.append(input())

l = len(query)
for i in range(1,l):
    flag = 0
    for j in range(i):
        if is_parent(query[j],query[i]):
            flag = 1
    if flag == 1:
        print(query[i])