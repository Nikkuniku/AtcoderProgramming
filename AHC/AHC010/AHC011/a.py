ans = []
cnt = 0
for i in range(25):
    px = -10000
    py = -10000+600*i
    qx = px+1
    qy = py+1
    ans.append([px, py, qx, qy])
    cnt += 1
for i in range(25):
    px = -10000+600*i
    py = -10000
    qx = px+1
    qy = py+1
    ans.append([px, py, qx, qy])
    cnt += 1
for i in range(25):
    px = 10000-600*i
    py = -10000
    qx = px-1
    qy = py+1
    ans.append([px, py, qx, qy])
    cnt += 1
for i in range(25):
    px = 10000
    py = -10000+600*i
    qx = px-1
    qy = py+1
    ans.append([px, py, qx, qy])
    cnt += 1
print(len(ans))
for p in ans:
    print(*p)
