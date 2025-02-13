N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
ans = N
X -= sum(M)
ans += X // min(M)
print(ans)
