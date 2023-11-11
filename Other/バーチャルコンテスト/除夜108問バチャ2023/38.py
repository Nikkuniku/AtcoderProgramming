S = [list(input()) for _ in range(10)]
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                tmp = [list('..........')for _ in range(10)]
                for i in range(a, b+1):
                    for j in range(c, d+1):
                        tmp[i][j] = '#'

                if S == tmp:
                    print(a+1, b+1)
                    print(c+1, d+1)
                    break
