S = list(input())
while S[-1] == "0":
    S.pop()
if S[-1] == ".":
    S.pop()
print(*S, sep="")
