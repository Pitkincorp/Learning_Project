import xml.etree.ElementTree as ET

root = ET.fromstring(input())  # create root-object


def lev_count(root):
    level = 0
    ans = {"red": 0, "green": 0, "blue": 0}

    def lev_recursion(root):
        nonlocal level
        nonlocal ans
        for element in root.ET.findall("cube"):
            pass

    return f"{ans['red']} {ans['green']} {ans['blue']}"


print(lev_count(root))
