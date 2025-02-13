N = int(input())
ans = [1]
for i in range(N):
    ans.append(0)
ans[-1] = 7
print(*ans, sep="")
