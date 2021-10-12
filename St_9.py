import json

def is_child(parent, child, dict):
    if parent == child:
        return True
    if child in dict[parent]:
        return False
    if child in dict:
        if parent in dict[child]:
            return True
        elif dict[child]:
            for parents in dict[child]:
                if is_child(parent, parents, js_dict):
                    return True
    return False

js_obj = json.loads(input())
js_dict = {x["name"]: x["parents"] for x in js_obj}

ans = {}
for parent in js_dict:
    n = 0
    for class_name in js_dict:
        if is_child(parent, class_name, js_dict):
            n += 1
    ans[parent] = n
for k,v in sorted(ans.items()):
    print(f"{k} : {v}")