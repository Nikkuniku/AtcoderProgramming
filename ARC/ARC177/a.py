Coin = [1, 5, 10, 50, 100, 500][::-1]
C = list(map(int, input().split()))[::-1]
N = int(input())
X = list(map(int, input().split()))
ans = "No"
for i in range(N):
    tmp = X[i]
    for j in range(6):
        d = tmp // Coin[j]
        k = min(d, C[j])
        tmp -= k * Coin[j]
        C[j] -= k
        if tmp == 0:
            break
    if tmp > 0:
        exit(print(ans))
ans = "Yes"
print(ans)
