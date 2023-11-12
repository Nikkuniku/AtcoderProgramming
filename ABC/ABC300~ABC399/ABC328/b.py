N = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(D[i]):
        s = set(list(str(i + 1) + str(j + 1)))
        if len(s) == 1:
            ans += 1
print(ans)
