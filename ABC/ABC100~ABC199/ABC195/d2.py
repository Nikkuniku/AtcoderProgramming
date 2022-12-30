n, m, q = map(int, input().split())
goods = []
for _ in range(n):
    goods.append(tuple(map(int, input().split())))
box = list(map(int, input().split()))
goods.sort(key=lambda x: x[0])
goods.sort(key=lambda x: x[1], reverse=True)
ans = []
for _ in range(q):
    l, r = map(int, input().split())
    usebox = []
    for i in range(m):
        if l <= i+1 <= r:
            continue
        usebox.append(box[i])
    usebox.sort()
    unused = [True]*len(usebox)
    tmp = 0
    for g in goods:
        for i in range(len(usebox)):
            if g[0] <= usebox[i] and unused[i]:
                tmp += g[1]
                unused[i] = False
                break
    ans.append(tmp)
print(*ans, sep="\n")
