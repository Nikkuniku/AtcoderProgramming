N = int(input())
A = list(map(int, input().split()))
ans = 0
B = [0] * 4
for v in A:
    B[0] += 1
    for j in range(3, -1, -1):
        if j + v >= 4:
            ans += B[j]
        else:
            B[j + v] += B[j]
        B[j] = 0
print(ans)
