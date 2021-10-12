import json


def is_parent(parent, class_name, dict):
    if parent == class_name:
        return True
    if class_name in dict:
        if parent in dict[class_name]:
            return True
        elif dict[class_name]:
            for parents in dict[class_name]:
                if is_parent(parent,parents, js_dict):
                    return True


js_obj = json.loads(input())
js_dict = {x["name"]: x["parents"] for x in js_obj}

ans = {}
for class_name in js_dict:
    n = 0
    for parent in js_dict:
        if is_parent(parent, class_name, js_dict):
            n += 1
    ans[class_name] = n
for k,v in ans.items():
    print(f"{k} : {v}")