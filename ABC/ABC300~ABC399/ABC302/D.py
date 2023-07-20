from bisect import bisect_right
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = -1

for ai in A:
    idx = bisect_right(B, ai+D)-1
    bi = B[idx]
    if abs(ai-bi) <= D:
        ans = max(ans, ai+bi)
print(ans)
