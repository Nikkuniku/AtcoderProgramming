N, M = map(int, input().split())
if pow(N, 2) < M:
    print(-1)
    exit()
ans = float('inf')
for a in range(1, int(M**0.5)+5):
    b = (M+a-1)//a
    if 1 <= a <= N and 1 <= b <= N:
        ans = min(ans, a*b)
print(ans)
