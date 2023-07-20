N = int(input())
ans = 1 << 60
for _ in range(N):
    A, P, X = map(int, input().split())
    if A >= X:
        continue
    ans = min(ans, P)
if ans == 1 << 60:
    ans = -1
print(ans)
