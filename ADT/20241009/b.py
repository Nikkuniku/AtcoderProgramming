S = input()
ans = []
for s in S:
    if s in "a,e,i,o,u":
        continue
    ans.append(s)
print(*ans, sep="")
