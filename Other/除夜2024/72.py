N = int(input())
Titan = [list(map(int, input().split())) for _ in range(N)]
S = 0
for a, b in Titan:
    S += a
ans = 0
for a, b in Titan:
    ans = max(ans, S - a + b)
print(ans)
