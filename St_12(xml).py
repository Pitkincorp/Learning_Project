import xml.etree.ElementTree as ET

root = ET.fromstring(input())  # create root-object


def lev_count(root):

    def lev_recursion(root, level):
        level += 1
        for element in root.findall("cube"):
            ans[element.attrib['color']] += level
            lev_recursion(element, level)

    level = 1
    ans = {"red": 0, "green": 0, "blue": 0}
    ans[root.attrib['color']] += level
    lev_recursion(root, level)

    return f"{ans['red']} {ans['green']} {ans['blue']}"


print(lev_count(root))
