n = int(input())
a = list(map(int, input().split()))

day = []
pre = a[0]
tmp = [a[0]]
for i in range(1, n):
    if a[i] > pre:
        day.append(tmp)
        tmp = []
        tmp.append(a[i])
    else:
        tmp.append(a[i])
    pre = a[i]
day.append(tmp)

ans = [0]*n
i = 0
for d in day:
    if len(d) == 1:
        i += 1
    else:
        ma = max(d)
        mi = min(d)
        for j in range(len(d)):
            if d[j] == ma:
                ans[i+j] = 1
                break
        for j in range(len(d)-1, -1, -1):
            if d[j] == mi:
                ans[i+j] = 1
                break
        i += len(d)
print(*ans)
