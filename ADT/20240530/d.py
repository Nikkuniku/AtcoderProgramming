N, P = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans += a < P
print(ans)
