d = {}
while 1:
    it = input().split(sep=':')
    if it==['конец']:
       break
    d[it[0]]=int(it[1])

for it in sorted(d.items(),key=lambda it: it[1],reverse=True):
    print(it[0])