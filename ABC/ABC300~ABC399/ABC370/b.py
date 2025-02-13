N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
i = 1
for j in range(1, N + 1):
    if i >= j:
        i = A[i - 1][j - 1]
    else:
        i = A[j - 1][i - 1]
print(i)
