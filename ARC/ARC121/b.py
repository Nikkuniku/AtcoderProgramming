import bisect
n = int(input())
dogs = [[] for _ in range(3)]
for _ in range(2*n):
    a, c = input().split()
    a = int(a)
    if c == 'R':
        dogs[0].append(a)
    elif c == 'G':
        dogs[1].append(a)
    else:
        dogs[2].append(a)
seq = []
t = 0
oddseq = []
evenseq = []
for i in range(3):
    dogs[i].sort()
    t += len(dogs[i]) % 2
    if len(dogs[i]) % 2 == 0:
        evenseq = dogs[i]
    else:
        oddseq.append(dogs[i])

ans = 10**18
if t == 0:
    ans = 0
else:
    B = []
    G = []
    # (even,odd),(even,odd)のパターン
    if evenseq:
        for p in evenseq:
            idx_b = bisect.bisect_left(oddseq[0], p)
            idx_g = bisect.bisect_left(oddseq[1], p)
            tmp_b = 10**18
            tmp_g = 10**18
            for k in [-1, 0, 1]:
                nx_b = idx_b+k
                nx_g = idx_g+k

                if 0 <= nx_b < len(oddseq[0]):
                    tmp_b = min(tmp_b, abs(p-oddseq[0][nx_b]))

                if 0 <= nx_g < len(oddseq[1]):
                    tmp_g = min(tmp_g, abs(p-oddseq[1][nx_g]))

            B.append(tmp_b)
            G.append(tmp_g)

        G_ind = sorted([(x, i) for i, x in enumerate(G)],
                       key=lambda x: x[0])
        m1 = G_ind[0][0]
        m1_ind = G_ind[0][1]
        m2 = G_ind[1][0]

        for i in range(len(B)):
            if i != m1_ind:
                ans = min(ans, B[i]+m1)
            else:
                ans = min(ans, B[i]+m2)

    # (odd,odd)の時
    for p in oddseq[0]:
        idx_g = bisect.bisect_left(oddseq[1], p)
        for k in [-1, 0, 1]:
            nx_g = idx_g+k
            if 0 <= nx_g < len(oddseq[1]):
                ans = min(ans, abs(p-oddseq[1][nx_g]))
print(ans)
