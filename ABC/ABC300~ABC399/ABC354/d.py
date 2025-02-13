A, B, C, D = map(int, input().split())
S = [2, 1, 0, 1]
T = [1, 2, 1, 0]
ans = 0
if B % 2 == 0:
    if D % 2 == 0:
        g = (D - B) // 2
        o = (D - B) // 2
    else:
        g = (D - B + 1) // 2
        o = (D - B) // 2
else:
    if D % 2 == 0:
        g = (D - B) // 2
        o = (D - B + 1) // 2
    else:
        g = (D - B) // 2
        o = (D - B) // 2
# 偶数
ans += ((C - A) // 4) * sum(S) * g
tmp = 0
if abs(A - C) <= 4:
    if not (A % 4 == 0 and C % 4 == 0):
        if A % 4 <= C % 4:
            for i in range(A % 4, C % 4):
                tmp += S[i]
        else:
            for i in range(A % 4, 4):
                tmp += S[i]
            for i in range(C % 4):
                tmp += S[i]
else:
    if not (A % 4 == 0 and C % 4 == 0):
        for i in range(A % 4, 4):
            tmp += S[i]
        for i in range(C % 4):
            tmp += S[i]
ans += tmp * g
# 奇数
ans += ((C - A) // 4) * sum(T) * g
tmp = 0
if abs(A - C) <= 4:
    if not (A % 4 == 0 and C % 4 == 0):
        if A % 4 <= C % 4:
            for i in range(A % 4, C % 4):
                tmp += T[i]
        else:
            for i in range(A % 4, 4):
                tmp += T[i]
            for i in range(C % 4):
                tmp += T[i]
else:
    if not (A % 4 == 0 and C % 4 == 0):
        for i in range(A % 4, 4):
            tmp += T[i]
        for i in range(C % 4):
            tmp += T[i]
ans += tmp * o
print(ans)
