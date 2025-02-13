N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
cuma, cumb = 0, 0
for i in range(N):
    cuma += A[i]
    cumb += B[i]
    if cuma > X:
        exit(print(i + 1))
    if cumb > Y:
        exit(print(i + 1))
print(N)
