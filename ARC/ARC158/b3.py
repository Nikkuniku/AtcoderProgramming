X = list(map(int, input().split()))
X.sort()
N = len(X)
INF = 1 << 60
ans_max, ans_min = -INF, INF
p_max, q_max, r_max = -1, -1, -1
p_min, q_min, r_min = -1, -1, -1
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x, y, z = X[i], X[j], X[k]
            tmp = (x + y + z) / (x * y * z)
            if ans_max < tmp:
                ans_max = tmp
                p_max, q_max, r_max = x, y, z
            if tmp < ans_min:
                ans_min = tmp
                p_min, q_min, r_min = x, y, z

print(X)
print("最大値", ans_max)
print("argmax", p_max, q_max, r_max)
print("最小値", ans_min)
print("argmin", p_min, q_min, r_min)
