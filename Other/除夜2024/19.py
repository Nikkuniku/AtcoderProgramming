N = int(input())
ans = []
for i in range(N):
    if i % 3 == 2:
        ans.append("x")
    else:
        ans.append("o")
print(*ans, sep="")
