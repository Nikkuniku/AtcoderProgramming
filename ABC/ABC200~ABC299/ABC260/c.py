n, x, y = map(int, input().split())

a = [0]*11
b = [0]*11

a[n] = 1
for i in range(n, 1, -1):
    # 1
    p = a[i]
    a[i-1] += p
    b[i] += x*p
    # 2
    q = b[i]
    a[i-1] += q
    b[i-1] += y*q

print(b[1])
