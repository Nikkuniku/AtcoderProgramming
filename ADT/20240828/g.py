N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]
B = []
for i in range(N + M - N + 1):
    p = A[0]
    q = C[i]
    b = q // p
    B.append(b)
    for k in range(N + 1):
        C[i + k] -= A[k] * b
print(*B[::-1])
