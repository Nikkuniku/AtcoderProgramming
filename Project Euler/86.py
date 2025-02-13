l = 1700
r = 2000
L = 1000000
while r - l > 1:
    M = (l + r) // 2
    squares = set([i * i for i in range(1, 10 * M)])
    ans = set()
    isOK = False
    for a in range(1, M + 1):
        for b in range(a, M + 1):
            for c in range(b, M + 1):
                temp = min(
                    (a + b) ** 2 + c**2, (a + c) ** 2 + b**2, (b + c) ** 2 + a**2
                )
                if temp in squares:
                    ans.add(tuple(sorted([a, b, c])))
                if len(ans) > L:
                    print(M, len(ans))
                    isOK = True
                    break
            if isOK:
                break
        if isOK:
            break
    if isOK:
        r = M
    else:
        l = M
print(l, r)
