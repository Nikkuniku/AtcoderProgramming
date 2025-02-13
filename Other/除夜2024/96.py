N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
for j in range(M):
    temp = 0
    for i in range(N):
        temp += X[i][j]
    if temp < A[j]:
        exit(print("No"))
print("Yes")
