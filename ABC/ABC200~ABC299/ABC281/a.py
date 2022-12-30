N = int(input())
ans = []
for i in range(N, -1, -1):
    ans.append(i)
print(*ans, sep="\n")
