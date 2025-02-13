N = int(input())
X = list(map(int, input().split()))
pos = []
neg = []
for x in X:
    if x > 0:
        pos.append(x)
    else:
        neg.append(x)
pos.sort()
neg.sort()
INF = 1 << 60
ans_max, ans_min = -INF, INF
if len(pos) >= 3:
    x, y, z = pos[-3], pos[-2], pos[-1]
    p, q, r = pos[0], pos[1], pos[2]
    ans_min = min(ans_min, (x + y + z) / (x * y * z))
    ans_max = max(ans_max, (p + q + r) / (p * q * r))
if len(neg) >= 3:
    x, y, z = neg[-3], neg[-2], neg[-1]
    p, q, r = neg[0], neg[1], neg[2]
    ans_min = min(ans_min, (p + q + r) / (p * q * r))
    ans_max = max(ans_max, (x + y + z) / (x * y * z))
pos2 = pos[:5] + pos[-5:]
neg2 = neg[:5] + neg[-5:]
if len(pos) < 10:
    pos2 = pos
if len(neg) < 10:
    neg2 = neg

for x in pos:
    for i in range(len(neg2)):
        for j in range(i + 1, len(neg2)):
            y, z = neg2[i], neg2[j]
            tmp = (x + y + z) / (x * y * z)
            ans_max = max(ans_max, tmp)
            ans_min = min(ans_min, tmp)
for x in neg:
    for i in range(len(pos2)):
        for j in range(i + 1, len(pos2)):
            y, z = pos2[i], pos2[j]
            tmp = (x + y + z) / (x * y * z)
            ans_max = max(ans_max, tmp)
            ans_min = min(ans_min, tmp)
print(ans_min)
print(ans_max)
