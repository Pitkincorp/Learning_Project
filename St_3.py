import requests, re

req = requests.get("http://pastebin.com/raw/7543p0ns")
# with open("adds.html", 'wb') as file:
#     file.write(req.content)
#
# with open("adds.html") as file:
#     text = file.read()
text = req.text
    # print(text)
print(*sorted(
    list(set([i[2] for i in re.findall(r'<a.*?href=[\'"](\.\.)?(.+?://)?([\.\w-]*).*[\'"].*>', text) if i[2]]))),
      sep="\n")
    # print(i[1])
