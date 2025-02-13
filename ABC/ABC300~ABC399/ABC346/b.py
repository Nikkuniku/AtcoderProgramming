W, B = map(int, input().split())
S = "wbwbwwbwbwbw"
T = 30 * S
M = len(T)
ans = "No"
for i in range(M):
    for j in range(M + 1):
        T_tmp = T[i:j]
        if W == T_tmp.count("w") and B == T_tmp.count("b"):
            ans = "Yes"
print(ans)
