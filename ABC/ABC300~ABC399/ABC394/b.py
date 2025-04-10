N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append((len(s), s))
S.sort()
ans = []
for _, t in S:
    ans.append(t)
print(*ans, sep="")
