h1, w1 = map(int, input().split())
a = [list(input().split()) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(input().split()) for _ in range(h2)]

for i in range(2**h1):
    for j in range(2**w1):
        a_tmp = []
        for k in range(h1):
            if (i >> k) & 1:
                tmp = []
                for m in range(w1):
                    if (j >> m) & 1:
                        tmp.append(a[k][m])
                a_tmp.append(tmp)
        if a_tmp:
            height = len(a_tmp)
            width = len(a_tmp[0])

            if height == h2 and width == w2:
                cnt = 0
                for s in range(h2):
                    for t in range(w2):
                        if a_tmp[s][t] == b[s][t]:
                            cnt += 1

                if cnt == h2*w2:
                    print('Yes')
                    exit(0)
print('No')
