N, M = map(int, input().split())
S = input().split("0")
ans = 0
for s in S:
    p = s.count("1")
    q = s.count("2")
    tmp = max(p - M, 0) + q
    ans = max(ans, tmp)
print(ans)
