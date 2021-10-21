import xml.etree.ElementTree as ET

root = ET.fromstring(input())  # create root-object


def lev_count(root):
    level = 0
    ans = {"red": 0, "green": 0, "blue": 0}

    return f"{ans['red']} {ans['green']} {ans['blue']}"


print(lev_count(root))