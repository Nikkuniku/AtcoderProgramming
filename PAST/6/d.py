from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))
cum = list(accumulate(A, initial=0))
ans = []
for i in range(N - K + 1):
    temp = cum[i + K] - cum[i]
    ans.append(temp)
print(*ans, sep="\n")
