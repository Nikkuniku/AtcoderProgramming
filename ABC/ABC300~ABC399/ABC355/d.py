from bisect import bisect_right

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x: x[1])
S.sort(key=lambda x: x[0])
L = [S[i][0] for i in range(N)]
R = [S[i][1] for i in range(N)]
ans = 0
for i in range(N):
    l = L[i]
    r = R[i]
    idx = bisect_right(L, r)
    ans += max(idx - i - 1, 0)
print(ans)
