N, M = map(int, input().split())
A = []
A = [list(map(int, input().split())) for _ in range(N)]
C = sorted([int(input()) for _ in range(M)], reverse=True)
A.sort(key=lambda x: x[0], reverse=True)
A.sort(key=lambda x: x[1], reverse=True)
ans = 0
j = 0
for i in range(M):
    while j < N:
        s, v = A[j]
        if s <= C[i]:
            ans += 1
            j += 1
            break
        else:
            j += 1
print(ans)
