from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cuma = set()
cumb = set()
q = int(input())
querys = []
for i in range(q):
    x, y = map(int, input().split())
    querys.append((x, y, i))
querys.sort(key=lambda x: x[1])
querys.sort(key=lambda x: x[0])
d = defaultdict(int)
nowx = 0
nowy = 0
for i in range(q):
    x, y, _ = querys[i]
    while nowx < x:
        cuma.add(a[nowx])
        nowx += 1
    while nowy < y:
        cumb.add(b[nowy])
        nowy += 1
    if cuma == cumb:
        d[(x, y)] = 1
querys.sort(key=lambda x: x[2])
for i in range(q):
    x, y, _ = querys[i]
    if d[(x, y)] > 0:
        print('Yes')
    else:
        print('No')
