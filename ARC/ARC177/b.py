N = int(input())
S = list(input())
ans = []
ones = []
for i, v in enumerate(S):
    if v == "1":
        ones.append(i + 1)
ones = ones[::-1]
for v in ones:
    for _ in range(v):
        ans.append("A")
    for _ in range(v - 1):
        ans.append("B")
print(len(ans))
print(*ans, sep="")
