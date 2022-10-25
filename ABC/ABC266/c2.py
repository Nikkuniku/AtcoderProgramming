import numpy as np
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))


def vec(u, v):
    return np.array([v[0]-u[0], v[1]-u[1]])


ab = vec(a, b)
ad = vec(a, d)
bc = vec(b, c)
cd = vec(c, d)
ABC = np.cross(ab, bc)
BCD = np.cross(bc, cd)
CDA = np.cross(cd, -ad)
DAB = np.cross(-ad, ab)
ans = 'No'
if ABC > 0 and BCD > 0 and CDA > 0 and DAB > 0:
    ans = 'Yes'
print(ans)
