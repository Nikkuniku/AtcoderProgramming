import datetime
H, M = map(int, input().split())

for i in range(2000):
    h = H
    m = M+i
    if m >= 60:
        h += m//60
        m = 0
    if h == 24:
        h = 0

    a, b = h//10, h % 10
    c, d = m//10, m % 10
    if 10*a+c <= 23 and 10*b+d <= 59:
        print(h, m)
        break
