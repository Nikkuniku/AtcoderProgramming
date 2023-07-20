H, M = map(int, input().split())
while 1:
    a = (H//10) % 10
    b = H % 10
    c = (M//10) % 10
    d = M % 10

    AC = 10*a+c
    BD = 10*b+d
    if 0 <= AC <= 23 and 0 <= BD <= 59:
        print(H, M)
        break
    M += 1
    if M == 60:
        H += 1
        M = 0
    if H == 24:
        H = 0
