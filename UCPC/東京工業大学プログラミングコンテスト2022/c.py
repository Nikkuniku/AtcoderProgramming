N = int(input())
NUM = 3
A = [sorted(list(map(int, input().split()))) for _ in range(NUM)]
A.sort()
print(N)
print(*A, sep="\n")
ans = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            ans += sorted([A[0][i], A[1][j], A[2][k]])[1]
print(ans)
