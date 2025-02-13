N, M = map(int, input().split())
ans = 0
for _ in range(N):
    S, R = input().split()
    if S[:4].count("x") > 0 and int(R) >= 1200:
        ans += 1
print(ans)
