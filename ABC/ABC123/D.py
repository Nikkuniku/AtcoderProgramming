x, y, z, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
a = a[:50]
b = b[:50]
c = c[:50]

tmp = []
for i in range(len(a)):
    for j in range(len(b)):
        tmp.append(a[i]+b[j])

ans = []
for k in range(len(tmp)):
    for m in range(len(c)):
        ans.append(tmp[k]+c[m])
ans = sorted(ans)[::-1]
print(*ans[:K], sep="\n")
