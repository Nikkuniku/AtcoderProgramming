N = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    for j in range(1, D[i - 1] + 1):
        S = set(list(str(i)) + list(str(j)))
        ans += len(S) == 1
print(ans)
