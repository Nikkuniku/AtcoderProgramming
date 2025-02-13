N = int(input())
K = list(map(int, input().split()))
S = sum(K)
ans = 1 << 60
for i in range(1 << N):
    temp = 0
    for j in range(N):
        if i & (1 << j):
            temp += K[j]
    res = max(temp, S - temp)
    ans = min(ans, res)
print(ans)
