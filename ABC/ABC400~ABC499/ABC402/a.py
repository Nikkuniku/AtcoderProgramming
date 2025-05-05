from string import ascii_uppercase

S = input()
ans = []
for s in S:
    if s in ascii_uppercase:
        ans.append(s)
print(*ans, sep="")
