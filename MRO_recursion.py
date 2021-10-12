def find_parent(parent, class_name):
    if parent == class_name:
        return True
    if class_name in inh:
        if parent in inh[class_name]:
            return True
        elif inh[class_name] != "object":
            for parents in inh[class_name]:  # Здесь с тупиковой ветки наследования возвращаемся \
                # к следующему родителю, чтобы проверить другую ветку наследования
                if find_parent(parent, parents):
                    return True


inh = {}
n = int(input())
for i in range(n):
    c_data = input().split()
    if len(c_data) > 1:
        inh[c_data[0]] = c_data[2:]
    else:
        inh[c_data[0]] = "object"

q = int(input())
for i in range(q):
    print("Yes" if find_parent(*input().split()) else "No")
