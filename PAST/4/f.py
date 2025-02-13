from collections import Counter

N, K = map(int, input().split())
S = [input() for _ in range(N)]
C = Counter(S)
A = C.most_common()
M = A[K - 1][1]
ans = A[K - 1][0]
cnt = 0
for k, v in A:
    if v == M:
        cnt += 1
if cnt > 1:
    ans = "AMBIGUOUS"
print(ans)
