X = [-6, -6, -4, -4, -3, -3, -2, -2, 1, 2, 3, 4, 5, 6]
pos = []
neg = []
for x in X:
    if x > 0:
        pos.append(x)
    else:
        neg.append(x)
for x in pos:
    ans_max = -(1 << 60)
    ans_min = 1 << 60
    p_max, q_max, r_max = -1, -1, -1
    p_min, q_min, r_min = -1, -1, -1
    M = len(neg)
    for i in range(M):
        for j in range(i + 1, M):
            y = neg[i]
            z = neg[j]
            tmp = (x + y + z) / (x * y * z)
            if ans_max < tmp:
                ans_max = tmp
                p_max, q_max, r_max = x, y, z
            if tmp < ans_min:
                ans_min = tmp
                p_min, q_min, r_min = x, y, z
    print("---------")
    print("x", x)
    print("最大値", ans_max)
    print("argmax", p_max, q_max, r_max)
    print("最小値", ans_min)
    print("argmin", p_min, q_min, r_min)
