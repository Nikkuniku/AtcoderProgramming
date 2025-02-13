N, C = map(int, input().split())
T = list(map(int, input().split()))
L = -1005
ans = 0
for i in range(N):
    if i == 0:
        L = T[i]
        ans += 1
        continue
    if T[i] - L >= C:
        L = T[i]
        ans += 1
print(ans)
