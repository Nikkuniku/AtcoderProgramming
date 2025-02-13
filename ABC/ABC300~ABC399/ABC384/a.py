N, c1, c2 = input().split()
S = input()
ans = []
for s in S:
    if s != c1:
        ans.append(c2)
    else:
        ans.append(s)
print(*ans, sep="")
