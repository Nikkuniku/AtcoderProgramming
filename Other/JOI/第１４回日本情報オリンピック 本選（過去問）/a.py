N, M = map(int, input().split())
T = list(map(int, input().split()))
Used = [0]*N
for i in range(M-1):
    a, b = T[i]-1, T[i+1]-1
    if a > b:
        a, b = b, a
    Used[a] += 1
    Used[b] -= 1
for i in range(N-1):
    Used[i+1] += Used[i]
ans = 0
for i in range(N-1):
    a, b, c = map(int, input().split())
    k = Used[i]
    ans += min(k*a, k*b + c)
print(ans)
