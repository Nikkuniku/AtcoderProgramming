from bisect import bisect_right

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
C = [(sum(P[i]), i) for i in range(N)]
D = [sum(P[i]) for i in range(N)]
D.sort()
ans = ["No"] * N
for c, i in C:
    idx = bisect_right(D, c + 300)
    if N - idx + 1 <= K:
        ans[i] = "Yes"
print(*ans, sep="\n")
