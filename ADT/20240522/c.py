H, M = map(int, input().split())
while 1:
    h1 = (H // 10) % 10
    h2 = H % 10
    m1 = (M // 10) % 10
    m2 = M % 10

    h3 = 10 * h1 + m1
    m3 = 10 * h2 + m2
    if 0 <= h3 <= 23 and 0 <= m3 <= 59:
        exit(print(H, M))
    M += 1
    if M == 60:
        M = 0
        H += 1
        H %= 24
