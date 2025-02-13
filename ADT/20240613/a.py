R, C = map(int, input().split())
R -= 1
C -= 1
A = [list(map(int, input().split())) for _ in range(2)]
print(A[R][C])
