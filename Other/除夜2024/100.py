N = int(input())
Garveges = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
ans = []
for _ in range(Q):
    t, d = map(int, input().split())
    q, r = Garveges[t - 1]
    mod = d % q
    if r - mod >= 0:
        ans.append(d + r - mod)
    else:
        ans.append(d + q - mod + r)
print(*ans, sep="\n")
