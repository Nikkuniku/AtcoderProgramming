M = int(input())
ans = []
while M > 0:
    k = 10
    while pow(3, k) > M:
        k -= 1
    M -= pow(3, k)
    ans.append(k)
print(len(ans))
print(*ans)
