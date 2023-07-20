N, K = map(int, input().split())
L = list(map(int, input().split()))
L = sorted(L)[::-1]
ans = sum(L[:K])
print(ans)
