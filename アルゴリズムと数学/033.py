from math import sqrt
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ba = [a[0]-b[0], a[1]-b[1]]
bc = [c[0]-b[0], c[1]-b[1]]
cb = [b[0]-c[0], b[1]-c[1]]
ca = [a[0]-c[0], a[1]-c[1]]
s = abs(ba[0]*bc[1]-ba[1]*bc[0])

def vec_len(x):
    return sqrt(x[0]**2 + x[1]**2)
bc_len = vec_len(bc)
ba_len=vec_len(ba)

def inner_product(x,y):
    return x[0]*y[0]+x[1]*y[1]
ans = s/bc_len

if inner_product(ba,bc)<0 and inner_product(ca,cb)>=0:
    ans =vec_len(ba)
elif inner_product(ba,bc)>=0 and inner_product(ca,cb)<0:
    ans = vec_len(ca)
print(ans)
