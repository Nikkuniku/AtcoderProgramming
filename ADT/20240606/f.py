N = int(input())
S = input()
isdot = True
ans = []
for s in S:
    if isdot:
        if s == '"':
            isdot = False
            ans.append(s)
        elif s == ",":
            ans.append(".")
        else:
            ans.append(s)
    else:
        if s == '"':
            isdot = True
        ans.append(s)
print(*ans, sep="")
