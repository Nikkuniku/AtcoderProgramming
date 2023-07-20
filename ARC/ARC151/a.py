N = int(input())
S = input()
T = input()
cnt = sum([1 if S[i] != T[i] else 0 for i in range(N)])
if cnt % 2 != 0:
    print(-1)
    exit()
HS, HT = 0, 0
ans = []
for i in range(N):
    res = '0'
    if S[i] == T[i]:
        pass
    else:
        if HS == cnt//2:
            res = S[i]
            HT += 1
        elif HT == cnt//2:
            res = T[i]
            HS += 1
        else:
            res = '0'
            if S[i] != res:
                HS += 1
            elif T[i] != res:
                HT += 1
    ans.append(res)
print(''.join(ans))
