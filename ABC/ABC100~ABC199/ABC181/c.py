N = int(input())


def vec(a, b):
    return (b[0]-a[0], b[1]-a[1])


def cross(a, b):
    return abs(a[0]*b[1]-a[1]*b[0])


points = [list(map(int, input().split())) for _ in range(N)]
ans = 'No'
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            IJ = vec(points[i], points[j])
            JK = vec(points[j], points[k])
            if cross(IJ, JK) == 0:
                ans = 'Yes'
print(ans)
