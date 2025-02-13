S = input()
ans = []
for s in S:
    if s in "aiueo":
        continue
    ans.append(s)
print(*ans, sep="")
