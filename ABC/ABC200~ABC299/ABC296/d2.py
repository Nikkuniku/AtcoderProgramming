N, M = map(int, input().split())
if pow(N, 2) < M:
    print(-1)
    exit()
ans = float('inf')
for a in range(1, 10**6+1):
    b = (M+a-1)//a
    if a <= N and b <= N:
        ans = min(ans, a*b)
print(ans)
