n, m = map(int, input().split())
ans = []
for k in range(1, 10):
    tmp = 0
    for j in range(n):
        tmp *= 10
        tmp += k
        tmp %= m
        if tmp == 0:
            ans.append((k, j+1))

if not ans:
    print(-1)
    exit()

ans.sort(key=lambda x: x[0], reverse=True)
ans.sort(key=lambda x: x[1], reverse=True)
k = str(ans[0][0])
print(k*ans[0][1])
