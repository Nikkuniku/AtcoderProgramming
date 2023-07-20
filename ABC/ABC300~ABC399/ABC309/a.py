from collections import defaultdict
A, B = map(int, input().split())
d = defaultdict(int)
for i in range(3):
    for j in range(3):
        d[3*i+(j+1)] = (i, j)
px, py = d[A]
qx, qy = d[B]
ans = 'No'
if abs(px-qx) == 0 and abs(py-qy) == 1:
    ans = 'Yes'
print(ans)
