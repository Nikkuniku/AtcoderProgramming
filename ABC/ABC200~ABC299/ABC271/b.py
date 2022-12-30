n, q = map(int, input().split())
seqs = [list(map(int, input().split())) for _ in range(n)]
ans = []
for _ in range(q):
    s, t = map(int, input().split())
    ans.append(seqs[s-1][t])

print(*ans, sep="\n")
