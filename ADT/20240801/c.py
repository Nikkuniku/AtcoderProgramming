N, X = map(int, input().split())
A = list(map(int, input().split()))
B = [False] * N
X -= 1
B[X] = True
to = A[X] - 1
while not B[to]:
    B[to] = True
    to = A[to] - 1
print(sum(B))
