N, D = map(int, input().split())
A = 0
B = 0
C = 0
while True:
    if D % 2 == 0:
        A += 1
        D //= 2
    elif D % 3 == 0:
        B += 1
        D //= 3
    elif D % 5 == 0:
        C += 1
        D //= 5
    else:
        break
if D != 1:
    print(0)
    exit()

dp1 = [[[0]*(C+2) for _ in range(B+2)] for _ in range(A+2)]
dp1[0][0][0] = 1
dice = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (2, 0, 0), (0, 0, 1), (1, 1, 0)]
for _ in range(N):
    dp2 = [[[0]*(C+2) for _ in range(B+2)] for _ in range(A+2)]
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                for x, y, z in dice:
                    dp2[min(a+x, A)][min(b+y, B)][min(c+z, C)] += dp1[a][b][c]

    dp1 = dp2

ans = dp1[A][B][C]/pow(6, N)
print(ans)
