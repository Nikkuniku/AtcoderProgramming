N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 1
for j in range(N):
    if ans >= j + 1:
        ans = A[ans - 1][j]
    else:
        ans = A[j][ans - 1]
print(ans)
