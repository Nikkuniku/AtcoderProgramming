N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def judge(X, Y, Z):
    S = (Y[1]-X[1])*(Z[0]-X[0])-(Y[0]-X[0])*(Z[1]-X[1])
    if S == 0:
        return False
    return True


ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if judge(points[i], points[j], points[k]):
                ans += 1
print(ans)
