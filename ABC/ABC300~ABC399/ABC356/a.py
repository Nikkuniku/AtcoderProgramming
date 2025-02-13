N, L, R = map(int, input().split())
A = [i + 1 for i in range(N)]
B = A[: L - 1] + A[L - 1 : R][::-1] + A[R:]
print(*B)
