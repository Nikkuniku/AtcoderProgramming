N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = []
for i in range(N):
    tmp = []
    for j in range(N):
        if A[i][j]:
            tmp.append(j + 1)
    ans.append(tmp)
for c in ans:
    print(*c)
