from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
AC = list(accumulate(A))
AC2 = AC.copy()
ans = [0, 0]
# 最初の項が正の時
tmp = 0
for i in range(N):
    p = AC[i]+tmp
    if i % 2 == 0:
        if p > 0:
            continue
        elif p == 0:
            tmp += 1
            ans[0] += 1
        else:
            tmp += 1-p
            ans[0] += 1-p
    else:
        if p > 0:
            tmp += -1-p
            ans[0] += abs(-1-p)
        elif p == 0:
            tmp -= 1
            ans[0] += 1
        else:
            continue
# 最初の項が負の時
tmp = 0
for i in range(N):
    p = AC[i]+tmp
    if i % 2 != 0:
        if p > 0:
            continue
        elif p == 0:
            tmp += 1
            ans[1] += 1
        else:
            tmp += 1-p
            ans[1] += 1-p
    else:
        if p > 0:
            tmp += -1-p
            ans[1] += abs(-1-p)
        elif p == 0:
            tmp -= 1
            ans[1] += 1
        else:
            continue

print(min(ans))
