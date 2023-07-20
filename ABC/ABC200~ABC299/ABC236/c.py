N, M = map(int, input().split())
ans = []
S = list(input().split())
M = set(input().split())
for s in S:
    res = 'No'
    if s in M:
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
