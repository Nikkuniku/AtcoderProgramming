N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = 0
for s in S:
    isOK = False
    for t in T:
        isOK |= s.endswith(t)
    ans += isOK
print(ans)
