h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
MOD = 998244353
ans = 1
for j in range(w):
    cnt = [0, 0, 0]
    i = 0
    while i < h and 0 <= j:
        if s[i][j] == 'R':
            cnt[0] += 1
        elif s[i][j] == 'B':
            cnt[1] += 1
        else:
            cnt[2] += 1
        i += 1
        j -= 1

    if cnt[0] > 0 and cnt[1] > 0:
        print(0)
        exit()
    if sum(cnt[:2]) == 0:
        ans *= 2
        ans %= MOD
for i in range(1, h):
    cnt = [0, 0, 0]
    j = w-1
    while i < h and 0 <= j:
        if s[i][j] == 'R':
            cnt[0] += 1
        elif s[i][j] == 'B':
            cnt[1] += 1
        else:
            cnt[2] += 1
        i += 1
        j -= 1

    if cnt[0] > 0 and cnt[1] > 0:
        print(0)
        exit()
    if sum(cnt[:2]) == 0:
        ans *= 2
        ans %= MOD

print(ans)
