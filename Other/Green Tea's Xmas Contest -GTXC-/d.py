from bisect import bisect_left, bisect_right
N, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
p = 0
i = 0
while True:
    idx = bisect_right(A[i], p)
    if idx > L-1:
        break
    p = A[i][idx]
    ans += 1
    i += 1
    i %= N
print(ans)
