N = int(input())
P = list(map(int, input().split()))

A = [[0] * N for _ in range(3)]
for i in range(N):
    pi = P[i]
    L = [pi - 1, pi, pi + 1]
    for j in range(3):
        k = L[j]
        if i <= k:
            A[j][i] = k - i
        else:
            A[j][i] = N - (i - k)
        A[j][i] %= N
M = [0] * N
for j in range(3):
    for i in range(N):
        v = A[j][i]
        M[v] += 1
print(max(M))
