n = int(input())
points = []
for _ in range(n):
    p = list(map(int, input().split()))
    points.append(p)

ans = 10**9
for i in range(n):
    for j in range(i+1, n):
        p = points[i]
        q = points[j]
        tmp = ((p[0]-q[0])**2+(p[1]-q[1])**2)**0.5
        ans = min(ans, tmp)
print(ans)
