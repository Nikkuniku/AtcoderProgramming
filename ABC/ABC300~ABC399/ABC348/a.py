N = int(input())
ans = []
for i in range(1, N + 1):
    res = "o"
    if i % 3 == 0:
        res = "x"
    ans.append(res)
print(*ans, sep="")
