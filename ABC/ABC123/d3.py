x, y, z, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
ans = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if (i+1)*(j+1)*(k+1) <= K:
                ans.append(a[i]+b[j]+c[k])
            else:
                break
ans = sorted(ans)[::-1][:K]
print(*ans, sep="\n")
