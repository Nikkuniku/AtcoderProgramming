def f(a, b):
    if a >= b:
        return a - b

    res = 1 << 60
    tmp = 0
    p, q = -1, -1
    for x in range(1000):
        for y in range(1000):
            if (b + y) % (a + x) == 0:
                tmp = x + y
                if tmp < res:
                    res = tmp
                    p, q = x, y
    return res, p, q


for a in range(1, 10):
    for b in range(a + 1, 20):
        print("a,b", a, b)
        print(f(a, b))
