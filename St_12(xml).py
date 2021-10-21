import xml.etree.ElementTree as ET

root = ET.fromstring(input())

level = 0


def lev_count():
    pass


print(root.tag, root.attrib)