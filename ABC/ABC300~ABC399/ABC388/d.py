N = int(input())
A = list(map(int, input().split()))
cum = [0] * (N + 2)
for i in range(N):
    if i > 0:
        cum[i] += cum[i - 1]
    A[i] += cum[i]
    if A[i] > 0:
        L = min(N - 1 - i, A[i])
        cum[i + 1] += 1
        cum[min(i + A[i] + 1, N + 1)] -= 1
        A[i] -= L
print(*A)
