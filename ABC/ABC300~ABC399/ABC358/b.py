N, A = map(int, input().split())
T = list(map(int, input().split()))
ans = []
t = 0
for i in range(N):
    if T[i] <= t:
        t += A
        ans.append(t)
    else:
        t = T[i] + A
        ans.append(t)
print(*ans, sep="\n")
