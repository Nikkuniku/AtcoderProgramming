n = int(input())
ans = [1]*(n+1)
for i in range(1, n+1):
    j = 2*i
    s = ans[i]
    while j <= n:
        ans[j] = s+1
        j += i
print(*ans[1:])
