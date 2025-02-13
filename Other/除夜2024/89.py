def dist(px, py, qx, qy):
    return (px - qx) ** 2 + (py - qy) ** 2


N = int(input())
Points = [list(map(int, input().split())) for _ in range(N)]
ans = []
for i in range(N):
    temp = []
    for j in range(N):
        if j == i:
            continue
        temp.append((dist(*Points[i], *Points[j]), j + 1))
    temp.sort(key=lambda x: x[1])
    temp.sort(key=lambda x: x[0], reverse=True)
    ans.append(temp[0][1])
print(*ans, sep="\n")
