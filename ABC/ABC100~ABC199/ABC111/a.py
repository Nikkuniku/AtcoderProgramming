n = input()
ans = []
for s in n:
    if s == "1":
        ans.append("9")
    else:
        ans.append("1")
print(*ans, sep="")
