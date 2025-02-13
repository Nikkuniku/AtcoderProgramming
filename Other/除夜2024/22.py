N, K = map(int, input().split())
A = list(map(int, input().split()))
B = A[-K:]
ans = B + A[: len(A) - K]
print(*ans)
