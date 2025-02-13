N, A = map(int, input().split())
T = list(map(int, input().split()))
ans = [-1] * N
now = 0
for i in range(N):
    if T[i] <= now:
        ans[i] = now + A
        now += A
    else:
        ans[i] = T[i] + A
        now = T[i] + A
print(*ans, sep="\n")
