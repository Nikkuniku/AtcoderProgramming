N, M = map(int, input().split())
S = list(input().split())
T = set(list(input().split()))
ans = []
for s in S:
    res = "No"
    if s in T:
        res = "Yes"
    ans.append(res)
print(*ans, sep="\n")
