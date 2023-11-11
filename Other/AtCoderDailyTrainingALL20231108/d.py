N, Q = map(int, input().split())
Seq = [list(map(int, input().split())) for _ in range(N)]
ans = []
for _ in range(Q):
    s, t = map(int, input().split())
    ans.append(Seq[s - 1][t])
print(*ans, sep="\n")
