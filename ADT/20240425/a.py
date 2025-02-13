S = input()
ans = []
for s in S:
    s = int(s)
    ans.append(s ^ 1)
print(*ans, sep="")
