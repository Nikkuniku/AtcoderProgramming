N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set([input() for _ in range(M)])
ans = 0
for s in S:
    t = s[-3:]
    if t in T:
        ans += 1
print(ans)
